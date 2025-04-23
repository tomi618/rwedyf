from rwydef import create_app
from init_db import init_db
from rwydef.extensions import db

app = create_app()

if __name__ == '__main__':
      init_db(app, db)
      app.run()