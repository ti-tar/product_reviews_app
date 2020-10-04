import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

# get env vars from `.env` file
if os.path.isfile('.env'):
    print('Environment vars is loading. file: `.env`')
    filepath = os.path.join(str(Path().cwd()), '.env')

    if load_dotenv(dotenv_path=filepath, override=True):
        print('ENV `.env` loaded')
    else:
        sys.exit('Error occurred during loading env file.')

# init app
app = Flask(__name__)

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300

app.config['CACHE_KEY_PREFIX'] = os.getenv('CACHE_KEY_PREFIX')
app.config['CACHE_REDIS_URL'] = os.getenv('CACHE_REDIS_URL')

app.config['PER_PAGE'] = 5

db = SQLAlchemy(app)
migrate = Migrate(app, db)
cache = Cache(app)


# CLI PARSE FILES
@app.cli.command("parse")
def parse():
    from cli.parse import Parse
    p = Parse()
    p.run()


# LOGGER
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(asctime)s | %(message)s")

# blueprints for views
main_blueprint = Blueprint('main_blueprint', __name__, url_prefix='/')
api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')

from . import views

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)
