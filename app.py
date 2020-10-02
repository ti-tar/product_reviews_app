import os

from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['PER_PAGE'] = 5

db = SQLAlchemy(app)

migrate = Migrate(app, db)

main_blueprint = Blueprint('main_blueprint', __name__, url_prefix='/')
api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')

import views

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run()
