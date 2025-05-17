from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Dict, Optional
from uuid import uuid4

app = FastAPI(title="IAM Service")

# Mô hình dữ liệu (có thể thay bằng database sau)
users = {}
roles = {}
permissions = {}

# Pydantic models
class Permission(BaseModel):
    id: str 
    name: str
    description: Optional[str] = None

class Role(BaseModel):
    id: str
    name: str
    permissions: List[str] = []

class User(BaseModel):
    id: str
    username: str
    roles: List[str] = []

class UserCreate(BaseModel):
    username: str

class RoleCreate(BaseModel):
    name: str

class PermissionCreate(BaseModel):
    name: str
    description: Optional[str] = None

# --- Permission endpoints ---
@app.post("/permissions/", status_code=status.HTTP_201_CREATED)
def create_permission(p: PermissionCreate):
    permission_id = str(uuid4())
    permissions[permission_id] = Permission(id=permission_id, **p.dict())
    return permissions[permission_id]

@app.get("/permissions/", response_model=List[Permission])
def list_permissions():
    return list(permissions.values())

# --- Role endpoints ---
@app.post("/roles/", status_code=status.HTTP_201_CREATED)
def create_role(r: RoleCreate):
    role_id = str(uuid4())
    roles[role_id] = Role(id=role_id, name=r.name, permissions=[])
    return roles[role_id]

@app.post("/roles/{role_id}/permissions/{permission_id}", status_code=status.HTTP_204_NO_CONTENT)
def add_permission_to_role(role_id: str, permission_id: str):
    if role_id not in roles:
        raise HTTPException(status_code=404, detail="Role not found")
    if permission_id not in permissions:
        raise HTTPException(status_code=404, detail="Permission not found")
    if permission_id not in roles[role_id].permissions:
        roles[role_id].permissions.append(permission_id)
    return

@app.get("/roles/", response_model=List[Role])
def list_roles():
    return list(roles.values())

# --- User endpoints ---
@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(u: UserCreate):
    user_id = str(uuid4())
    users[user_id] = User(id=user_id, username=u.username, roles=[])
    return users[user_id]

@app.post("/users/{user_id}/roles/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def add_role_to_user(user_id: str, role_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    if role_id not in roles:
        raise HTTPException(status_code=404, detail="Role not found")
    if role_id not in users[user_id].roles:
        users[user_id].roles.append(role_id)
    return

@app.get("/users/", response_model=List[User])
def list_users():
    return list(users.values())

# --- Check permission for a user ---
@app.get("/users/{user_id}/permissions/", response_model=List[Permission])
def get_user_permissions(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    user_roles = users[user_id].roles
    user_permissions = set()
    for role_id in user_roles:
        role = roles.get(role_id)
        if role:
            for perm_id in role.permissions:
                user_permissions.add(perm_id)
    return [permissions[pid] for pid in user_permissions]
