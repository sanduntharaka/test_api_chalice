from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List


class Order(BaseModel):
    odoo_order_id: int = Field(...,
                               description="Unique ID of the order in Odoo")
    order_amount: Decimal = Field(..., gt=0, description="Total order amount")


class OrderProduct(BaseModel):
    odoo_product_id: int = Field(...,
                                 description="Unique ID of the product in Odoo")
    product_name: str = Field(..., description="Name of the product")
    product_description: str = Field(...,
                                     description="Description of the product")
    product_price: Decimal = Field(..., ge=0,
                                   description="Price of the product")
    qty: int = Field(..., ge=1, description="Quantity of the product")
    free_qty: int = Field(..., ge=0,
                          description="Free quantity of the product")


class OrderRequest(BaseModel):
    order: Order
    order_products: List[OrderProduct]
