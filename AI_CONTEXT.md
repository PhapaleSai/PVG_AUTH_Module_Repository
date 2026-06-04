# 🤖 PVG College ERP Auth Module — Developer & AI Context Guide

Welcome to the **Central Authentication & Role-Based Access Control (RBAC) Module** for the PVG College ERP ecosystem. 

This document serves as the **master context guide** for developers and AI assistants. It explains the system architecture, setup steps, database restoration, and code-level function flows to enable a frictionless transition and future enhancement.

---

## 📁 1. Project Directory Layout

```
pvg-auth/
├── backend/                       # Python FastAPI backend core
│   ├── routes/                    # API route controllers
│   │   ├── admin.py               # Administrative metrics & user listing
│   │   ├── auth.py                # Core auth routes (login, register, refresh, logout)
│   │   ├── student.py             # Legacy student signup & profile routes
│   │   └── ... (modules/features/permissions/logs)
│   ├── auth.py                    # Token creation, verification, and password hashing
│   ├── database.py                # SQLAlchemy engine & SessionLocal sessionmaker
│   ├── models.py                  # Database SQLAlchemy Models & AuditMixin
│   ├── schemas.py                 # Pydantic Schemas for type validation
│   ├── main.py                    # App entry point, CORS middleware, and root routes
│   └── requirements.txt           # Python dependencies
├── frontend/                      # React (Vite) frontend portals
│   ├── admin/                     # Administrative management dashboard (port 5173)
│   └── user/                      # Student personal profile portal (port 5175)
├── database_scripts/              # Schema & Database seeding/export scripts
│   ├── pvg_auth_full_dump.sql     # MASTER DUMP: Full schema + seeded tables
│   ├── setup_auth_tables.sql      # DDL only schema
│   └── export_full_db.py          # Utility script to export DB dump
├── start_all.ps1                  # PowerShell script to run everything in one-click
└── README.md                      # Basic setup documentation
```

---

## 🛠️ 2. Technology Stack & Key Libraries

### **Backend Core (Python)**
* **FastAPI**: Asynchronous web framework used for fast, type-safe REST APIs.
* **Uvicorn**: High-performance ASGI server for running the FastAPI application.
* **SQLAlchemy 2.0+**: ORM used to map python classes to PostgreSQL tables.
* **Psycopg2**: Database driver for PostgreSQL connectivity.
* **Passlib (with bcrypt)**: Secure cryptographic library used for hashing and verifying passwords (using standard salt-rounds).
* **Python-Jose**: Used to generate, sign, and decode JSON Web Tokens (JWT).
* **Slowapi**: Implements rate-limiting on authentication endpoints (Token Bucket algorithm).

### **Frontend Core (JavaScript/CSS)**
* **React 18 (Vite)**: For building fast single-page interfaces.
* **Vanilla CSS / Custom HSL Variables**: For modern glassmorphism styling, custom shadows, and animations.
* **Axios**: HTTP client used to interact with backend endpoints.

### **Infrastructure**
* **PostgreSQL (Local / Docker)**: Central database running on port `5432`.
* **Ngrok reverse-tunneling**: For creating secure, public URLs of local servers to test cross-module integrations.

---

## 💾 3. Database Dump & Import (Zero Dependency Setup)

To free new developers from manual schema setup and empty database tables, the complete database (structure + seeded rows) is version-controlled inside the repository.

