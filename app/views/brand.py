from app.views import brand_bp
from . import make_resp
from app.utils.brand_analysis import *


@brand_bp.route('/')
def index():
    return make_resp('brand')


@brand_bp.route('/detail/<brand>')
def brand_detail(brand):
    num, resp_data = get_brand_detail(brand)

    data = {
        'brand': brand,
        'city_num': num,
        'detail': resp_data
    }

    return make_resp(data)


@brand_bp.route('/price/<brand>')
def brand_price(brand):
    resp_data = get_brand_price(brand)
    data = {
        'brand': brand,
        'price_area': resp_data
    }
    return make_resp(data)


@brand_bp.route('/score/<brand>')
def brand_score(brand):
    resp_data = get_brand_score(brand)
    data = {
        'brand': brand,
        'score_area': resp_data
    }
    return make_resp(data)
