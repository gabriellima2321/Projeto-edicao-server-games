from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory,session
from authenticator import authenticate,inst_infuser
from db_connection import app,Jogos,upload_dir,app
from dataset import LeitorJSON
from dotenv import load_dotenv
import os

load_dotenv()

caminho=f"""{str(os.getenv('VRISING_JSON_LOCATE'))}"""

@app.route('/')
def index():  # put application's code here
    #Inicia sessao colocando usuario e senha
    if 'user' not in session:
        session['user'] = ''
        session['password'] = ''

    #autentica usuario conforme a base de dados.
    auth = authenticate(session['user'],session['password'])
    if auth:
        return redirect(url_for('v_rising_server_edit'))
    else:
        return redirect(url_for('login'))

# Informações de login e metodo de autheticação:
@app.route('/login')
def login(): #Pagina de login
    return render_template('login_form.html')

@app.route('/authenticar', methods=['POST'])
def authenticar():
        auth = authenticate(request.form['username'],request.form['password'])
        if auth:
            session['user'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

@app.route('/logout')
def logout():  # put application's code here
    session['user'] = None
    session['password'] = None
    return redirect(url_for('login'))


@app.route('/v_rising_server_edit', methods=['GET','POST'])
def v_rising_server_edit(): #Pagina de login
    if (request.method == 'POST'):
        form_data = request.form
        server_name = form_data.get('nome')
        print(server_name)
        return render_template('v_rising_server_edit.html', form_data=form_data)
    
    
    leitor=LeitorJSON(caminho)
    dados = leitor.obter_dado()
    return render_template('v_rising_server_edit.html', info=dados)