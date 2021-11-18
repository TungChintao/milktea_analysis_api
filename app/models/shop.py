from app.models.base import Base
from app.libs.extensions import db


class Shop(Base):
    """
    奶茶店铺数据表模型类
    """
    __tablename__ = 'milktea_shop'
    shopid = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(35), nullable=False)
    avgprice = db.Column(db.Float)
    avgscore = db.Column(db.Float)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    comments = db.Column(db.Integer)
    city = db.Column(db.String(20), nullable=False)
    isMain = db.Column(db.Boolean)
    address = db.Column(db.String(45))
    record = db.Column(db.Boolean)
    goods = db.relationship(
        'Good', cascade='all, delete-orphan'
    )


