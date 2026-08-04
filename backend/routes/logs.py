from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
from auth import oauth2_scheme
from database import get_db

router = APIRouter(prefix="/logs", tags=["Logs"])


@router.get("", response_model=list[schemas.LoginLogOut])
def get_logs(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """Get Logs"""
    return (
        db.query(models.LoginLog)
        .order_by(models.LoginLog.login_time.desc())
        .limit(100)
        .all()
    )
