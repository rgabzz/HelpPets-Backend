from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile(filename='config.py')

    db.init_app(app=app)
    jwt.init_app(app=app)

    from app.routes.user import user_bp
    app.register_blueprint(user_bp)

    from app.routes.report import report_bp
    app.register_blueprint(report_bp)

    return app