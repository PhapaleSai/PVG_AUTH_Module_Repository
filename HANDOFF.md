# PVG College Auth & Enterprise Management System - Handoff & Knowledge Transfer

Welcome to the KT/Handoff document. This guide is designed to provide the next developers or teams taking over the project with a comprehensive overview of the current state, recent accomplishments, system architecture, and future roadmap.

---

## 1. Project Overview

The PVG College Auth & Enterprise Management System is a unified authentication, authorization, and administrative suite. It manages users and roles across the entire ERP ecosystem of the college (Admission, Fees, Placement, etc.).

**Core Technology Stack:**
*   **Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL, Passlib/Bcrypt (for auth)
*   **Frontend:** React 18 (Vite), Vanilla CSS (Custom HSL/Glassmorphism)
*   **Infrastructure:** PostgreSQL database, Ngrok (for dual-tunnel micro-frontend bridging)

---

## 2. Current State & Recent Accomplishments

The foundational authentication and RBAC (Role-Based Access Control) architecture is fully implemented. Recent updates leading up to this handoff include:

*   **Unified Database & Seeding**: Provided a master DB dump (`pvg_auth_full_dump.sql`) containing the schema, seeded roles, permissions, and test accounts.
*   **Test User Scripts**: Implemented automated python scripts in `database_scripts/` to seed testing accounts for various roles: TPOs (Placement Officers), Alumni, Parents, and Employers.
*   **Enhanced UI/UX**: 
    *   Applied "Pink Glow" styles to input fields and centered action buttons on the login portals.
    *   Updated the Admin Dashboard greeting to dynamically display the logged-in user's role (instead of a hardcoded string).
    *   Fixed CSS grid layouts on the Permissions Modal to prevent right-column clipping.
    *   Cleaned up the dashboard by removing mock Node Status widgets.
*   **Code Quality & Infrastructure**: 
    *   Formatted the core backend with `black`.
    *   Updated CORS settings for seamless local development and Ngrok integration.
    *   Centralized documentation (like `AI_CONTEXT.md` and this `HANDOFF.md`).

---

## 3. System Architecture & Key Flows

The system relies on a **Central Authentication Mechanism** with JWT tokens. 
*   **Login Flow (`POST /api/auth/login`)**: Verifies credentials and generates an Access Token (60m) and a Refresh Token (7d). Includes a Just-In-Time (JIT) migration that automatically shifts legacy "students" into the unified "users" table upon their first login.
*   **Token Refresh (`POST /api/auth/refresh`)**: Handles rotation of access/refresh tokens to maintain secure, persistent sessions.
*   **Ngrok Bridging**: Uses dual ngrok tunnels to allow the different frontends (Admin port `5173`, User port `5175`) to communicate locally via public HTTPS URLs without triggering CORS blocks. (A custom header `ngrok-skip-browser-warning` is used by the frontend).

> [!NOTE]
> For a deeper, code-level explanation of these flows and exact file locations, refer to the **[AI_CONTEXT.md](file:///d:/taking_my_code_out/AI_CONTEXT.md)** file included in this repository.

---

## 4. Environment & Quick Setup

To get the ecosystem running on your local machine quickly:

### 1. Database Initialization
Ensure PostgreSQL is running locally on port `5432`.
```sql
CREATE DATABASE pvg_auth;
```
Import the dump to set up tables and seed data:
```bash
psql -U postgres -d pvg_auth -f database_scripts/pvg_auth_full_dump.sql
```

### 2. Environment Variables
Create a `.env` file in the `backend/` directory:
```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/pvg_auth
JWT_SECRET=6950526b1649fdd3c7e15d430812376a2c775156cc9510cefd8c4dc9e9d69e5a
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```
> [!IMPORTANT]
> The `JWT_SECRET` must remain consistent across all future ERP modules so they can decode these auth tokens.

### 3. One-Click Master Startup
Run the master PowerShell script from the root to launch the backend, both frontends, and ngrok tunnels simultaneously:
```powershell
.\start_all.ps1
```

---

## 5. Future Roadmap & Pending Tasks

For the next team continuing the development, here are the immediate priorities (also listed in the AI Context guide):

1.  **Email / SMS OTP Verification (2FA)**: Add an email gateway (e.g., SendGrid) for 2FA on login or registration.
2.  **OAuth2 Integration**: Implement Google Sign-In via `api/auth/login` for institutional accounts.
3.  **Password Reset Flow**: Build an `/api/auth/forgot-password` endpoint sending reset links.
4.  **Session Management**: Create a view in the User portal to let users see active login sessions and "Log out from all other devices".
5.  **Interactive Admin Logs**: Add charting (e.g., Recharts) to the Admin dashboard to visualize login patterns and failed attempts.
