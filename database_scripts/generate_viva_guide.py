# -*- coding: utf-8 -*-
import os

def generate_guide():
    filepath = r"D:\taking_my_code_out\docs\viva_prep_guide.md"
    
    content = """# 🎓 PVG ERP Authentication Module — Viva Exam Preparation Guide
This preparation guide contains **40 high-probability viva questions and answers** compiled directly from your project report, codebase, database design, and role implementation. 

Use this to prepare for your Institutional Project / Industrial Training Viva Examination next week!

---

## 📌 Section 1: Project Overview, Motivation & Scope

### Q1. What is the core objective of your project?
* **Answer:** The primary objective is to implement a secure, centralized, and stateless **Authentication and Authorization Module** using Role-Based Access Control (RBAC) that serves as the unified security gateway for the PVG College of Science & Commerce ERP system.

### Q2. Why did you choose a decoupled architecture (React for frontend, FastAPI for backend)?
* **Answer:** 
  * **React** allows building a fast, component-based, single-page application (SPA) with a modern user experience (smooth transitions, responsive designs).
  * **FastAPI** is chosen for the backend because it is one of the fastest Python web frameworks (due to Starlette and Pydantic), naturally supports asynchronous requests (`async/await`), auto-generates Swagger API documentation, and simplifies type validation.

### Q3. What is the scope of your module within the entire PVG ERP system?
* **Answer:** The scope encompasses user registration, secure login validation, stateless session management using JWT, password security (bcrypt), role-based access control (RBAC), security audit logging (login logs), and cross-module SSO redirection (teleporting users securely to SIS, Fees, and Admission modules via callback URLs).

### Q4. What are the major limitations of the legacy systems in colleges?
* **Answer:** Traditional systems store passwords in plain text or weak hashes, lack role segregation (allowing students to potentially access administrative endpoints), lack token-based session validation (leading to session-hijacking vulnerability), and have no audit trail for user activities.

### Q5. What is the "least privilege" principle, and how is it applied in your project?
* **Answer:** The principle states that a user should only have the minimum permissions necessary to perform their role. In our module, every newly registered user is automatically assigned the role **`Guest`** (which has zero elevated privileges) until the administrator explicitly assigns them a higher role (e.g., Student, Teacher, HOD, principal, admin).

---

## 📌 Section 2: Technical Architecture & System Flow

### Q6. Walk me through the step-by-step sequence when a user logs in.
* **Answer:** 
  1. The user inputs their credentials (Email and Password) on the React login page.
  2. The frontend sends an HTTP POST request to the backend endpoint `/api/auth/login`.
  3. The backend validates the input and queries the PostgreSQL database for the user's record.
  4. The password hash is compared with the entered password using **`bcrypt`**.
  5. On success, the backend generates an access JWT token containing claims (email, user_id, role, etc.).
  6. The token is logged in the `user_tokens` table.
  7. The backend returns the token and user payload. The frontend stores it in `localStorage` and redirects the user to the `/welcome` landing page.

### Q7. How does the SSO (Single Sign-On) redirection work between your Auth module and other modules (like SIS, Fees, Admission)?
* **Answer:** When a user logs in, the backend checks for a `redirect_uri` parameter. If present, and the user is authenticated, the system redirects them to that module's callback URL (e.g. `http://localhost:5174/callback` for SIS) appending the token, user ID, role, and name as secure query parameters:
  `?token=<token>&user_id=<id>&role=<role>&name=<name>`
  The target module accepts these parameters, saves the token, and grants access.

### Q8. What is `ngrok` and why did you use it in your project?
* **Answer:** **`ngrok`** is a reverse-proxy tool that exposes local web servers (running on localhost) to the public internet via secure tunnels. We used it to test the integration between our local Auth module and other external modules (like Admission) during development, allowing secure API callbacks without public domain hosting.

### Q9. What is the role of Docker and Docker Compose in your project?
* **Answer:** Docker containerizes our application modules (Frontend, Backend, Database) into isolated containers. Docker Compose coordinates them, ensuring that the exact same versions of PostgreSQL, Python libraries, and Node.js packages run on everyone's computer, eliminating "it works on my machine" bugs.

### Q10. What is the stateless nature of JWT authentication?
* **Answer:** It means the server does not need to store active session states in memory or constantly query the database to verify if a user is logged in. All the necessary information (user ID, role, expiration) is contained inside the token itself. The server only needs to decrypt and verify the token signature to authorize requests.

---

## 📌 Section 3: Security, Hashing, & JWT

### Q11. What is the difference between hashing and encryption?
* **Answer:** 
  * **Hashing** is a one-way, irreversible function. You cannot retrieve the original password from its hash (e.g., `bcrypt`). It is used for verifying passwords.
  * **Encryption** is a two-way function that can be decrypted back to plain text using a key. It is used to protect data in transit or storage.

### Q12. Why is `bcrypt` preferred over MD5 or SHA256 for password hashing?
* **Answer:** MD5 and SHA256 are designed to be extremely fast cryptographic algorithms, making them vulnerable to modern GPU-based brute-force and rainbow table attacks. **`bcrypt`** uses a slow key derivation function with an adjustable work factor (salt rounds), which computationally slows down brute-force attacks. It also automatically incorporates a unique salt for each password to prevent rainbow table matches.

### Q13. Explain the structure of a JSON Web Token (JWT).
* **Answer:** A JWT consists of three parts separated by dots (`.`):
  1. **Header:** Contains the token type (JWT) and the signing algorithm (e.g., HS256).
  2. **Payload:** Contains the claims (e.g. `sub`, `email`, `role`, `user_id`, `username`, `exp`).
  3. **Signature:** Generated by combining the encoded header, encoded payload, and a secret key (`JWT_SECRET`) using the specified algorithm. It ensures the token has not been tampered with.

### Q14. What is the `JWT_SECRET` key and what happens if it is compromised?
* **Answer:** The `JWT_SECRET` is the private key used to sign and verify the integrity of JWTs. If compromised, an attacker can generate valid tokens for any user, bypass the login screen completely, and assign themselves the `admin` role, compromising the entire system.

### Q15. How does your backend handle token expiration?
* **Answer:** Every JWT contains an `"exp"` (expiration) claim set to a Unix timestamp (calculated as `now + ACCESS_TOKEN_EXPIRE_MINUTES`). The authentication middleware checks this claim on every request; if the current time exceeds the expiration time, the backend rejects it with a `401 Unauthorized` HTTP status code.

### Q16. How does your backend prevent brute-force attacks on the login screen?
* **Answer:** We integrated the **`Slowapi`** library, which uses the Token Bucket algorithm to implement rate-limiting. The `/api/auth/login` endpoint is limited to **5 attempts per minute per IP address**. Exceeding this rate returns a `429 Too Many Requests` error.

### Q17. How do you protect against Cross-Origin Resource Sharing (CORS) issues?
* **Answer:** In FastAPI, we configure the `CORSMiddleware` in `main.py`, specifying allowed origins (`allow_origins`), allowed headers, and allowed HTTP methods. This enables our React frontend (running on port 5173) to securely communicate with the FastAPI backend (running on port 8000).

---

## 📌 Section 4: Database Design & Schema

### Q18. Explain the database structure of your Auth system.
* **Answer:** The database consists of 9 core tables:
  1. `users`: Stores user credentials and profile details.
  2. `roles`: Catalog of roles.
  3. `user_roles`: Many-to-many relationship mapping users to roles.
  4. `user_tokens`: Tracks active session tokens and expiries.
  5. `modules`: ERP subsystems (SIS, Fees, Admission).
  6. `features`: Views/components in modules.
  7. `permissions`: Actions (CREATE, VIEW, EDIT, DELETE, APPROVE).
  8. `role_permissions`: Core of RBAC, maps roles to specific permissions.
  9. `login_log`: Audit trail recording IP, device, and status of logins.

### Q19. Why did you use many-to-many relationships for users and roles?
* **Answer:** In a real-world college ERP, a single user can hold multiple roles simultaneously. For instance, a professor can be a **`Teacher`** for their classes and also a **`HOD`** for department management, or an **`accountant`** could also be a **`placement_officer`**. A junction table `user_roles` supports this flexibility.

### Q20. What is the difference between Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC)?
* **Answer:**
  * **RBAC** grants permissions based on a user's assigned role (e.g., an HOD can manage users).
  * **ABAC** grants access based on attributes of the user, resource, or environment (e.g. allowing access only during working hours of 9 AM to 5 PM, or only to users in a specific department). Our ERP primarily relies on RBAC.

### Q21. Explain the role of `AuditMixin` in your database models.
* **Answer:** The `AuditMixin` is an abstract class in `models.py` containing columns like `created_at`, `updated_at`, `created_by`, `updated_by`, and `token_expiry`. Every table inheriting from this mixin automatically implements these columns, providing complete traceability on when and by whom rows were created or modified.

### Q22. Why did you drop the Admission module tables from the pvg_auth database?
* **Answer:** The original database contained 14 unused legacy tables related to admission processing (e.g. `brochure_request`, `documents`, `student_applications`). Since the Admission module is now a separate microservice with its own database, keeping these tables in the Auth database violated the single-responsibility principle and created redundancy. We dropped them to leave exactly 9 auth-related tables.

---

## 📌 Section 5: Code-Level Implementation Details

### Q23. What is the JIT (Just-In-Time) user migration logic in your login route?
* **Answer:** When a user logs in, the backend first checks the `users` table. If not found, it queries the legacy `students` table. If the user exists there and the password is correct, the backend automatically migrates their record (username, full_name, email, hashed password) to the new `users` table, assigns them the `Student` role in `user_roles`, and commits the transaction. This enables zero-downtime migration of legacy students.

### Q24. How do you implement FastAPI Dependency Injection in authentication?
* **Answer:** We use FastAPI's `Depends()` function. For example, `db: Session = Depends(get_db)` injects a database session into endpoints, and `current_user: models.User = Depends(get_current_user)` resolves and validates the JWT token from the HTTP authorization header, verifying the session before running the endpoint code.

### Q25. What is the purpose of the `OAuth2PasswordBearer` class in your code?
* **Answer:** It defines the token URL (`/api/auth/login`) and automatically extracts the Bearer token from the `Authorization: Bearer <token>` header of incoming HTTP requests.

### Q26. How is user password verification implemented in code?
* **Answer:** We use the `passlib.context.CryptContext` library configured with `bcrypt`. We call `pwd_context.verify(plain_password, hashed_password)`, which hashes the plain password using the salt extracted from the hashed password and performs a constant-time comparison to protect against timing attacks.

### Q27. What is a "constant-time comparison" and why is it important for security?
* **Answer:** It is a password comparison method that takes the exact same amount of time regardless of whether the passwords match. This prevents attackers from using timing attacks (measuring microsecond differences in database response times) to guess password characters.

---

## 📌 Section 6: User Interface & Frontend Styling

### Q28. What modifications did you make to the login page form inputs?
* **Answer:** 
  * Changed the first input label from `REGISTERED EMAIL-ID` $\rightarrow$ `Email`.
  * Changed the second input label from `Secret Key` (Admin) / `Security Credentials` (User) $\rightarrow$ `Password`.
  * Positioned the labels consistently and changed their color to the primary college color (`var(--erp-primary)`).
  * Centered and capitalized the main action button text to read `"Login"`.

### Q29. How did you implement the "pink glow" focus effect on the email and password inputs?
* **Answer:** We created a CSS class `.pink-glow-input` in `index.css` and added it to the inputs. In CSS, we define:
  * Default style: A soft pink border and ambient pink box-shadow.
  * Focus state (`:focus`): A vibrant pink border (`#ec4899`) and intense pink glow using CSS `box-shadow`:
    `box-shadow: 0 0 15px rgba(236, 72, 153, 0.4), 0 0 0 3px rgba(236, 72, 153, 0.15) !important;`
  * Cleared the conflicting inline background/border properties on the password input in `Login.jsx` so the class styles both inputs identically.

### Q30. Why did the "Last Seen" badge show "NEVER" for some users, and how did you resolve it?
* **Answer:** Users who had newly registered or were created through seed scripts did not have any login logs in the `login_log` table, so `audit.length` was `0`, triggering the fallback text `LAST SEEN: NEVER`. It looked unpolished. We resolved it in `UserProfile.jsx` by wrapping the badge in a conditional render `{audit.length > 0 && (...)}` so the badge is completely hidden for users with no login history.

### Q31. How does React handle route protection in your application?
* **Answer:** We use an `AuthContext` to store the active user state. In `App.jsx`, we wrap protected routes (like `/dashboard`, `/users`, `/roles`) in a guard component. If the user state is null, the guard component redirects them to `/login`.

---

## 📌 Section 7: Testing, Deployment & Code Quality

### Q32. What tools did you use to test your API endpoints?
* **Answer:** We used:
  * **FastAPI Auto Swagger UI** (`/docs`): To interactively test routes.
  * **Pytest**: To run automated backend unit tests (e.g. testing token expiry, rate-limiting, and registration).
  * **PostgreSQL pgAdmin / psql Client**: To verify database records.

### Q33. What linting and code quality standards did you maintain in the backend?
* **Answer:** We maintained PEP 8 standards using **`Ruff`** for fast linting and **`Black`** for automated code formatting, ensuring clean and maintainable Python code.

### Q34. How did you handle environment variables?
* **Answer:** We used a `.env` file containing variables like `DATABASE_URL`, `JWT_SECRET`, and API endpoint URLs. We loaded these in backend using `python-dotenv` and in React using `import.meta.env`, keeping configuration separate from source code (12-Factor App methodology).

---

## 📌 Section 8: Team Roles, Contributions & Project Management

### Q35. What was Sai's contribution to the project?
* **Answer:** Sai focused on core backend and database engineering. He built the FastAPI routing controllers for login and registration, configured security middleware including `Slowapi` rate-limiting, and designed database schemas for users.

### Q36. What was Varad's contribution to the project?
* **Answer:** Varad acted as the full-stack lead. He designed the RBAC permissions catalog check, generated JWT payloads, resolved package vulnerabilities, and developed the Admin portal interface (active sessions, dashboard charts, role assign modals, and UML/ERD documentation).

### Q37. What was Swaraj's contribution to the project?
* **Answer:** Swaraj led requirement gathering (interviewing faculty/students), document preparation, and inter-team coordination to synchronize JWT secrets with other module teams. He also worked on the frontend, building the student portal login/signup forms, password visibility toggles, and fixing card grid rendering.

### Q38. How does the system handle database migrations?
* **Answer:** We use SQLAlchemy's declarative base. During startup, the engine calls `Base.metadata.create_all(bind=engine)` to automatically generate missing tables. For seed data, we run custom SQL files or Python seed scripts (like `create_test_users.py`).

### Q39. What is the future scope of this project?
* **Answer:** 
  * Implementing Multi-Factor Authentication (MFA) via email/mobile OTP.
  * Implementing a Refresh Token rotation scheme to keep users logged in securely without manual re-login.
  * Hosting the entire ERP platform on cloud services (AWS/Azure) with automated database backups.
  * Integrating Auth with all remaining college ERP modules (Hostel, Transport, Library, Placement).

### Q40. Why does your database schema separate `roles` and `permissions`?
* **Answer:** By separating them, the system becomes highly scalable. If the college introduces a new job title (e.g. "Department Librarian"), we only need to add that role to the `roles` table and map it to existing permissions in the `role_permissions` table, without changing any backend code or database schemas.

---
"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Generated viva prep guide at {filepath}")

if __name__ == "__main__":
    generate_guide()
