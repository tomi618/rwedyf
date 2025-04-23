from rwydef import create_app
from rwydef.extensions import db
import os

app = create_app()

# for development
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))