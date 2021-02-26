from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.doors.views import blueprint as doors_blueprint
from webapp.showers.views import blueprint as showers_blueprint
from webapp.mirrors.views import blueprint as mirrors_blueprint
from webapp.septums.views import blueprint as septums_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.errors import blueprint as errors_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(errors_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(doors_blueprint)
    app.register_blueprint(showers_blueprint)
    app.register_blueprint(mirrors_blueprint)
    app.register_blueprint(septums_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
