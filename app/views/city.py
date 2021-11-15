from . import make_resp
from app.views import city_bp
from flask import redirect, request
from app.utils.city_analysis import *


@city_bp.route('/')
def index():
    return make_resp('city')


# 生成地图店铺信息
@city_db.route('/shop/details/<city>', methods=['GET'])
def get_shop_details(city):
    city_name = city
    city_list = get_citys_list()
    list1 = shop_details(city_name)
    if city_name in city_list:
        return make_resp(data=list1)
    else:
        return make_resp(data=[], status=404, message="fail")


# 图表二：该城市中  各品牌店铺数量与在店铺总数占比
@city_db.route('/shop/percentage/<city>', methods=['GET'])
def get_shop_percentange(city):
    city_name = city
    if city_name not in get_citys_list():
        return make_resp(data=[], status=404, message="fail")
    else:
        title_list = []
        title_num_list = []
        fifty_shops = get_fifty_shops(city_name)
        for shop in fifty_shops:
            title_list.append(shop[0])
            title_num_list.append(shop[1])
        percentage_list = get_percentage(city_name)
        results_list = []
        for n in range(50):
            result_data = {
                'title': title_list[n],
                'num_and_percentage': {
                    'num': title_num_list[n],
                    'percentage': percentage_list[n]
                }
            }
            results_list.append(result_data)
        data_dict = {
            'titles': results_list
        }
        return make_resp(data=data_dict)


# 表三：主要品牌区域分布
@city_db.route('/shop/address/<city>', methods=['GET'])
def get_shop_address(city):
    city_name = city
    if city_name not in get_citys_list():
        return make_resp(data=[], status=404, message="fail")
    else:
        # 品牌列表
        title_list = get_five_shops(city_name)
        # 地区列表
        address_list = fiveshops_address(city_name)
        # 店铺数量列表
        address_shopnum_list = get_fiveshops_num(city_name, title_list, address_list)
        address_dict_array = []
        for n in range(len(address_list)):
            shops_list = []
            for m in range(5):
                shop_dict = {
                    'shopnum': address_shopnum_list[n][m],
                    'title': title_list[m]
                }
                shops_list.append(shop_dict)
            address_dict = {
                'address': address_list[n],
                'shops': shops_list
            }
            address_dict_array.append(address_dict)
        data_dict = {
            'addresses': address_dict_array
        }
        return make_resp(data=data_dict)
