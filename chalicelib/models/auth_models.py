from pydantic import BaseModel, EmailStr
from typing import Union


class SignUpRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class AuthTokens(BaseModel):
    access_token: str
    refresh_token: Union[str, None]


class UserMetadata(BaseModel):
    user_id: str
    provider: str
    email: EmailStr


class GetUserResponse(BaseModel):
    detail: str
    data: UserMetadata
