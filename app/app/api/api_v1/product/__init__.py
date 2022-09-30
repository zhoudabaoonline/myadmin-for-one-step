from fastapi import APIRouter
from app.api.api_v1.product import product
from app.api.api_v1.product import procate

router = APIRouter()
router.include_router(product.router, prefix="/product/product", tags=["product"])
router.include_router(procate.router, prefix="/product/procate", tags=["procate"])
