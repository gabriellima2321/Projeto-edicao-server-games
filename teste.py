import os
from dotenv import load_dotenv
load_dotenv()

caminho_vrising=f"""{str(os.getenv('ENTRADA_JSON_LOCATE'))}"""+'ServerHostSettings.json'


print(caminho_vrising)