from sqlalchemy import create_engine, URL, MetaData
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

url_object = URL.create(
    "mysql",
    username=os.environ.get('DB_ROOT'),
    password=os.environ.get('DB_ROOT_PASSWORD'),
    host=os.environ.get('DB_HOSTNAME'),
    database=os.environ.get('DB_DATABASE')
)

engine = create_engine(url_object, echo=True)

metadata_obj = MetaData()