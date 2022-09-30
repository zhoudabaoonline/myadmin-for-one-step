from typing import Text
from sqlalchemy import Column, Integer, String, ForeignKey, Date, TEXT
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    proName = Column(TEXT, doc="产品名称")
    area = Column(Integer, doc="区域")  # 从字典里面取数据
    img = Column(TEXT, doc="产品图片")
    logo = Column(TEXT, doc="产品logo")
    content = Column(TEXT, doc="产品详情")
    link = Column(TEXT, doc="产品链接")
    logodesc = Column(TEXT, doc="logo描述")

    proCateId = Column(Integer, ForeignKey(
        "procate.id", ondelete='SET NULL'), doc='分类')
    product = relationship('ProCate', backref="product")


class ProCate(Base):
    id = Column(Integer, primary_key=True, index=True)
    proCateName = Column(String(2048), doc="分类名称")
    desc = Column(TEXT, doc="备注")
