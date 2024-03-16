from back.models import db_postgres
from flask import Flask
from mongoengine import connect
from flask_pymongo import PyMongo
from gridfs import GridFS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://starisii:starisii@localhost:5432/starisii'
app.config['MONGO_DBNAME'] = 'Starisii'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Starisii'

connect(db='Starisii', host='mongodb://localhost:27017/Starisii')
#client = pymongo.MongoClient("mongodb://localhost:27017/flask_db")
# Initialize the SQLAlchemy, Mongo database
db_postgres.init_app(app)
mongo = PyMongo(app)

grid_fs_seniors = GridFS(mongo.db, collection='seniors_photos')
grid_fs_youngers = GridFS(mongo.db, collection='youngers_photos')