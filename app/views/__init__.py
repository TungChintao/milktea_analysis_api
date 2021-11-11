# app/views/__init__.py
from flask import Blueprint

summary_bp = Blueprint('summary', __name__)
brand_bp = Blueprint('brand', __name__)
city_bp = Blueprint('city', __name__)

from . import summary
from . import brand
from . import city
