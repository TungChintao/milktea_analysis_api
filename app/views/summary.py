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




