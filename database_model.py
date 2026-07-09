from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column ,Integer, Sequence , String , Float ,ForeignKey , DateTime
import uuid 
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime
from datetime import datetime

base = declarative_base()

class TimestampMixin:
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

class Product(base , TimestampMixin):
    
    __tablename__ = "products"
    
    id = Column (Integer, primary_key = True , index = True)
    name = Column (String , nullable = False)
    quantity = Column (Float , nullable = False)
    quantity_unit = Column (String , nullable = False)
    original_price_per_unit = Column (Float , nullable = False)
    discount_percentage_per_unit = Column(Float, nullable= True)
    discounted_price_per_unit = Column (Float, nullable= True )
    
    

    order_items = relationship(
        "OrderItem",
        back_populates="product"
    )

class Customer(base , TimestampMixin):
    __tablename__ = "customers"
    
    customer_id = Column (Integer ,
                         Sequence('customer_id_seq', start=1000),
                          primary_key = True , 
                          index = True,
                          )
    name = Column (String , nullable = False)
    mobile_number = Column (String , nullable = False)
    email = Column (String , nullable = False)
    address = Column (String , nullable = False)
    
    orders = relationship(
        "Order",
        back_populates="customer"
    )
    
class Order(base ,TimestampMixin):
    __tablename__ = "orders"
    
    order_id = Column (UUID(as_uuid=True),
                       primary_key=True,
                       default=uuid.uuid4,
                       index=True)
    
    customer_id = Column(Integer,
                        ForeignKey("customers.customer_id"))
    
    total_price = Column(Float , nullable= False)
    
    
    customer = relationship(
        "Customer",
        back_populates="orders"
    )
    order_items = relationship(
        "OrderItem",    
        back_populates="orders"
    )
    
    
class OrderItem(base , TimestampMixin):
    
    __tablename__ = "orderItem"
    
    order_item_id = Column(Integer,
                           Sequence('order_item_seq', start=10000),
                           primary_key=True
                           )
    
    order_id = Column (UUID(as_uuid=True),
                       ForeignKey("orders.order_id"),
                       
                       )
    product_id = Column (Integer,
                         ForeignKey("products.id"),
                        )
    
    quantity = Column(Integer , 
                      nullable=False)
    
    product = relationship(
        "Product",
        back_populates = "order_items"
    )
    
    orders = relationship(
        "Order",
        back_populates = "order_items"
    )