import requests
from pprint import pprint


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores do servidor de corredoes
# via GET, e devolve uma lista de todos os corredores

def todos_corredores():
    url = "http://127.0.0.1:5000/corredores"
    requisicao = requests.get(url)
    dic_requisicao = requisicao.json()
    return dic_requisicao



# faça uma função usando a biblioteca requests
# que acessa a URL /corredores do servidor de corredoes
# via POST, enviando um dicionário de um novo corredor.
# Um corredor tem os campos "nome", "tempo" e "id"

def inserir_corredor(nome, tempo, id):
    url = "http://127.0.0.1:5000/corredores"
    dicionario = {
        "nome": nome,
        "tempo": tempo,
        "id": id
    }
    requisicao = requests.post(url, json=dicionario)
    return True


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/maior_tempo do servidor
# de corredoes
# via GET, e retorne o nome do corredor
# mais lento


def corredor_mais_lento():
    url = "http://127.0.0.1:5000/corredores/maior_tempo"
    requisicao = requests.get(url)
    dic_requisicao = requisicao.json()
    return dic_requisicao["nome"]


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/maior_tempo do servidor
# de corredoes
# via DELETE, causando a remoção dos dados do corredor
# mais lento.
# Infelizmente o servidor tem um bug no caso em que a lista
# de corredores está vazia, mas vamos tratar esse bug
# no nosso cliente

def deletar_mais_lento():
    url = "http://127.0.0.1:5000/corredores/maior_tempo"
    requisicao = requests.delete(url)
    if requisicao.status_code == 200:
        return True
    return "Não é possível deletar dados de uma lista vazia"


# porque a funcionalidade anterior consiste em um erro
# de design no servidor corredores?

'''
O verbo DELETE deveria ser IDEMPOTENTE.
Deveria ser o caso que uma segunda chamada nao causa um efeito colateral
'''


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via GET,
# sua função deve retornar o nome do corredor em questão
# o o seu melhor tempo, em uma tupla

def corredor_por_id(id):
    url = f"http://127.0.0.1:5000/corredores/{id}"
    requisicao = requests.get(url)
    # como eu trataria o erro 404 e informaria o meu usuário?
    if requisicao.status_code == 404:
        return "Corredor não encontrado"
    dic_requisicao = requisicao.json()
    return (dic_requisicao["corredor"]["nome"], dic_requisicao["corredor"]["tempo"])


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via DELETE,
# causando a remoção dos dados do corredor
# mais lento

def deletar_corredor_por_id(id):
    url = f"http://127.0.0.1:5000/corredores/{id}"
    
    if requests.delete(url, json=id).status_code == 404:
        return "corredor não encontrado"
    return "Corredor deletado"


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via PUT,
# e você deverá enviar um dicionário com o novo tempo,
# para atualizar
# o tempo atual do corredor. O tempo deverá ser menor
# do que o tempo atual, caso contrário, o servidor
# lançará um erro, que você deve tratar
