import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from sqlalchemy import create_mock_engine
from backend.models import Base

output_lines = []

def dump(sql, *multiparams, **params):
    # Compile SQL to string
    sql_str = str(sql.compile(dialect=mock_engine.dialect))
    # Replace the single line statement with a formatted one ending in semicolon
    output_lines.append(sql_str.strip() + ";\n")

mock_engine = create_mock_engine('postgresql://', dump)

# Drop tables is handled by export_full_db.py, we just need Create
Base.metadata.create_all(mock_engine, checkfirst=False)

output_file = os.path.join(os.path.dirname(__file__), "database_scripts", "setup_auth_tables.sql")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("-- ============================================================\n")
    f.write("--  AUTH TABLE DDL (Generated from SQLAlchemy Models)\n")
    f.write("-- ============================================================\n\n")
    for line in output_lines:
        f.write(line + "\n")

print(f"Successfully updated {output_file}")
