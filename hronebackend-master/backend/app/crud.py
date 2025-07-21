from .database import db

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# Product CRUD
async def create_product(data: dict):
    result = await db['products'].insert_one(data)
    return str(result.inserted_id)

async def get_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size
    products = []
    cursor = db['products'].find(query).skip(offset).limit(limit)
    async for doc in cursor:
        print("Serializing product document:")
        products.append(serialize_doc(doc))
        print("Serialized product:")
    return products

# Order CRUD
async def create_order(data: dict):
    result = await db['orders'].insert_one(data)
    return str(result.inserted_id)

async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders = []
    cursor = db['orders'].find({"user_id": user_id}).skip(offset).limit(limit)
    async for doc in cursor:
        orders.append(serialize_doc(doc))
    return orders
