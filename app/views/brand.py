from app.views import brand_bp
from . import make_resp


@brand_bp.route('/')
def index():
    return make_resp('brand')
