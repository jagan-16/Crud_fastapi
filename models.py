from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Product(BaseModel):
        name:str
        original_price:float
        quantity:int
        discount_percentage : int 
        

class Customer(BaseModel):
        name: str
        mobile_number: str
        email: str
        address: str

class Order(BaseModel):
        customer_id: int
        item : list["OrderCreate"]
        
        
class OrderCreate(BaseModel):
        product_id: int
        quantity: int 
        
        # List of dictionaries containing product_id and quantity
class orderItem(BaseModel):
        order_id: int
        product_id: int
        quantity: int
        
        
class OrderItemResponse(BaseModel):
        product_id: int
        product_name: str
        order_item_id: int
        product_quantity: int
        
        
class OrderResponse(BaseModel):
        customer_id: int 
        order_date: datetime
        order_id: UUID
        item: list[OrderItemResponse]