### **Seeded Data in the Dump**
The dump file [database_scripts/pvg_auth_full_dump.sql](file:///d:/taking_my_code_out/database_scripts/pvg_auth_full_dump.sql) contains:
* **All ERP Modules & Features** (Admission, Student Information, Fees, Placement, etc.).
* **Granular Permissions Catalog** (VIEW, CREATE, EDIT, APPROVE actions for every feature).
* **Complete RBAC Roles Mapping** (`admin`, `student`, `teacher`, `hod`, `principal`, `guest`).
* **Initial Test Users & Student Records** (pre-migrated and active).

### **How to Import the Database Dump**
1. Ensure **PostgreSQL** is running on your system (`localhost:5432`).
2. Log into your PostgreSQL client (pgAdmin or psql shell) and create a database named `pvg_auth`:
   ```sql
   CREATE DATABASE pvg_auth;
   ```
3. Run the import command from the terminal in the root directory:
   ```bash
   psql -U postgres -d pvg_auth -f database_scripts/pvg_auth_full_dump.sql
   ```
   *(Enter password `sai123` or your configured PostgreSQL password).*

---

## 🌐 4. Ngrok Configuration & Setup

### **Why ngrok is used**
Because the college ERP is designed as a series of **decoupled micro-frontends** (Auth, SIS, Fees, Admission, etc.), they run on different localhost ports or different developer machines. Ngrok tunnels allow these services to communicate seamlessly using HTTPS endpoints over the public internet.

### **How to Install & Configure Ngrok**
1. **Download**: Download the ngrok zip for Windows from the [Official Website](https://ngrok.com/download) or install via Chocolatey:
   ```powershell
   choco install ngrok
   ```
2. **Authenticate**: Create a free ngrok account to get your Authtoken. Configure it locally:
   ```bash
   ngrok config add-authtoken YOUR_AUTHTOKEN
   ```
3. **Ecosystem Tunnel Startup**:
   The repository includes a customized tunnel configuration file: `ngrok_dual.yml`. 
   To start the tunnels, run:
   ```powershell
   .\ngrok_bin\ngrok.exe start --all --config=ngrok_dual.yml
   ```
   This will spin up the tunnels routing traffic to your local portals.

### **CORS Bypass & Fallback**
By default, free ngrok tunnels show an intermediate warning page to human visitors. When the frontend tries to call the backend APIs, the browser intercepts this warning page as a CORS blocker.
* **Our Solution**: In [backend/main.py](file:///d:/taking_my_code_out/backend/main.py#L82-L88), we have updated the CORS configuration to use `allow_origin_regex="https?://.*"` and `allow_credentials=True`.
* **Frontend Bypassing**: Ensure frontend Axios/Fetch requests include the following header to bypass the warning:
  ```javascript
  headers: {
    "ngrok-skip-browser-warning": "true"
  }
  ```

---

## 🔄 5. Key Authentication Flows & Functions

### **A. User Login (`POST /api/auth/login`)**
* **File Location**: [backend/routes/auth.py](file:///d:/taking_my_code_out/backend/routes/auth.py#L74-L215)
* **Function Flow**:
  1. Receives `username` (email) and `password`.
  2. **JIT Migration Check**: If the user is not found in the `users` table, it checks the legacy `students` table. If found there, it matches the password using bcrypt, migrates their profile to the `users` table, assigns them the `Student` role in `user_roles`, and commits the transaction.
  3. **Verification**: Compares the provided password against the bcrypt hash in the `users` table.
  4. **Access Token Creation**: Generates a JWT containing `sub` (email), `role`, `user_id`, `username`, and `full_name`. Expires in **60 minutes** (`ACCESS_TOKEN_EXPIRE_MINUTES`).
  5. **Refresh Token Creation**: Generates a long-lived JWT containing user identifier and `type: "refresh"`. Expires in **7 days** (`REFRESH_TOKEN_EXPIRE_DAYS`).
  6. **DB Token Tracking**: Clears old tokens for the user in `user_tokens` and inserts the new access and refresh token pair with their respective expiries.
  7. Logs a successful or failed entry in `login_log`.

### **B. Token Refresh (`POST /api/auth/refresh`)**
* **File Location**: [backend/routes/auth.py](file:///d:/taking_my_code_out/backend/routes/auth.py#L298-L390)
* **Function Flow**:
  1. Receives the `refresh_token` from the frontend.
  2. Decodes the token to verify the signature and checks that its claim `"type" == "refresh"`.
  3. Checks the `user_tokens` database table to make sure the token is active (`is_active = True`).
  4. Verifies if the token has expired by comparing `refresh_token_expiry` against the current UTC timestamp.
  5. **Token Rotation**: Generates a new Access Token (60m) and a new Refresh Token (7d).
  6. Updates the database row with the new tokens and expiries (preventing token reuse).
  7. Returns both new tokens to the client.

### **C. Root-Level Profile Lookup (`GET /me` Fallback)**
* **File Location**: [backend/main.py](file:///d:/taking_my_code_out/backend/main.py#L123-L171)
* **Function Flow**:
  * Serves as a root-level fallback when frontends omit the `/api` prefix (making requests directly to `/me` instead of `/api/me` or `/api/student/me`).
  * Extracts the Bearer token from the `Authorization` header.
  * Attempts to verify the user session using the modern `get_current_user` logic.
  * If that fails, it falls back to checking the session using the legacy `get_current_student` logic.
  * On success, returns the unified profile payload (ID, email, roles).

---

## 📈 6. Status of the System (What is Done)

* **Central User Registry**: Unified PostgreSQL schema with 9 cleanly separated tables.
* **Zero-Downtime Migration**: Active JIT student-to-user migration on login.
* **SSO Integrations**: Query-parameter token passing implemented for student portal redirections.
* **Admin Portal**: Multi-card telemetry dashboards, live audits, and dynamic RBAC role assignment forms.
* **CSS System**: Unified `#881f42` (Burgundy/Crimson) brand styling with interactive pink-glow inputs (`.pink-glow-input`).
* **CORS & ngrok Compliance**: Open access configuration for local tunnels and local React development servers.

---

## 🚀 7. Roadmap & Tasks for Future Students

If you are continuing development on this module, here is a list of features you can implement next:

1. **Email / SMS OTP Verification (2FA)**:
   * Integrate an email gateway (like SendGrid or FastAPI-Mail) to send a 6-digit OTP code to users on login, verification, or registration.
2. **OAuth2 Integration (Google Sign-In)**:
   * Add Google OAuth2 endpoints to `/api/auth/login` to allow faculty and students to log in using their official institutional google accounts.
3. **Password Reset Flow**:
   * Create an endpoint `/api/auth/forgot-password` that generates a short-lived password reset token, emails it to the user, and validates it on `/api/auth/reset-password`.
4. **Session Management Panel**:
   * Build a view in the User Portal (`:5175`) showing a list of active devices/browsers where their account is logged in, with the ability to "Log out from all other devices" (deactivating all other entries in `user_tokens`).
5. **Interactive Logs Dashboard**:
   * Add a graphical layout (charts) on the Admin dashboard to visualize login patterns, peak usage hours, and failed login alerts.
