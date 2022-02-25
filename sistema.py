from ClassDados import *
from ClassConsultas import *
from ClassMenu import *


self = 'self'
dados = Dados.obter_dados(self)

print()
Menu.menu(self, dados)