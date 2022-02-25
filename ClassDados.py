import json
import os.path
import sys


class Dados:
    
    def __init__(self, dados):
        self.dados = dados


    def obter_dados(self):
        with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
            dados = json.loads(arq.read())
        return dados