# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)


class RestoreLicense(Base):
    __tablename__ = "restore_licenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # "users" jadvalining asosiy kaliti
    fName = Column(String(150), nullable=False)
    licenseNumber = Column(Integer, nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    phoneNum = Column(String(13), nullable=False)

    user = relationship("User", back_populates="licenses")  # Agar `User` jadvalingiz bo'lsa, bog'lash uchun

    def __repr__(self):
        return f"<RestoreLicense(fName={self.fName}, licenseNumber={self.licenseNumber})>"

class Affidavit(Base):
    __tablename__ = "affidavits"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    fName = Column(String(150), nullable=False)
    guvoxnomaNum = Column(Integer, nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    lifeTime = Column(String(150), nullable=False)
    givenName = Column(String(150), nullable=False)
    pasSeria = Column(String(2), nullable=True)  # blank=True Django'dagi ekvivalenti nullable=True
    pasNum = Column(Integer, nullable=True)
    guvoxnoma2Num = Column(Integer, nullable=False)

    user = relationship("User", back_populates="affidavits")  # Agar `User` jadvali mavjud bo'lsa

    def __repr__(self):
        return f"<Affidavit(fName={self.fName}, guvoxnomaNum={self.guvoxnomaNum})>"

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    fName = Column(String(150), nullable=False)
    departmentName = Column(String(150), nullable=False)
    departmentHead = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True, index=True)
    phoneNum = Column(String(13), nullable=False)

    user = relationship("User", back_populates="departments")  # Agar `User` jadvali mavjud bo'lsa

    def __repr__(self):
        return f"<Department(fName={self.fName}, departmentName={self.departmentName})>"

