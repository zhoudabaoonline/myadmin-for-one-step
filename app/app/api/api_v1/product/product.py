from typing import Any, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.api import deps
from app.extensions.utils import list_to_tree

router = APIRouter()


@router.get("/list", response_model=schemas.Response)
def get_products(*,
                 db: Session = Depends(deps.get_db),
                 limit: int,
                 page: int,
                 name: Optional[str] = None,) -> Any:
    """用户管理-查询"""
    query = db.query(models.Product)
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


@router.get("/{id}", response_model=schemas.Response)
def getProduct(id: int, db: Session = Depends(deps.get_db), ) -> Any:
    """Get a specific menu by id."""
    menu = db.query(models.Product).filter(models.Product.id == id).one()
    return {"code": 20000, "data": menu, }


@router.put("/", response_model=schemas.Response)
def update_product(*, db: Session = Depends(deps.get_db), product_in: schemas.ProductUpdate) -> Any:
    """update a specific menu by id."""
    id = product_in.id
    product_in = product_in.dict()
    db.query(models.Product).filter(
        models.Product.id == id).update(product_in)
    db.commit()
    return {"code": 20000, "data": "", "message": "修改成功", }


@router.delete("/{id}", response_model=schemas.Response)
def delete_product_id(id: int, db: Session = Depends(deps.get_db), ) -> Any:
    """Delete a specific menu by id."""
    db.query(models.Product).filter(models.Product.id == id).delete()
    db.commit()
    return {"code": 20000, "data": "", "message": f"删除成功"}


@router.post("/", response_model=schemas.Response)
def post_product(*, db: Session = Depends(deps.get_db), product: schemas.ProductCreate, ) -> Any:
    """Add a specific menu"""
    db.add(models.Product(**product.dict()))
    db.commit()
    return {"code": 20000, "data": "", "message": "新增菜单成功"}
