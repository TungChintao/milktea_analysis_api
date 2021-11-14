# app/models/good.py
from app.models.base import Base
from app.libs.extensions import db


class Good(Base):
    """
    奶茶商品数据表模型类
    """
    __tablename__ = 'milktea_good'
    shopid = db.Column(db.String(20), db.ForeignKey('milktea_shop.shopid'), primary_key=True)
    good = db.Column(db.String(200), primary_key=True)
    price = db.Column(db.Float)
    value = db.Column(db.Float)
