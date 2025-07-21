from pydantic import BaseModel, Field
from typing import Optional, List

class Product(BaseModel):
    name: str
    description: str
    price: float
    size: Optional[str] = None

class ProductInDB(Product):
    id: str = Field(..., alias="_id")

class OrderProductItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    user_id: str
    products: List[OrderProductItem]
    total_price: float

class OrderInDB(Order):
    id: str = Field(..., alias="_id")
