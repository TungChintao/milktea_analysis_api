# app/models/wordcloud.py
from app.models.base import Base
from app.libs.extensions import db


class WordCloud(Base):
    """
    奶茶商品数据表模型类
    """
    __tablename__ = 'wordcloud'
    num = db.Column(db.BIGINT, primary_key=True)
    keyword = db.Column(db.String(35))
    brand = db.Column(db.String(50))