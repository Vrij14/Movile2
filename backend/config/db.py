from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/petspa"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.secret_key = "movil2"

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

