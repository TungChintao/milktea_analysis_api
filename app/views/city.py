from app.views import city_bp
from . import make_resp


@city_bp.route('/')
def index():
    return make_resp('city')


