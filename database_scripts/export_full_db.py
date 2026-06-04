import os
import psycopg2
from datetime import datetime

dsn = "postgresql://postgres:sai123@localhost:5432/pvg_auth"
output_file = os.path.join(os.path.dirname(__file__), "pvg_auth_full_dump.sql")

tables = [
    "modules",
    "features",
    "permissions",
    "roles",
    "role_permissions",
    "users",
    "user_roles",
    "students",
    "user_tokens",
    "login_log"
]

def format_value(val):
    if val is None:
        return "NULL"
    if isinstance(val, bool):
        return "TRUE" if val else "FALSE"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, datetime):
        return f"'{val.isoformat()}'"
    # String or other
    val_str = str(val).replace("'", "''")  # escape single quotes
    return f"'{val_str}'"

try:
    print(f"Connecting to database to generate full dump...")
    conn = psycopg2.connect(dsn)
    cursor = conn.cursor()
    
    sql_lines = []
    sql_lines.append("-- ============================================================")
    sql_lines.append(f"--  PVG AUTH FULL DATABASE DUMP (Schema + Data)")
    sql_lines.append(f"--  Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    sql_lines.append("-- ============================================================\n")
    
    # 1. Clean up existing tables (reverse order of dependencies)
    sql_lines.append("-- 1. Drop existing tables if they exist")
    for table in reversed(tables):
        sql_lines.append(f"DROP TABLE IF EXISTS {table} CASCADE;")
    sql_lines.append("")
    
    # 2. Add table definitions (DDL)
    sql_lines.append("-- 2. Create tables")
    
    # We read from setup_auth_tables.sql to get original schema definitions
    setup_sql_path = os.path.join(os.path.dirname(__file__), "setup_auth_tables.sql")
    if os.path.exists(setup_sql_path):
        with open(setup_sql_path, "r", encoding="utf-8") as f:
            ddl_content = f.read()
            # Clean up comments and standard headers from setup_auth_tables
            sql_lines.append(ddl_content)
    else:
        print("Warning: setup_auth_tables.sql not found. Generating minimal DDL.")
        
    sql_lines.append("\n-- ============================================================")
    sql_lines.append("--  TABLE DATA INSERTS")
    sql_lines.append("-- ============================================================\n")
    
    # 3. Fetch data and generate inserts for each table
    for table in tables:
        sql_lines.append(f"-- Data for table: {table}")
        
        # Get column names
        cursor.execute(f"SELECT * FROM {table} LIMIT 0")
        colnames = [desc[0] for desc in cursor.description]
        col_list = ", ".join(colnames)
        
        # Fetch all rows
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        
        if not rows:
            sql_lines.append(f"-- No records in {table}\n")
            continue
            
        for row in rows:
            val_list = ", ".join(format_value(val) for val in row)
            sql_lines.append(f"INSERT INTO {table} ({col_list}) VALUES ({val_list});")
        sql_lines.append("")
        print(f"Exported {len(rows)} records from table '{table}'")

    # Write to output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(sql_lines))
        
    print(f"\nSuccessfully generated full database dump: {output_file}")
    conn.close()
except Exception as e:
    print(f"Error generating database dump: {e}")
