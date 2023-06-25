from sqlalchemy import create_engine, URL, MetaData
from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

url_object = URL.create(
    "mysql",
    username=config['DB_USERNAME'],
    password=config['DB_PASSWORD'],
    host=config['DB_HOSTNAME'],
    database=config['DB_DATABASE']
)

engine = create_engine(url_object, echo=True)

metadata_obj = MetaData()