from typing import Optional, Any

from pydantic import BaseModel


# Shared properties
class Product(BaseModel):
    proCateId: Optional[int] = None
    area: Optional[Any] = None
    proName: str
    img: Optional[str] = None
    logo: Optional[str] = None
    link: Optional[str] = None
    content: Optional[str] = None
    logodesc: Optional[str] = None


class ProductCreate(Product):
    pass


class ProductUpdate(Product):
    id: int

# Shared properties


class ProCate(BaseModel):
    proCateName: Optional[str] = None
    desc: Optional[str] = None


class ProCateUpdate(ProCate):
    id: int


class ProCateCreate(ProCate):
    pass
