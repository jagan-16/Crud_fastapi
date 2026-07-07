from datetime import datetime
from fastapi import Depends , FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uuid import UUID
from models import Customer, Product, Order , OrderResponse, OrderItemResponse
from database import session, engine
import database_model
from sqlalchemy.orm import Session
from fastapi.security import APIKeyHeader
from fastapi import Security, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("api_key")

api_key_header = APIKeyHeader(
    name="x-api-key",
    auto_error=False
)

def verify_api_key(
    api_key: str = Security(api_key_header)
):
    if api_key is None:
        raise HTTPException(
            status_code=401,
            detail="API Key Missing"
        )

    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return api_key

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
     allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database_model.base.metadata.create_all(bind= engine)



products = [
    Product( name="Phone ", original_price =10.99, quantity=5 , discount_percentage = 30),
    Product( name="laptop ", original_price =19.99, quantity= 3 , discount_percentage = 30 ),
    Product( name="tablet ", original_price =5.99, quantity= 10 , discount_percentage = 30 ),
    Product( name="headphones ", original_price =2.99, quantity= 15 , discount_percentage = 30),
]

customers = [
    Customer( name="John Doe", mobile_number="1234567890", email="john.doe@example.com", address="123 Main St"),
    Customer( name="Jane Smith", mobile_number="0987654321", email="jane.smith@example.com", address="456 Oak Ave"),
]





def get_db():
    db = session()
    try :
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_model.Product).count()
    count1 = db.query(database_model.Customer).count()
    if count1 == 0:
        for customer in customers:
            db.add(database_model.Customer(**customer.model_dump()))
        db.commit()
    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))
        db.commit()

init_db()

@app.get("/products/" , tags=["Products"] , summary="Get all products" , description="Retrieve a list of all products in the database.")
def get_all_product( db: Session = Depends(get_db) ,  _: str = Depends(verify_api_key)):
    db_products = db.query(database_model.Product).all() 
    return db_products

@app.get("/product/{id}" , tags=["Products"] , summary="Get product by ID" , description="Retrieve a product by its ID.")
def get_product_by_id(id:int , db: Session = Depends(get_db) , _: str = Depends(verify_api_key)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
    return {"message": "Product not found!"}

@app.post("/products/" , tags=["Products"] , summary="Add new product" , description="Add a new product to the database.")
def add_product(product: Product, db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    product_data = product.model_dump()
    product_data["discounted_price "] = (product.original_price - (product.original_price * product.discount_percentage / 100 ))
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return {"message": "Product added successfully!"}

@app.put("/products/{id}" , tags=["Products"] , summary="Update product" , description="Update an existing product in the database.")
def update_product(id:int , product: Product, db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
       db_product.name = product.name
       db_product.original_price  = product.original_price 
       db_product.quantity = product.quantity
       db.commit()
       return {"message": "Product updated successfully!"}
    else:
        return {"message": "Product not found!"}

@app.delete("/products/{id}" , tags=["Products"] , summary="Delete product" , description="Delete a product from the database by its ID.")
def delete_product(id:int, db: Session = Depends(get_db) , _: str = Depends(verify_api_key)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully!"}
    return {"message": "Product not found!"}

@app.get("/customers/" , tags=["Customers"] , summary="Get all customers" , description="Retrieve a list of all customers in the database.")
def get_all_customers(db: Session = Depends(get_db) , _: str = Depends(verify_api_key)):
    return db.query(database_model.Customer).all()
    
@app.get("/customer/{id}" , tags=["Customers"] , summary="Get customer by ID" , description="Retrieve a customer by their ID.")
def get_customer_by_id(id:int , db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    db_customer = db.query(database_model.Customer).filter(database_model.Customer.customer_id == id).first()
    if db_customer:
        return db_customer
    return {"message": "Customer not found!"}

@app.post("/customers/" , tags=["Customers"] , summary="Add new customer" , description="Add a new customer to the database.")
def add_customer(customer: Customer, db: Session = Depends(get_db) , _: str = Depends(verify_api_key)):
    db.add(database_model.Customer(**customer.model_dump()))
    db.commit()
    return {"message": "Customer added successfully!"}

@app.post("/orders/" , tags=["Orders"] , summary="Create new order" , description="Create a new order in the database.")
def create_order(order: Order , db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    customer = db.query(database_model.Customer).filter(database_model.Customer.customer_id == order.customer_id).first()
    if customer is None:
        return {"message": "Customer not found!"}
    
    db_order = database_model.Order(customer_id = order.customer_id , created_at = datetime.utcnow())
    
    db.add(db_order)
    db.flush()
    
    for item in order.item:
        product = db.query(database_model.Product ).filter(database_model.Product.id == item.product_id).first()
        
        if product is None:
            db.rollback()
            return {"message": f"Product with id {item.product_id} not found!"}
        
        if product.quantity < item.quantity:
            db.rollback()
            return {"message": f"Insufficient quantity for product {product.name}!"}
        
        db_order_item = database_model.OrderItem(order_id = db_order.order_id , product_id = item.product_id, quantity = item.quantity)
        
        db.add(db_order_item)
        product.quantity -= item.quantity
        
    db.commit()
    return {"message": "Order created successfully!"}

@app.get("/orders/" , tags=["Orders"] , summary="Get all orders" , description="Retrieve a list of all orders in the database.")
def get_all_orders(db: Session = Depends(get_db) , _: str = Depends(verify_api_key)):
   rows = (db.query(
        database_model.Order.customer_id,
        database_model.Order.created_at,
        database_model.Order.updated_at ,
        database_model.Product.name,
        database_model.Product.id,
         database_model.Order.order_id,
        database_model.OrderItem.order_item_id,
        database_model.OrderItem.quantity
    )
    .join(
        database_model.OrderItem,
        database_model.Order.order_id == database_model.OrderItem.order_id
    )
    .join(
        database_model.Product,
        database_model.OrderItem.product_id == database_model.Product.id
    )
    .all()
)
    
   
   orders = {}

   for row in rows:

        if row.order_id not in orders:

            orders[row.order_id] = OrderResponse(
                customer_id=row.customer_id,
                order_id=row.order_id,
                order_date=row.created_at,
                item=[]
            )

        orders[row.order_id].item.append(

            OrderItemResponse(
                product_id=row.id,
                product_name=row.name,
                order_item_id=row.order_item_id,
                product_quantity=row.quantity
            )

        )

   return list(orders.values())

@app.get("/order/{id}" , tags=["Orders"])
def get_order_by_id(id: UUID, db: Session = Depends(get_db) , _: str = Depends(verify_api_key)):
        db_order = db.query( database_model.Order.customer_id,
            
            database_model.Product.name,
            database_model.Product.id ,
            database_model.Order.order_id,
            database_model.Order.created_at,
            database_model.OrderItem.order_item_id,
            database_model.OrderItem.quantity
        ).join(
            database_model.OrderItem,
            database_model.Order.order_id == database_model.OrderItem.order_id
        ).join(
            database_model.Product,
            database_model.OrderItem.product_id == database_model.Product.id
        ).filter(database_model.Order.order_id == id).all()
        if db_order:
            return OrderResponse(
                customer_id=db_order[0].customer_id,
                order_id=db_order[0].order_id,
                order_date=db_order[0].created_at,
                item = [
                    OrderItemResponse(
                        product_id = row.id,
                        product_name = row.name ,
                        order_item_id = row.order_item_id ,
                        product_quantity= row.quantity
                    )
                    for row in db_order
                ]
            )
      
        return {"message": "Order not found!"}