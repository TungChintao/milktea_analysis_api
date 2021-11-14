from . import make_resp
from app.views import city_bp
from flask import redirect, request
from app.utils.city_analysis import *


@city_bp.route('/')
def index():
    return make_resp('city')


# 生成城市地图信息
@city_bp.route('/generate_map/cities', methods=['POST'])
def generate_map():
    getjson = request.get_json()
    city_name = getjson.get("city_name")
    if city_name == '武汉':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/420100_full.json")
    elif city_name == '南京':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/320100_full.json")
    elif city_name == '深圳':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/440300_full.json")
    elif city_name == '广州':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/440100_full.json")
    elif city_name == '西安':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/610100_full.json")
    elif city_name == '石家庄':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/130100_full.json")
    elif city_name == '长春':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/220100_full.json")
    elif city_name == '北京':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/110000_full.json")
    elif city_name == '哈尔滨':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/230100_full.json")
    elif city_name == '上海':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/310000_full.json")
    elif city_name == '沈阳':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/210100_full.json")
    elif city_name == '西宁':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/630100_full.json")
    elif city_name == '银川':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/640100_full.json")
    elif city_name == '郑州':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/410100_full.json")
    elif city_name == '乌鲁木齐':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/650100_full.json")
    elif city_name == '呼和浩特':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/150100_full.json")
    elif city_name == '海口':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/460100_full.json")
    elif city_name == '贵阳':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/520100_full.json")
    elif city_name == '南昌':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/360100_full.json")
    elif city_name == '济南':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/370100_full.json")
    elif city_name == '昆明':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/530100_full.json")
    elif city_name == '兰州':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/620100_full.json")
    elif city_name == '杭州':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/330100_full.json")
    elif city_name == '合肥':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/340100_full.json")
    elif city_name == '南宁':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/450100_full.json")
    elif city_name == '长沙':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/430100_full.json")
    elif city_name == '重庆':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/500000_full.json")
    elif city_name == '太原':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/140100_full.json")
    elif city_name == '成都':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/510100_full.json")
    elif city_name == '福州':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/350100_full.json")
    elif city_name == '拉萨':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/540100_full.json")
    elif city_name == '三亚':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/460200_full.json")
    elif city_name == '厦门':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/350200_full.json")
    elif city_name == '天津':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/120000_full.json")
    elif city_name == '苏州':
        return redirect("https://geo.datav.aliyun.com/areas_v3/bound/320500_full.json")
    else:
        return make_resp(data=[], status=404, message="fail")


# 生成地图店铺信息
@city_bp.route('/shop/details/<city>', methods=['GET'])
def get_shop_details(city):
    city_name = city
    city_list = get_cities_list()
    list1 = shop_details(city_name)
    if city_name in city_list:
        return make_resp(data=list1)
    else:
        return make_resp(data=[], status=404, message="fail")


# 图表二：该城市中  各品牌店铺数量与在店铺总数占比
@city_bp.route('/shop/percentage/<city>', methods=['GET'])
def get_shop_percentange(city):
    city_name = city
    if city_name not in get_cities_list():
        return make_resp(data=[], status=404, message="fail")
    else:
        title_list = []
        title_num_list = []
        fifty_shops = get_fifty_shops(city_name)
        for shop in fifty_shops:
            title_list.append(shop[0])
            title_num_list.append(shop[1])
        percentage_list = get_percentage(city_name)
        data_dict = {
            'title_list': title_list,
            'num_list': title_num_list,
            'percentage_list': percentage_list
        }
        return make_resp(data=data_dict)


# 表三：主要品牌区域分布
@city_bp.route('/shop/address/<city>', methods=['GET'])
def get_shop_address(city):
    myjson = request.get_json()
    city_name = city
    if city_name not in get_cities_list():
        return make_resp(data=[], status=404, message="fail")
    else:
        title_list = get_five_shops(city_name)
        address_list = fiveshops_address(city_name)
        address_shopnum_list = get_fiveshops_num(city_name, title_list, address_list)
        data_dict = {
            'addresses': address_list,
            'titles': title_list,
            'shops_num': address_shopnum_list
        }
        return make_resp(data=data_dict)
