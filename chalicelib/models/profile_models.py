from pydantic import BaseModel
from typing import Union


class ProfileRequestData(BaseModel):
    first_name: str
    last_name: str
    phone: str
    dob: str


class ProfileServiceModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    dob: str
    user_id: str


class ProfileUpdateRequestData(BaseModel):
    first_name: Union[str, None]
    last_name: Union[str, None]
    phone: Union[str, None]
    dob: Union[str, None]


# class Profile(BaseModel):
#     id: str
#     first_name: str
#     last_name: str
#     email: str
#     phone: str
#     dob: str
#     user_id: str


# class SubscriptionCard(BaseModel):
#     id: str
#     user_id: str
#     status: str
#     valid_to: str
#     created_at: str
#     program_id: int
#     total_amount: float


# class ProfileResponseData(BaseModel):
#     profile: Profile
#     subscription_card: SubscriptionCard
