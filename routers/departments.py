from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Department
from app.schemas import DepartmentCreate, DepartmentResponse

router = APIRouter(prefix="/api/departments", tags=["Departments"])

# GET: Barcha departmentlarni olish
@router.get("/", response_model=list[DepartmentResponse])
async def get_departments(db: Session = Depends(get_db)):
    departments = db.query(Department).all()
    return departments

# POST: Yangi department qo'shish
@router.post("/", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED)
async def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    new_department = Department(**department.dict())
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department
