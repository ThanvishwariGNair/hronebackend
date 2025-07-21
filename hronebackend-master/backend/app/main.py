from fastapi import FastAPI
from app.routes import products, orders

app = FastAPI()

@app.get("/")
async def read_home():
    return {"Routes Available": [products.router.prefix, orders.router.prefix]}

app.include_router(products.router)
app.include_router(orders.router)
