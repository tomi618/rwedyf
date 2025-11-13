from rwydef.extensions import db
from .wsgi import app

def init_db(app, db):
      with app.app_context():
            db.create_all()
            print('Database created successfully')
            
init_db(app, db)