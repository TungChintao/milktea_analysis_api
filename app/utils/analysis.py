import pandas as pd
from app.models import Shop, Good



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


# 获取35个城市的前五十品牌及其店铺数量
def get_top_fifty_brands_and_shopnum():
    brands_list = []
    # 获取数据库中该城市的所有品牌的元组
    shops = Shop.query.filter_by(isMain=1)
    for shop in shops:
        get_title = shop.title
        if get_title not in brands_list:
            brands_list.append(get_title)
    num_list = []
    for brand in brands_list:
        num = Shop.query.filter_by(title=brand, isMain=1).count()
        num_list.append(num)
    a = dict(zip(brands_list, num_list))
    a = sorted(a.items(), key=lambda x: x[1], reverse=True)
    result = []
    for n in range(50):
        result.append(a[n])
    return result


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
    result ={
        'brands': brand_list
    }
    return result

