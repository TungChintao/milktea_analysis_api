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
@summary_bp.route("/brands/top50", methods=['GET'])
def top_fifty_brands():
    data = get_top_brands()
    return make_resp(data=data)


# 全国前50品牌及产品价格
@summary_bp.route("/brands/goods/top50", methods=['GET'])
def top_fifty_brands_goods():
    data = get_top_brands_goods()
    return make_resp(data=data)


