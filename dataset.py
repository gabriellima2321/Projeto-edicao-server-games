import json
import os
from dotenv import load_dotenv
load_dotenv()

arquivo_vrising_server='ServerHostSettings.json'
arquivo_vrising_game='ServerGameSettings.json'

class LeitorJSON:
    caminho_vrising_server=f"""{str(os.getenv('ENTRADA_JSON_LOCATE'))}"""+arquivo_vrising_server
    caminho_vrising_game=f"""{str(os.getenv('ENTRADA_JSON_LOCATE'))}"""+arquivo_vrising_game
    print(caminho_vrising_server)
    print(caminho_vrising_game)

    def __init__(self,game=None,type=None):
        print(type)
        print(game)
        self.caminho_arquivo =''
        if (game=='vrising' and type=='server'):
            self.caminho_arquivo = self.caminho_vrising_server
        elif (game=='vrising' and type=='game'):
            self.caminho_arquivo = self.caminho_vrising_game
        self.dados = self._carregar_json()

    def _carregar_json(self):
        # Abre o arquivo usando a codificação 'utf-8-sig' para lidar com o BOM
        with open(self.caminho_arquivo, 'r', encoding='utf-8-sig') as arquivo:
            dados = json.load(arquivo)
        return dados

    def obter_dado(self):
        return self._carregar_json()

# Exemplo de uso
if __name__ == "__main__":
        caminho_arquivo_json = os.path.join(os.path.dirname(__file__), 'dados.json')
        leitor = LeitorJSON(caminho_arquivo_json)
        print(leitor.obter_dado('nome'))  # Deve imprimir 'João'

def geraJSON(dado,game=None,type=None):
     if (game=='vrising' and type=='server'):
         arquivo_name=arquivo_vrising_server
     elif (game=='vrising' and type=='game'):
         arquivo_name=arquivo_vrising_game

     caminho_diretorio=f"""{str(os.getenv('SAIDA_GERAR_JSON_LOCATE'))}"""
     caminho_arquivo = os.path.join(caminho_diretorio,arquivo_name)
     with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(dado, arquivo_json, indent=2)