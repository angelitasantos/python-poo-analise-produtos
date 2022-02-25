import datetime
data_hora_atuais = datetime.datetime.now()
data_hora_pt_BR = data_hora_atuais.strftime(' %d/%m/%Y %H:%M:%S')

tamanho = 100


class Interface:

    def __init__(self, tamanho):
        self.tamanho = tamanho


    def incrementar_linha(self, tamanho=50, caracter='-'):
        return caracter * tamanho


    def imprimir_cabecalho_sistema(self, empresa='', app='', versao='v1.0 '):
        tam = int(tamanho / 2)
        caracter = '='
        print(f'{Interface.incrementar_linha(self, tamanho, caracter)}')
        empresa = empresa.center(tamanho)
        print(f'{empresa}')
        app = app.center(tamanho)
        print(f'{app}')
        print(f'{data_hora_pt_BR.ljust(tam)}{versao.rjust(tam)}')
        print(f'{Interface.incrementar_linha(self, tamanho, caracter)}')


    def imprimir_cabecalho_interno(self, texto=''):
        print(Interface.incrementar_linha(self, tamanho))
        print(texto.center(tamanho))
        print(Interface.incrementar_linha(self, tamanho))


    def apresentar_menu_principal(self, lista):
        Interface.imprimir_cabecalho_interno(self, 'MENU PRINCIPAL')
        contador = 1
        for item in lista:
            print(f'{contador:>30} - {item}')
            contador += 1
        print(Interface.incrementar_linha(self, tamanho, '~'))