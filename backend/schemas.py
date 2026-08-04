from datetime import datetime

from pydantic import BaseModel, EmailStr

# ── Auth ────────────────────────────────────────────────────────────────────


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str
    role: str
    user_id: int
    username: str
    full_name: str | None = None
    permissions: list[str] = []
    created_at: datetime | None = None
    updated_at: datetime | None = None


class LogoutResponse(BaseModel):
    message: str


class TokenRefreshRequest(BaseModel):
    refresh_token: str


# ── System ──────────────────────────────────────────────────────────────────


class ModuleCreate(BaseModel):
    module_name: str
    description: str | None = None


class ModuleOut(BaseModel):
    module_id: int
    module_name: str
    description: str | None = None

    class Config:
        from_attributes = True


class FeatureCreate(BaseModel):
    feature_name: str
    description: str | None = None
    module_id: int


class FeatureOut(BaseModel):
    feature_id: int
    feature_name: str
    description: str | None = None
    module_id: int | None = None

    class Config:
        from_attributes = True


class PermissionCreate(BaseModel):
    permission_name: str
    action: str
    feature_id: int


class PermissionOut(BaseModel):
    permission_id: int
    permission_name: str
    action: str | None = None
    feature_id: int | None = None

    class Config:
        from_attributes = True


class RolePermissionOut(BaseModel):
    role_permission_id: int
    role_id: int
    permission_id: int

    class Config:
        from_attributes = True


class LoginLogOut(BaseModel):
    login_log_id: int
    user_id: int | None = None
    ip_address: str | None = None
    device_info: str | None = None
    status: str | None = None
    login_time: datetime | None = None

    class Config:
        from_attributes = True


# ── Roles ───────────────────────────────────────────────────────────────────


class RoleOut(BaseModel):
    role_id: int
    role_name: str

    class Config:
        from_attributes = True


class AssignRoleRequest(BaseModel):
    user_id: int
    role: str


class AssignRoleResponse(BaseModel):
    message: str


# ── Users ───────────────────────────────────────────────────────────────────


class UserCreate(BaseModel):
    username: str | None = None
    full_name: str | None = None
    email: EmailStr
    password: str
    department: str | None = None
    phone_number: str | None = None


class UserOut(BaseModel):
    user_id: int
    username: str
    full_name: str | None = None
    email: str
    department: str | None = None
    phone_number: str | None = None
    role: str | None = None
    permissions: list[str] = []
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


# ── Legacy schemas (kept for backward compatibility) ─────────────────────────


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    username: str | None = None
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class StudentOut(BaseModel):
    id: int
    name: str
    email: str | None = None
    phone: str
    username: str

    class Config:
        from_attributes = True
