from sqlalchemy import func, distinct
from app.models import Shop, Good
from app.libs.extensions import db
import requests
province_dict = {'武汉': '湖北', '南京': '江苏', '深圳': '广东', '广州': '广东', '西安': '陕西', '石家庄': '河北', '长春': '吉林', '北京': '北京', '哈尔滨': '黑龙江', '上海': '上海', '沈阳': '辽宁', '西宁': '青海', '银川': '宁夏', '郑州': '河南', '乌鲁木齐': '新疆', '呼和浩特': '内蒙古', '海口': '海南', '贵阳': '贵州', '南昌': '江西', '济南': '山东', '昆明': '云南', '兰州': '甘肃', '杭州': '浙江', '合肥': '安徽', '南宁': '广西', '长沙': '湖南', '重庆': '重庆', '太原': '山西', '成都': '四川', '福州': '福建', '拉萨': '西藏', '三亚': '海南', '厦门': '福建', '天津': '天津', '苏州': '江苏'}


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


# 获取各省份奶茶热度
def get_milktea_heat():
    check_list = []
    resp_data = []
    citys = cities_shop_num()
    total = 0
    for i in citys:
        if i['shopnum'] > total:
            total = i['shopnum']
    for i in citys:
        city = i['city']
        num = i['shopnum']
        heat = num / total
        heat = float("%.2f" % heat)
        province = province_dict['city']
        if province not in check_list:
            check_list.append(province)
            resp_data.append({
                'province': province,
                'heat': heat
            })
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
