from dataset import LeitorJSON
from dotenv import load_dotenv
import os

load_dotenv()

caminho=f"""{str(os.getenv('VRISING_JSON_LOCATE'))}"""
leitor=LeitorJSON(caminho)
nome=leitor.obter_dado('Name')
print(nome)