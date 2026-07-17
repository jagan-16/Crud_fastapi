from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Product(BaseModel):
        name:str
        original_price_per_unit :float
        quantity:float
        quantity_unit:str 
        discount_percentage_per_unit : int 
        
class productResponse(BaseModel):
        product_id : int 
        product_name : str
        quantity : float
        quantity_unit: str 
        original_price_per_unit: float
        currency: str
        discounted_percentage_per_unit: float
        discounted_price_per_unit: float
        
        

class Customer(BaseModel):
        name: str
        mobile_number: str
        email: str
        address: str
        
class customerResponse(BaseModel):
        customer_id: int
        customer_name : str
        mobile_number: str
        email: str
        address: str
        created_at: datetime
        updated_at : datetime

class Order(BaseModel):
        customer_id: int
        item : list["OrderCreate"]
        
class orderUpdate(BaseModel):
        items: list["OrderCreate"]
        
        
class OrderCreate(BaseModel):
        product_id: int
        quantity: float 
                
        
class OrderItemResponse(BaseModel):
        product_id: int
        product_name: str
        order_item_id: int
        product_quantity: float
        product_quantity_unit: str
        
        
class OrderResponse(BaseModel):
        customer_id: int 
        order_date: datetime
        order_id: UUID
        total_price: float
        currency: str
        item: list[OrderItemResponse]
        
class SummarizeRequest(BaseModel):
        text : str 
        
class SummarizeResponse(BaseModel):
        summary : str