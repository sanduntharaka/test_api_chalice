from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SubscriptionPlan(BaseModel):
    id: int
    created_at: datetime
    program_name: str
    active: bool
    description: str
    amount: float


class CreateSubscriptionCard(BaseModel):
    program_id: int
    datetime: datetime


class UpdateSubscriptionCard(BaseModel):
    status: str
