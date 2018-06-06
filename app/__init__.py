from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'some_secret' #not sure why its needed?

db = SQLAlchemy(app)
from app import models , routes
