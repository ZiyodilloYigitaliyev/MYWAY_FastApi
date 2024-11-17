# app/main.py
from fastapi import FastAPI
from ..routers import auth, affidavits, departments
from .database import engine, Base
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()
# CORS middleware sozlamalari
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Bu yerda barcha domenlarga ruxsat beriladi ("*" hamma uchun)
    allow_credentials=True,
    allow_methods=["*"],  # Barcha methodlarga (GET, POST, va h.k.) ruxsat beriladi
    allow_headers=["*"],  # Barcha headerslarga ruxsat beriladi
)



app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(affidavits.router)
app.include_router(departments.router)