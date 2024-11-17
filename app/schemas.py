# app/schemas.py
from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class RestoreLicenseBase(BaseModel):
    fName: str
    licenseNumber: int
    startDate: date
    endDate: date
    phoneNum: str   

class RestoreLicenseCreate(RestoreLicenseBase):
    user_id: int

class RestoreLicense(RestoreLicenseBase):
    id: int

    class Config:
        orm_mode = True

# Affidavit uchun Pydantic model
class AffidavitBase(BaseModel):
    fName: str
    guvoxnomaNum: int
    startDate: date
    endDate: date
    lifeTime: str
    givenName: str
    pasSeria: str | None = None
    pasNum: int | None = None
    guvoxnoma2Num: int

class AffidavitCreate(AffidavitBase):
    user_id: int

class AffidavitResponse(AffidavitBase):
    id: int

    class Config:
        orm_mode = True

# Department uchun Pydantic model
class DepartmentBase(BaseModel):
    fName: str
    departmentName: str
    departmentHead: str
    email: EmailStr
    phoneNum: str

class DepartmentCreate(DepartmentBase):
    user_id: int

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        orm_mode = True

