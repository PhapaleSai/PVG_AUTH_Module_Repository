import sys
import os

# Append backend directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from database import SessionLocal
import models
from auth import get_password_hash

def reset_faculty():
    db = SessionLocal()
    try:
        emails = ['teacher@pvg.edu', 'teaching_staff@pvg.edu', 'teacher@gmail.com']
        users = db.query(models.User).filter(models.User.email.in_(emails)).all()
        
        print("--- Resetting Faculty/Teacher Test Accounts ---")
        for u in users:
            u.password_hash = get_password_hash("password123")
            # Get roles list
            roles = [ur.role.role_name for ur in db.query(models.UserRole).filter(models.UserRole.user_id == u.user_id).all() if ur.role is not None]
            print(f"User: {u.email} | Roles: {roles} | Password set to: password123")
        
        db.commit()
        print("--- Reset Complete ---")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    reset_faculty()
