from app.views import word_bp
from . import make_resp
from app.utils.word_analysis import *


@word_bp.route('', methods=['GET'])
def summary_word():
    data = get_all_word()
    return make_resp(data)


@word_bp.route('/<brand>', methods=['GET'])
def brand_word(brand):
    data = get_brand_word(brand)
    return make_resp(data)
