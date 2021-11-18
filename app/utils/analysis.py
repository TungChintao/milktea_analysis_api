
from sqlalchemy import func, desc, distinct
from app.models import Shop, Good
from app.libs.extensions import db


def brand_shop_num(brand):
    pass


def cities_shop_num():
    resp_data = []
    query_data = db.session.query(Shop.city, func.count(Shop.shopid)).filter(Shop.isMain == 1).group_by("city").all()
    for data in query_data:
        resp_data.append({'city': data[0], 'shopnum': data[1]})
    resp_data = sorted(resp_data, key=lambda data: data["shopnum"], reverse=True)
    return resp_data


def brands_shop_num():
    resp_data = []
    pass


# 获取35个城市的前五十品牌及其店铺数量
def get_top_brands():
    query_data = db.session.query(Shop.title, func.count(Shop.title)).filter(Shop.isMain == 1).group_by("title").all()
    resp_data = []
    for data in query_data:
        resp_data.append({
            'title': data[0],
            'num': data[1]
        })
    resp_data = sorted(resp_data, key=lambda data: data['num'], reverse=True)
    return resp_data[0:50]


# 获取35个城市前50品牌及其所有产品价格
def get_top_brands_goods():
    top_brands = get_top_brands()
    resp_data = []
    for brand in top_brands:
        good_list = []
        title = brand['title']
        query_data = db.session.query(distinct(Good.good), Good.price).filter(Shop.shopid == Good.shopid,
                                                                              Shop.isMain == 1,
                                                                              Shop.record == 1,
                                                                              Shop.title == title).all()
        for data in query_data:
            good_list.append({
                'good': data[0],
                'price': data[1],
            })
        resp_data.append({
            'title': title,
            'goods': good_list
        })
    resp_data = {
        'brands': resp_data
    }
    return resp_data
