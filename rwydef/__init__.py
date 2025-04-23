from flask import Flask
from rwydef.routes.main import main_blueprint
from rwydef.config import Config
from .extensions import db
from flask_migrate import Migrate

def create_app():
      app = Flask(__name__)
      app.config.from_object(Config)
      
      register_extensions(app)
      register_blueprints(app)
      
      return app

def register_blueprints(app):
      app.register_blueprint(main_blueprint)
      
def register_extensions(app):
      db.init_app(app)
      Migrate(app, db)