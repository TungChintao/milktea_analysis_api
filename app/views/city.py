from . import make_resp
from app.views import city_bp
from flask import redirect, request
from app.utils.city_analysis import *


@city_bp.route('/')
def index():
    return make_resp('city')


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
        results_list = get_city_brands_top50(city_name)
        data_dict = {
            'titles': results_list
        }
        return make_resp(data=data_dict)


# 表三：主要品牌区域分布
@city_bp.route('/shop/address/<city>', methods=['GET'])
def get_shop_address(city):
    city_name = city
    if city_name not in get_cities_list():
        return make_resp(data=[], status=404, message="fail")
    else:
        result_list = get_brands_top5_address(city_name)
        data_dict = {
            'addresses': result_list
        }
        return make_resp(data=data_dict)
