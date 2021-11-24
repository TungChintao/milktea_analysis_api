# app/__init__.py
from flask import Flask
from flask_cors import CORS
from app.configs import config_map
from app.libs.extensions import db, migrate


def create_app(key="development"):
    """
    工厂函数
    """
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_map[key])
    register_extensions(app)
    register_blueprints(app)
    # db.create_all()
    return app


def register_extensions(app):
    """
    注册第三方插件
    """
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """
    注册蓝图
    """
    from app.views import summary_bp
    from app.views import brand_bp
    from app.views import city_bp
    from app.views import word_bp
    app.register_blueprint(summary_bp, url_prefix='/api/summary')
    app.register_blueprint(brand_bp, url_prefix='/api/brand')
    app.register_blueprint(city_bp, url_prefix='/api/city')
    app.register_blueprint(word_bp, url_prefix='/api/wordcloud')

