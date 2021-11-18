from app.models import Shop
from sqlalchemy import distinct, func
from app.libs.extensions import db


# 获取35个城市列表
def get_cities_list():
    city_list = []
    results = db.session.query(distinct(Shop.city)).all()
    for i in results:
        city_list.append(i[0])
    return city_list


# 表一  获取城市地图中店铺散点图信息
def shop_details(city_name):
    json_list = []
    shops = Shop.query.filter(Shop.city == city_name, Shop.isMain == 1, Shop.avgprice > 0)
    for shop in shops:
        get_title = shop.title
        get_latitude = shop.latitude
        get_longitude = shop.longitude
        get_avgprice = "%.2f" % shop.avgprice
        get_address = shop.address
        shop1 = {
            'title': get_title,
            'latitude': get_latitude,
            'longitude': get_longitude,
            'avgprice': get_avgprice,
            'address': get_address
        }
        json_list.append(shop1)
    return json_list


# 表二  获取该城市前50品牌的名称，店铺数量，店铺数量在全国的占比
def get_city_brands_top50(city_name):
    query_data_city = db.session.query(Shop.title, func.count(Shop.title)).filter(Shop.isMain == 1,
                                                                                  Shop.city == city_name).group_by(
        'title').all()
    resp_data = []
    for data in query_data_city:
        all_num = db.session.query(func.count(Shop.title)).filter(Shop.isMain == 1,
                                                                  Shop.title == data[0]).group_by('title').first()
        percentage = data[1] / all_num[0]
        percentage = "%.2f" % percentage
        resp_data.append({
            'title': data[0],
            'num_and_percentage': {
                'num': data[1],
                'percentage': percentage
            }
        })
        resp_data = sorted(resp_data, key=lambda data: data['num_and_percentage']['num'], reverse=True)
    return resp_data[0:50]


# 表三  获取该城市前五品牌在该城市各地区店铺分布情况
def get_brands_top5_address(city_name):
    top50 = get_city_brands_top50(city_name)
    top5 = top50[0:5]
    resp_data = []
    addresses = db.session.query(distinct(Shop.address)).filter(Shop.city == city_name, Shop.isMain == 1).all()
    for address in addresses:
        shops_list = []
        for brand in top5:
            query_data = db.session.query(func.count(Shop.title)).filter(Shop.city == city_name, Shop.isMain == 1,
                                                                         Shop.title == brand['title'],
                                                                         Shop.address == address[0]).group_by(
                'title').all()
            if query_data:
                for data in query_data:
                    shops_list.append({
                        'shopnum': data[0],
                        'title': brand['title']
                    })
            else:
                shops_list.append({
                    'shopnum': 0,
                    'title': brand['title']
                })
        resp_data.append({
            'address': address[0],
            'shops': shops_list
        })
    return resp_data
