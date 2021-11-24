# app/views/__init__.py
from flask import Blueprint, jsonify

summary_bp = Blueprint('summary', __name__)
brand_bp = Blueprint('brand', __name__)
city_bp = Blueprint('city', __name__)
word_bp = Blueprint('word', __name__)


def make_resp(data, status=200, message="success"):
    """
    自定义请求的反馈响应
    """
    return jsonify(status=status, message=message, data=data)


from . import summary
from . import brand
from . import city
from . import word

