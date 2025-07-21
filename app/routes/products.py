from fastapi import APIRouter, Query, status
from app import crud, models

router = APIRouter(prefix="/products", tags=["products"])

# 
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: models.Product):
    pid = await crud.create_product(product.model_dump())
    return {"id": pid}

@router.get("/", status_code=status.HTTP_200_OK)
async def list_products(
    name: str = Query(None, description="Search by name, regex allowed"),
    size: str = Query(None, description="Filter by size"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    products = await crud.get_products(name, size, limit, offset)
    next_offset = offset + limit
    return {
        "products": products,
        "page": {
            "next": next_offset,
            "limit": limit,
            "previous": offset if offset > 0 else None,
        }
    }
