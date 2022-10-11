from typing import Any, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
import models
from app.api import deps
from app.extensions.utils import list_to_tree

router = APIRouter()


@router.get("/", response_model=schemas.Response)
def get_proCates(*,
                 db: Session = Depends(deps.get_db),
                 limit: int,
                 page: int,
                 name: Optional[str] = None,) -> Any:
    """产品分类-查询"""
    query = db.query(models.ProCate)
    if name:
        query = query.filter(models.ProCate.proCateName.like("%" + name + "%"))
    # 根据部门ID筛选部门及部门下级所有员工
    proCates = query.order_by(models.ProCate.id).limit(
        limit).offset((page - 1) * limit).all()

    total = query.count()

    proCate_list = []
    for proCate in proCates:
        proCate_info = proCate.dict()
        proCate_list.append(proCate_info)
    return {"code": 20000, "data": {"items": proCate_list, 'total': total}, }


@router.get("/{id}", response_model=schemas.Response)
def getProcate(id: int, db: Session = Depends(deps.get_db), ) -> Any:
    """Get a specific menu by id."""
    proCate = db.query(models.ProCate).filter(models.ProCate.id == id).one()
    return {"code": 20000, "data": proCate, }


@router.put("/", response_model=schemas.Response)
def update_procate(*, db: Session = Depends(deps.get_db), proCate: schemas.ProCateUpdate) -> Any:
    """update a specific menu by id."""
    id = proCate.id
    proCate = proCate.dict()
    db.query(models.ProCate).filter(models.ProCate.id == id).update(proCate)
    db.commit()
    return {"code": 20000, "data": "", "message": "修改成功", }


@router.delete("/{id}", response_model=schemas.Response)
def delete_procate_id(id: int, db: Session = Depends(deps.get_db), ) -> Any:
    """Delete a specific menu by id."""
    db.query(models.ProCate).filter(models.ProCate.id == id).delete()
    db.commit()
    return {"code": 20000, "data": "", "message": f"删除成功"}


@router.post("/", response_model=schemas.Response)
def post_procate(*, db: Session = Depends(deps.get_db), proCate: schemas.ProCateCreate, ) -> Any:
    """Add a specific menu"""
    db.add(models.ProCate(**proCate.dict()))
    db.commit()
    return {"code": 20000, "data": "", "message": "新增产品分类成功"}
