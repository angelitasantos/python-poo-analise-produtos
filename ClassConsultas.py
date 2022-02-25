from ClassDados import *


class Consultas:

    def __init__(self, dados):
        self.dados = dados
    

    def listar_categorias(self, dados):
        lista_categorias = []
        for categoria in dados:
            if not (categoria['categoria']) in lista_categorias:
                lista_categorias.append(categoria['categoria'])
        lista_categorias.sort()
        return lista_categorias


    def listar_produto_por_categoria(self, dados, categoria):
        produto_por_categoria = []
        for produto in dados:
            if produto['categoria'] == categoria:
                produto_por_categoria.append({'id': produto['id'], 'preco': produto['preco']})
        return produto_por_categoria


    def listar_produto_mais_caro(self, dados, categoria):
        lista_mais_caro = []
        produto_mais_caro = {}
        for produto in dados:
            if produto['categoria'] == categoria:
                lista_mais_caro.append(float(produto['preco']))
                produto_mais_caro[categoria] = lista_mais_caro[0]
            lista_mais_caro.sort(reverse=True)

        mais_caro = str(lista_mais_caro[0])
        for produto in dados:
            if produto['preco'] == mais_caro:
                print({'categoria': produto['categoria'], 'id': produto['id'], 'preco': produto['preco']})
        resultado = ''
        return resultado


    def listar_produto_mais_barato(self, dados, categoria):
        lista_mais_barato = []
        produto_mais_barato = {}
        for produto in dados:
            if produto['categoria'] == categoria:
                lista_mais_barato.append(float(produto['preco']))
                produto_mais_barato[categoria] = lista_mais_barato[0]
            lista_mais_barato.sort()

        mais_barato = str(lista_mais_barato[0])
        for produto in dados:
            if produto['preco'] == mais_barato:
                print({'categoria': produto['categoria'], 'id': produto['id'], 'preco': produto['preco']})
        resultado = ''
        return resultado

    
    def listar_top_10_caros(self, dados):
        lista_ordem_mais_caro = []
        for produto in dados:
            lista_ordem_mais_caro.append(float(produto['preco']))
        lista_ordem_mais_caro.sort(reverse=True)

        ordem_mais_caro = lista_ordem_mais_caro[:10]
        ordem_mais_caro_str = []
        for elemento in ordem_mais_caro:
            ordem_mais_caro_str.append(str(elemento))

        por_preco = {}
        for dado in dados:
            if not (dado['preco']) in por_preco:
                por_preco[dado['preco']] = []
            id = dado['id']
            preco = dado['preco']
            categoria = dado['categoria']
            por_preco[dado['preco']].append([id, preco, categoria])

        lista_10_mais_caros = []
        for elemento in ordem_mais_caro_str:
            if elemento in por_preco:
                lista_10_mais_caros.append(por_preco[elemento])
        return lista_10_mais_caros


    def listar_top_10_baratos(self, dados):
        lista_ordem_mais_barato = []
        for produto in dados:
            lista_ordem_mais_barato.append(float(produto['preco']))
        lista_ordem_mais_barato.sort()

        ordem_mais_barato = lista_ordem_mais_barato[:10]
        ordem_mais_barato_str = []
        for elemento in ordem_mais_barato:
            ordem_mais_barato_str.append(str(elemento))

        por_preco = {}
        for dado in dados:
            if not (dado['preco']) in por_preco:
                por_preco[dado['preco']] = []
            id = dado['id']
            preco = dado['preco']
            categoria = dado['categoria']
            por_preco[dado['preco']].append([id, preco, categoria])

        lista_10_mais_baratos = []
        for elemento in ordem_mais_barato_str:
            if elemento in por_preco:
                lista_10_mais_baratos.append(por_preco[elemento])
        return lista_10_mais_baratos