from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column ,Integer, Sequence , String , Float ,ForeignKey , DateTime
import uuid 
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

base = declarative_base()

class Product(base):
    
    __tablename__ = "products"
    
    id = Column (Integer, primary_key = True , index = True)
    name = Column (String , nullable = False)
    price = Column (Float , nullable = False)
    quantity = Column (Integer , nullable = False)

    order_items = relationship(
        "OrderItem",
        back_populates="product"
    )

class Customer(base):
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
    
class Order(base):
    __tablename__ = "orders"
    
    order_id = Column (UUID(as_uuid=True),
                       primary_key=True,
                       default=uuid.uuid4,
                       index=True)
    
    customer_id = Column(Integer,
                        ForeignKey("customers.customer_id"))
    
    Date = Column(DateTime , nullable=False) 
    
    customer = relationship(
        "Customer",
        back_populates="orders"
    )
    order_items = relationship(
        "OrderItem",    
        back_populates="orders"
    )
    
    
class OrderItem(base):
    
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