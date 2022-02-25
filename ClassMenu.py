from ClassConsultas import *
from ClassInterface import *
from time import sleep

tamanho = 100
empresa = 'NOME DA EMPRESA'
app = 'ANALISE DE PRODUTOS'

lista_menu = [
    'Listar as categorias',
    'Listar os produtos de uma categoria',
    'Listar o produto mais caro por categoria',
    'Listar o produto mais barato por categoria',
    'Listar os 10 produtos mais caros',
    'Listar os 10 produtos mais baratos',
    'Sair'
]


class Menu:

    def __init__(self, menu):
        self.menu = menu


    def menu(self, dados):

        categoria_inexistente = 'Categoria inexistente. Digite uma categoria que existe.'
        escolher_categoria = 'Digite a categoria que deseja consultar: '
        escolher_opcao = 'Escolha uma das seguintes opções acima: '
        opcao_invalida = 'Por favor, digite uma opção válida.'

        opcao = 999
        Interface.imprimir_cabecalho_sistema(self, empresa, app)

            
        while opcao != 0:
            Interface.apresentar_menu_principal(self, lista_menu)
            
            o = str(input(escolher_opcao))
            while o.isnumeric() != True:
                print(opcao_invalida)
                o = str(input(escolher_opcao))
            opcao = int(o)


            if opcao == 1:
                sleep(1)
                Interface.imprimir_cabecalho_interno(self, 'Lista de Categorias por Ordem Alfabética')
                Consultas.listar_categorias(self, dados)
                for elemento in Consultas.listar_categorias(self, dados):
                    print(elemento)
                print(f'\nExistem {len(Consultas.listar_categorias(self, dados))} categorias ativas no sistema.\n')            
            

            if opcao == 2:
                categoria = input(escolher_categoria).strip().lower()

                while categoria not in Consultas.listar_categorias(self, dados):
                    print(categoria_inexistente)
                    categoria = input(escolher_categoria).strip().lower()
                
                sleep(1)
                Interface.imprimir_cabecalho_interno(self, f'Lista de Produtos da Categoria: {categoria}')
                tam = int(tamanho / 2)
                print(f'{"PRODUTO":<8} {"PRECO":<5}')
                print('-' * 14)
                for elemento in Consultas.listar_produto_por_categoria(self, dados, categoria):
                    print(elemento['id'], elemento['preco'])
                print(f'\nExistem {len(Consultas.listar_produto_por_categoria(self, dados, categoria))} produtos para esta categoria.\n')  
                
            
            if opcao == 3:
                categoria = input(escolher_categoria).strip().lower()

                while categoria not in Consultas.listar_categorias(self, dados):
                    print(categoria_inexistente)
                    categoria = input(escolher_categoria).strip().lower()

                sleep(1)
                Interface.imprimir_cabecalho_interno(self, f'Produto Mais Caro da Categoria: {categoria}')
                print(f'{Consultas.listar_produto_mais_caro(self, dados, categoria)}')

            
            if opcao == 4:
                categoria = input(escolher_categoria).strip().lower()

                while categoria not in Consultas.listar_categorias(self, dados):
                    print(categoria_inexistente)
                    categoria = input(escolher_categoria).strip().lower()

                sleep(1)
                Interface.imprimir_cabecalho_interno(self, f'Produto Mais Barato da Categoria: {categoria}')
                print(f'{Consultas.listar_produto_mais_barato(self, dados, categoria)}')

            
            if opcao == 5:
                sleep(1)
                Interface.imprimir_cabecalho_interno(self, f'Lista 10 Produtos Mais Caros')
                print(f'{"PRODUTO":<8} {"PRECO":<5} {"CATEGORIA":<9}')
                print('-' * 30)
                for elemento in Consultas.listar_top_10_caros(self, dados):
                    print(elemento[0][0], elemento[0][1], elemento[0][2])
                print('')

            
            if opcao == 6:
                sleep(1)
                Interface.imprimir_cabecalho_interno(self, f'Lista 10 Produtos Mais Baratos')
                print(f'{"PRODUTO":<8} {"PRECO":<5} {"CATEGORIA":<9}')
                print('-' * 30)
                for elemento in Consultas.listar_top_10_baratos(self, dados):
                    print(elemento[0][0], elemento[0][1], elemento[0][2])
                print('')

            
            if opcao == 7:
                sleep(1)
                Interface.imprimir_cabecalho_interno(self, f'Saindo ...')
                sleep(2)
                break

            
            if opcao >= 8:
                print(opcao_invalida)