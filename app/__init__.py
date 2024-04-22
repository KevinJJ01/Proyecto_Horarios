from flask import Flask, render_template, Blueprint
from .config import Config
from app.coordinaciones import coordinaciones
from app.transversal import transversal
from app.centros import centros 
from app.regionales import regionales
from app.administrador import administrador
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

#inicializar el objeto SQLALCHEMY
db=SQLAlchemy(app)
migrate=Migrate(app, db)

#registrar modulos(blueprints)
app.register_blueprint(centros)
app.register_blueprint(regionales)
app.register_blueprint(administrador)
app.register_blueprint(transversal)
app.register_blueprint(coordinaciones)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")


from .models import *