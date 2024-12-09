from pydantic import BaseModel
from typing import Union


class AddPaymentModel(BaseModel):
    amount: float
    date_time: str
    type: str
    program_id: Union[str, None]
