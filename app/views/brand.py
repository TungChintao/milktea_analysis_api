from app.views import brand_bp


@brand_bp.route('/')
def index():
    return 'brand'
