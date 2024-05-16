from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory,session
from authenticator import authenticate,inst_infuser
from db_connection import app,Jogos,upload_dir,app
from dataset import LeitorJSON,geraJSON
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
        return render_template('index.html',usuario=session['user'])
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

@app.route('/meus_jogos')
def meus_jogos():  # put application's code here
    #Inicia sessao colocando usuario e senha
    if 'user' not in session:
        session['user'] = ''
        session['password'] = ''

    #autentica usuario conforme a base de dados.
    auth = authenticate(session['user'],session['password'])
    if auth:
        return render_template('meus_jogos.html',usuario=session['user'])
    else:
        return redirect(url_for('login'))


@app.route('/v_rising_server_edit')
def v_rising_server_edit(): #Pagina de login
    #Inicia sessao colocando usuario e senha
    if 'user' not in session:
        session['user'] = ''
        session['password'] = ''

    #autentica usuario conforme a base de dados.
    auth = authenticate(session['user'],session['password'])
    if auth:
        leitor=LeitorJSON()
        dados = leitor.obter_dado()
        return render_template('v_rising_server_edit.html', usuario=session['user'] ,info=dados)
    else:
        return redirect(url_for('login'))


@app.route('/atualiza_v_rising_server_edit', methods=['POST'])
def atualiza_v_rising_server_edit():
    name = request.form['nome']
    description = request.form['descricao']
    maxconnectedusers = request.form['number-max-players']
    maxconnectedadmins = request.form['number-max-adm']
    serverfps = request.form['fps-server-tax']
    savename = request.form['save-nome']
    password = request.form['password']
    secure = request.form['seguranca-ativa']
    listonsteam = request.form['listar-steam']
    listoneos = request.form['listar-eos']
    autosavecount = request.form['auto-save-count']
    autosaveinterval = request.form['auto-save-interval']
    compresssavefiles = request.form['compress-file']
    adminonlydebugevents = request.form['adm-event-debug']
    disabledebugevents = request.form['debug-event']
    dados={
        "Name":name,
        "Description":description,
        "Port":9876,
        "QueryPort":9877,
        "MaxConnectedUsers":int(maxconnectedusers),
        "MaxConnectedAdmins":int(maxconnectedadmins),
        "ServerFps": int(serverfps),
        "SaveName": savename,
        "Password":password,
        "Secure":bool(secure),
        "ListOnSteam": bool(listonsteam),
        "ListOnEOS":bool(listoneos),
        "AutoSaveCount": int(autosavecount),
        "AutoSaveInterval": int(autosaveinterval),
        "CompressSaveFiles": bool(compresssavefiles),
        "GameSettingsPreset": "",
        "GameDifficultyPreset": "",
        "AdminOnlyDebugEvents": bool(adminonlydebugevents),
        "DisableDebugEvents": bool(disabledebugevents),
        "API":{"Enabled":False},
        "Rcon": {"Enabled":False,"Port": 25575,"Password": "biribiri1313"}
    }

    geraJSON(dados)
    return redirect(url_for('meus_jogos')) 
