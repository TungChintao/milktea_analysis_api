import pandas as pd
from app.models import Shop


def city_shop_num(city):
    shop_num = Shop.query.filter_by(city=city, isMain=True).count()
    return {'city': city, 'shopnum': shop_num}


def brand_shop_num(brand):
    pass


def cities_shop_num():
    resp_data = []
    query_data = Shop.query.group_by(Shop.city)
    for d in query_data:
        city = d.city
        resp_data.append(city_shop_num(city))
    resp_data = sorted(resp_data, key=lambda data: data["shopnum"], reverse=True)
    return resp_data


def brands_shop_num():
    resp_data = []
    pass



