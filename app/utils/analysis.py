import pandas as pd
from sqlalchemy import func, desc
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
    query_data = db.session.query(Shop.title, func.count(Shop.title)).filter(Shop.isMain == 1).group_by(
        "title").limit().all()
    resp_data = []
    for data in query_data:
        resp_data.append({
            'title': data[0],
            'num': data[1]
        })
    resp_data = sorted(resp_data, key=lambda data: data['num'], reverse=True)
    return resp_data


# 获取35个城市前50品牌及其所有产品价格
def get_top_fifty_brands_and_goods():
    a = get_top_fifty_brands_and_shopnum()
    id_list = []
    for i in a:
        shop = Shop.query.filter_by(title=i[0], isMain=1, record=1).first()
        id_list.append(shop.shopid)
    brand_list = []
    for i in range(50):
        good_list = []
        goods = Good.query.filter_by(shopid=id_list[i])
        for g in goods:
            good = g.good
            price = g.price
            good_dict = {
                'good': good,
                'price': "%.2f" % price
            }
            good_list.append(good_dict)
        brand_dict = {
            'title': a[i][0],
            'goods': good_list
        }
        brand_list.append(brand_dict)
    result = {
        'brands': brand_list
    }
    return result
