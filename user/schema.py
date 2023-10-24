from pydantic import BaseModel, EmailStr
from typing import Optional, List
#from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType

class userInfo(BaseModel):
    fullName: str
    userName: str
    email: EmailStr
    country: str
    password: str
    class Config():
        orm_mode = True

class showUserInfo(BaseModel):
    fullName: str
    email: EmailStr
    country: str
    total_score: Optional[int]
    class Config():
        orm_mode = True

class updateUserInfo(BaseModel):
    fullName: Optional[str]
    userName: Optional[str]
    email: Optional[EmailStr]
    country: Optional[str]
    password: Optional[str]
    class Config():
        orm_mode = True



class otp(BaseModel):
    userid: int
    OTP: int
    class Config():
        orm_mode = True

class updateOtp(BaseModel):
    userid: Optional[int]
    OTP: Optional[int]
    class Config():
        orm_mode = True

class login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

