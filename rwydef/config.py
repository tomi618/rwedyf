import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv(os.path.join(os.getcwd(), 'rwydef', '.env'))

password = quote_plus(os.getenv('PASSWORD'))
class Config():
      DEBUG=True
      PORT=os.getenv('PORT')
      SECRET_KEY=os.getenv('SECRET_KEY')
      SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')#f"postgresql+psycopg2://{os.getenv('USER')}:{password}@localhost:{os.getenv('PORT')}/{os.getenv('DB')}" 