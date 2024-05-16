import json
import os

class LeitorJSON:
    caminho_vrising=f"""{str(os.getenv('VRISING_JSON_LOCATE'))}"""

    def __init__(self):
        self.caminho_arquivo = self.caminho_vrising
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

def geraJSON(dado):
     caminho_diretorio=f"""{str(os.getenv('VRISING_GERAR_JSON_LOCATE'))}"""
     caminho_arquivo = os.path.join(caminho_diretorio,'ServerHostSettings.json')
     with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(dado, arquivo_json, indent=2)