import json
import os

class LeitorJSON:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
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