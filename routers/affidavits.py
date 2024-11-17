from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Affidavit
from app.schemas import AffidavitCreate, AffidavitResponse

router = APIRouter(prefix="/api/affidavits", tags=["Affidavits"])

# GET: Barcha affidavitlarni olish
@router.get("/", response_model=list[AffidavitResponse])
async def get_affidavits(db: Session = Depends(get_db)):
    affidavits = db.query(Affidavit).all()
    return affidavits

# POST: Yangi affidavit qo'shish
@router.post("/", response_model=AffidavitResponse, status_code=status.HTTP_201_CREATED)
async def create_affidavit(affidavit: AffidavitCreate, db: Session = Depends(get_db)):
    new_affidavit = Affidavit(**affidavit.dict())
    db.add(new_affidavit)
    db.commit()
    db.refresh(new_affidavit)
    return new_affidavit
