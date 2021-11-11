from app.views import summary_bp


@summary_bp.route('/', methods=['GET'])
def index():
    return 'summary'
