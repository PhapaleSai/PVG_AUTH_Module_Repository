# PVG College Auth & Enterprise Management System 🎓

A professional-grade, unified authentication, authorization, and administrative suite built for **PVG College of Science**.

**Technology Stack:** React (Vite) · FastAPI · PostgreSQL · SQLAlchemy · Glassmorphism UI

---

## 🚀 Step 1: Clone the Repository

To get started, clone this repository to your local machine:

```bash
# Clone the repository
git clone https://github.com/PhapaleSai/PVG_AUTH_Module_Repository.git

# Navigate into the project folder
cd PVG_AUTH_Module_Repository
```

---

## 🗄️ Step 2: Database Setup (PostgreSQL)

The system requires **PostgreSQL**. Ensure it is installed and the `psql` command is available in your system's PATH. 

### **Creating and Seeding the Database**
To avoid manual table creation, we provide a full database dump (`database_scripts/pvg_auth_full_dump.sql`) containing the complete schema and seed data (modules, roles, users, students).

### **Method 1: Using Command Line (psql)**
1. Open your command prompt/terminal and log into PostgreSQL:
   ```bash
   psql -U postgres
   ```
2. Create the database:
   ```sql
   CREATE DATABASE pvg_auth;
   ```
3. Exit the `psql` prompt:
   ```sql
   \q
   ```
4. **Import the full database dump:** 
   From the root of the `pvg-auth` folder, run:
   ```bash
   psql -U postgres -d pvg_auth -f database_scripts/pvg_auth_full_dump.sql
   ```

### **Method 2: Using pgAdmin (GUI)**
1. Open pgAdmin and connect to your local PostgreSQL server.
2. Right-click on **Databases** -> **Create** -> **Database...**
3. Name it `pvg_auth` and click **Save**.
4. Right-click on the newly created `pvg_auth` database and select **Restore...**
5. In the **Filename** field, click the folder icon and select `pvg_auth_full_dump.sql` from the `database_scripts` folder inside the project.
6. Click **Restore**.

---

## ⚙️ Step 3: Environment Configuration

Before starting the server, you must configure your backend environment variables.

1. Navigate to the `backend/` folder.
2. Create a new file named `.env`.
3. Paste the following configuration into the `.env` file:

```env
# Replace YOUR_PASSWORD with your actual postgres password!
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/pvg_auth

# JWT Secret - Keep this identical across all ERP modules (SIS, Placement, etc.)
JWT_SECRET=6950526b1649fdd3c7e15d430812376a2c775156cc9510cefd8c4dc9e9d69e5a
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 🚀 Step 4: Starting the Project

You can start the project using the automatic Master Script, or run the components manually.

### **Option A: The Automatic Master Script (Recommended)**
The fastest way to launch the entire ecosystem is to use the provided master startup script. This script automatically frees up required ports (`8000` and `5173`), activates virtual environments, and opens separate windows for Backend, Frontend, and Ngrok.

From the root directory, open **PowerShell** and run:
```powershell
.\start_all.ps1
```

### **Option B: Manual Startup**
If you prefer to run services individually, use the following commands from the root directory:

**1. Start the Python Backend**
```powershell
cd backend
# Create a virtual environment (only needed the first time)
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt

# Start the FastAPI development server
python -m uvicorn main:app --reload --port 8000
```

**2. Start the React Frontends**
```powershell
# In a new terminal window at the root directory:
npm install

# Start the frontend dev servers (Admin on port 5173, User on port 5175)
npm run dev:frontend
```

**3. Start Ngrok Tunnels**
```powershell
# In a new terminal window at the root directory:
# This launches the local ngrok executable with the configured dual-tunnel settings
.\ngrok_bin\ngrok.exe start --all --config=ngrok_dual.yml
```

---

## 📄 IMP Documents

The project also contains an `IMP_Documents_Created_for_ERP_Auth` folder which includes system designs, architectural diagrams, PDF reports, and PowerPoint presentations outlining the secure authentication workflow and Role-Based Access Control logic used in this ERP module. 

## 🧠 AI and Developer Deep-Dive

For a complete breakdown of code-level function flows, JIT user migrations, token refresh mechanisms, and the future development roadmap, please refer directly to the **AI and Developer Context Guide**:

👉 **[AI_CONTEXT.md](./AI_CONTEXT.md)**
