from pydantic import BaseModel


class UserModelForSupabase(BaseModel):
    user_id: str
