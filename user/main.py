import sqlite3
from fastapi import FastAPI, Depends, HTTPException,status, Query, Response, File, UploadFile, BackgroundTasks
import schema, models, database, oauth2
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from routers import authentication, user
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from minio import Minio
from minio.error import S3Error
import minio, uuid, io
import datetime
import base64
from io import BytesIO
from fastapi import BackgroundTasks


app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with the origins that should be allowed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(user.router)