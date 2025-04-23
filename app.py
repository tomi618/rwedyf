from rwydef import create_app
from init_db import init_db
from rwydef.extensions import db
import os

app = create_app()
init_db(app, db)

if __name__ == '__main__':
      port = int(os.environ.get("PORT", 5000))
      app.run(host="0.0.0.0", port=port)