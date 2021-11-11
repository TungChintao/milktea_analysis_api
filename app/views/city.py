from app.views import city_bp


@city_bp.route('/')
def index():
    return 'city'
