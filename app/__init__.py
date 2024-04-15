from flask import Flask, render_template, Blueprint
from .config import Config
from app.centros import centros 
from app.regionales import regionales
from app.administrador import administrador
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)

#inicializar el objeto SQLALCHEMY
db=SQLAlchemy(app)
migrate=Migrate(app, db)

#registrar modulos(blueprints)
app.register_blueprint(centros)
app.register_blueprint(regionales)
app.register_blueprint(administrador)



@app.route('/')
def index():
    return render_template("index.html")
