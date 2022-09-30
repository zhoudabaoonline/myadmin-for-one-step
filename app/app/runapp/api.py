from optparse import Option
from app.extensions.utils import list_to_tree
from app.api import deps
from app import models, schemas
from sqlalchemy.orm import Session
from typing import Any, Optional
from fastapi import APIRouter, Depends


router = APIRouter()


@router.get("/list", response_model=schemas.Response)
def get_products(*,
                 db: Session = Depends(deps.get_db),
                 limit: int,
                 page: int,
                 procate: Optional[int] = None,
                 area: Optional[int] = None,
                 name: Optional[str] = None,) -> Any:
    query = db.query(models.Product)

    if procate:
        query = query.filter(models.Product.proCateId == procate)

    if area:
        query = query.filter(models.Product.area == area)

    if name:
        query = query.filter(models.Product.proName.like("%" + name + "%"))
    # 根据部门ID筛选部门及部门下级所有员工
    products = query.order_by(models.Product.id).limit(
        limit).offset((page - 1) * limit).all()

    total = query.count()

    pro_list = []
    for product in products:
        pro_info = product.dict()
        pro_list.append(pro_info)
    return {"code": 20000, "data": {"items": pro_list, 'total': total}, }
