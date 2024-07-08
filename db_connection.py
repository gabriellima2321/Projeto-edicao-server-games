import os.path
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from pathlib import Path, os
from dotenv import load_dotenv

load_dotenv()

# Inicialize o Flask
app = Flask(__name__)

# Configuração do SQLAlchemy para a primeira instância
app.secret_key = str(os.getenv('SECRET_KEY'))
dba = f'{str(os.getenv('DBJ'))}://{str(os.getenv('DBJ_USERNAME'))}:{str(os.getenv('DBJ_PASSWORD'))}@{str(os.getenv('DBJ_HOST'))}/{str(os.getenv('DBJ_SCHEMA'))}'
app.config['SQLALCHEMY_DATABASE_URI'] = str(dba)
db = SQLAlchemy(app)
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '\\uploads'
upload_dir = app.config['UPLOAD_PATH'] = UPLOAD_PATH
csrf = CSRFProtect()

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    usuario = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    senha = db.Column(db.String(100), nullable=False)

class Jogos(db.Model):
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    console = db.Column(db.String, nullable=False)

class FormularioTemplate(db.Model):
    __tablename__ = 'formulario_template'
    form_user = db.Column(db.String(500))
    form_type = db.Column(db.String(50), nullable=False)
    form_id = db.Column(db.String(255), nullable=False, primary_key=True)
    form_name = db.Column(db.String(255), nullable=False)
    form_class = db.Column(db.String(255), nullable=True)
    form_descript = db.Column(db.String(255), nullable=True)
    form_value = db.Column(db.String(255), nullable=True)
    form_onclick = db.Column(db.String(255), nullable=True)
    form_python = db.Column(db.String(1000), nullable=True)
    form_end = db.Column(db.String(255), nullable=False)
    form_game = db.Column(db.String(255), nullable=False)
    form_game_type = db.Column(db.String(255), nullable=False)

class FormularioSelectTemplate