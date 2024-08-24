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
    __tablename__ = 'FormularioTemplate'
    form_id = db.Column(db.Integer, primary_key=True)
    form_user = db.Column(db.String(500), nullable=False)
    form_cuidx = db.Column(db.String(255), nullable=False)
    form_idx = db.Column(db.Integer, nullable=False)
    form_status = db.Column(db.String(255), nullable=False)
    form_descript = db.Column(db.String(2000), nullable=True)
    form_connection_cuidx = db.Column(db.String(255), nullable=False)
    form_type = db.Column(db.String(255), nullable=False)
    form_game = db.Column(db.String(255), nullable=False)
    form_game_type = db.Column(db.String(255), nullable=False)

class FormulariolistTemplate(db.Model):
    __tablename__ = 'formulario_list_template'
    list_id = db.Column(db.Integer, primary_key=True)
    list_cuidx = db.Column(db.String(255), nullable=False)
    list_status = db.Column(db.String(255), nullable=False)
    list_idx = db.Column(db.Integer)
    list_descript = db.Column(db.String(2000), nullable=True)
    list_class = db.Column(db.String(255), nullable=True)
    list_name = db.Column(db.String(255), nullable=True)
    list_valeu = db.Column(db.String(255), nullable=True)
    list_python_code = db.Column(db.String(2000), nullable=True)
    list_type_connection = db.Column(db.String(255), nullable=True)
    list_connection_key = db.Column(db.String(255), nullable=True)
    list_game = db.Column(db.String(255), nullable=False)
    list_game_type = db.Column(db.String(255), nullable=False)


class FormularioSelectTemplate(db.Model):
    __tablename__ = 'formulario_select_template'
    select_id = db.Column(db.Integer, primary_key=True)
    select_cuidx = db.Column(db.String(255), nullable=False)
    select_idx = db.Column(db.Integer, nullable=False)
    select_status = db.Column(db.String(255), nullable=False)
    select_descript = db.Column(db.String(2000), nullable=True)
    select_class = db.Column(db.String(255), nullable=True)
    select_name = db.Column(db.String(255), nullable=True)
    select_value = db.Column(db.String(255), nullable=True)
    select_option_cuidx = db.Column(db.String(255), nullable=True)
    select_python_code = db.Column(db.String(2000), nullable=True)
    select_game = db.Column(db.String(255), nullable=False)
    select_game_type = db.Column(db.String(255), nullable=False)

class FormulariooptionTemplate(db.Model):
    __tablename__ = 'formulario_option_template'
    option_id = db.Column(db.Integer, primary_key=True)
    option_cuidx = db.Column(db.String(255), nullable=False)
    option_idx = db.Column(db.Integer, nullable=False)
    option_status = db.Column(db.String(255), nullable=False)
    option_descript = db.Column(db.String(2000), nullable=True)
    option_class = db.Column(db.String(255), nullable=True)
    option_name = db.Column(db.String(255), nullable=True)
    option_value = db.Column(db.String(255), nullable=True)
    option_python_code = db.Column(db.String(2000), nullable=True)
    option_game = db.Column(db.String(255), nullable=False)
    option_game_type = db.Column(db.String(255), nullable=False)

class FormularioinputTemplate(db.Model):
    __tablename__ = 'formulario_input_template'
    input_id = db.Column(db.Integer, primary_key=True)
    input_cuidx = db.Column(db.String(255), nullable=False)
    input_idx = db.Column(db.Integer, nullable=False)
    input_status = db.Column(db.String(255), nullable=False)
    input_descript = db.Column(db.String(2000), nullable=True)
    input_type = db.Column(db.String(255), nullable=False)
    input_name = db.Column(db.String(255), nullable=True)
    input_value =  db.Column(db.String(255), nullable=True)
    input_placeholder = db.Column(db.String(255), nullable=True)
    input_class = db.Column(db.String(255), nullable=True)
    input_disabled = db.Column(db.String(255), nullable=True)
    input_readonly = db.Column(db.String(255), nullable=True)
    input_required = db.Column(db.String(255), nullable=True)
    input_maxlength = db.Column(db.String(255), nullable=True)
    input_min = db.Column(db.String(255), nullable=True)
    input_max = db.Column(db.String(255), nullable=True)
    input_pattern = db.Column(db.String(255), nullable=True)
    input_size = db.Column(db.String(255), nullable=True)
    input_autocomplete = db.Column(db.String(255), nullable=True)
    input_autofocus = db.Column(db.String(255), nullable=True)
    input_onclick = db.Column(db.String(2000), nullable=True)
    input_python_code = db.Column(db.String(2000), nullable=True)
    input_complement = db.Column(db.String(255), nullable=True)
    input_game = db.Column(db.String(255), nullable=False)
    input_game_type = db.Column(db.String(255), nullable=False)

class FormularioinputTemplate(db.Model):
    __tablename__ = 'formulario_ul_template'
    ul_id = db.Column(db.Integer, primary_key=True)
    ul_cuidx = db.Column(db.String(255), nullable=False)
    ul_idx = db.Column(db.Integer, nullable=False)
    ul_status = db.Column(db.String(255), nullable=False)
    ul_descript = db.Column(db.String(2000), nullable=True)
    ul_class = db.Column(db.String(255), nullable=True)
    ul_style = db.Column(db.String(255), nullable=True)
    ul_title = db.Column(db.String(255), nullable=True)
    ul_dir = db.Column(db.String(255), nullable=True)
    ul_lang = db.Column(db.String(255), nullable=True)
    ul_role = db.Column(db.String(255), nullable=True)
    ul_aria_label = db.Column(db.String(255), nullable=True)
    ul_aria_hidden = db.Column(db.String(255), nullable=True)
    ul_python_code = db.Column(db.String(2000), nullable=True)
    ul_complement = db.Column(db.String(255), nullable=True)
    ul_game = db.Column(db.String(255), nullable=False)
    ul_game_type = db.Column(db.String(255), nullable=False)