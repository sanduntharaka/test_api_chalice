from pydantic import BaseModel


class ProfileRequestData(BaseModel):
    first_name: str
    last_name: str
    phone: str
    dob: str


class Profile(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    dob: str
    user_id: str


class SubscriptionCard(BaseModel):
    id: str
    user_id: str
    status: str
    valid_to: str
    created_at: str
    program_id: int
    total_amount: float


class ProfileResponseData(BaseModel):
    profile: Profile
    subscription_card: SubscriptionCard
