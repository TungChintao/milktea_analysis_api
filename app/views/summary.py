from app.views import summary_bp
from . import make_resp
from app.utils.analysis import *
# 获取参数
# 检验参数
# 业务逻辑处理
# 返回值


@summary_bp.route('/', methods=['GET'])
def heat():
    return make_resp('summary')


@summary_bp.route('/shopnum', methods=['GET'])
def index():
    data = cities_shop_num()
    return make_resp(data)


# 全国前50热门品牌以及店铺数量
@summary_bp.route("/top/fifty/brands", methods=['GET'])
def top_fifty_brands():
    fifty_brands = get_top_fifty_brands_and_shopnum()
    list1 = []
    for n in range(50):
        a = {
            'title': fifty_brands[n][0],
            'num': fifty_brands[n][1]
        }
        list1.append(a)
    data = {
        'brands': list1
    }
    return make_resp(data=data)


# 全国前50品牌及产品价格
@summary_bp.route("/top/fifty/brands/goods", methods=['GET'])
def top_fifty_brands_goods():
    data = get_top_fifty_brands_and_goods()
    return make_resp(data=data)


