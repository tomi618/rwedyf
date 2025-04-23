import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv(os.path.join(os.getcwd(), 'rwydef', '.env'))

# password = quote_plus(os.getenv('PASSWORD'))
database_uri = quote_plus(os.getenv('DATABASE_URI'))
class Config():
      DEBUG=False
      SECRET_KEY=os.getenv('SECRET_KEY')
      SQLALCHEMY_DATABASE_URI = database_uri