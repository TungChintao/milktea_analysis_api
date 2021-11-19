from sqlalchemy import func, distinct
from app.models import Shop, Good
from app.libs.extensions import db
import requests


def brand_shop_num(brand):
    pass


def generate_map(city):
    if city == '武汉':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/420100_full.json").json()
    elif city == '南京':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/320100_full.json").json()
    elif city == '深圳':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/440300_full.json").json()
    elif city == '广州':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/440100_full.json").json()
    elif city == '西安':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/610100_full.json").json()
    elif city == '石家庄':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/130100_full.json").json()
    elif city == '长春':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/220100_full.json").json()
    elif city == '北京':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/110000_full.json").json()
    elif city == '哈尔滨':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/230100_full.json").json()
    elif city == '上海':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/310000_full.json").json()
    elif city == '沈阳':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/210100_full.json").json()
    elif city == '西宁':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/630100_full.json").json()
    elif city == '银川':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/640100_full.json").json()
    elif city == '郑州':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/410100_full.json").json()
    elif city == '乌鲁木齐':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/650100_full.json").json()
    elif city == '呼和浩特':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/150100_full.json").json()
    elif city == '海口':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/460100_full.json").json()
    elif city == '贵阳':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/520100_full.json").json()
    elif city == '南昌':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/360100_full.json").json()
    elif city == '济南':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/370100_full.json").json()
    elif city == '昆明':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/530100_full.json").json()
    elif city == '兰州':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/620100_full.json").json()
    elif city == '杭州':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/330100_full.json").json()
    elif city == '合肥':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/340100_full.json").json()
    elif city == '南宁':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/450100_full.json").json()
    elif city == '长沙':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/430100_full.json").json()
    elif city == '重庆':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/500000_full.json").json()
    elif city == '太原':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/140100_full.json").json()
    elif city == '成都':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/510100_full.json").json()
    elif city == '福州':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/350100_full.json").json()
    elif city == '拉萨':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/540100_full.json").json()
    elif city == '三亚':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/460200_full.json").json()
    elif city == '厦门':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/350200_full.json").json()
    elif city == '天津':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/120000_full.json").json()
    elif city == '苏州':
        return requests.get("https://geo.datav.aliyun.com/areas_v3/bound/320500_full.json").json()


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
    query_data = db.session.query(Shop.title, func.count(Shop.title)).filter(Shop.isMain == 1).group_by("title").limit(50).all()
    resp_data = []
    for data in query_data:
        resp_data.append({
            'title': data[0],
            'num': data[1]
        })
    resp_data = sorted(resp_data, key=lambda data: data['num'], reverse=True)
    return resp_data


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
