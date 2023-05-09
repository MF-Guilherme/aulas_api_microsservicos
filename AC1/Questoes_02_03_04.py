from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///imoveis.db')


class Imovel:
    def __init__(self, id, logradouro, numero, cep):
        pass
    
    
def criar_tabela():
    with engine.connect() as con:
        create_tabela_imoveis = """
        CREATE TABLE IF NOT EXISTS imoveis  (
            id INTEGER PRIMARY KEY,
            logradouro TEXT NOT NULL,
            numero INTEGER NOT NULL,
            cep TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL)
        """
        rs = con.execute(create_tabela_imoveis)
        

def criar_imoveis():
    with engine.connect() as con:
        add_imovel = "INSERT INTO imoveis (id, logradouro, numero, cep, cidade, estado) VALUES (1, 'Rua Eurides Lopes', 6, '123645789-10', 'São Paulo', 'SP')"
        con.execute(add_imovel)
        add_imovel1 = "INSERT INTO imoveis (id, logradouro, numero, cep, cidade, estado) VALUES (2, 'Rua Felipe Cardoso', 550, '123645789-10', 'São Paulo', 'SP')"
        con.execute(add_imovel1)
        add_imovel2 = "INSERT INTO imoveis (id, logradouro, numero, cep, cidade, estado) VALUES (3, 'Rua Laranjal do Jari', 360, '123645789-10', 'São Paulo', 'SP')"
        con.execute(add_imovel2)


def converte_dict_para_imovel(linha):
    d = dict(linha)
    return Imovel(**d)


def pesquisar(nome_rua):
    with engine.connect() as con:
        lista = []
        sql = text("SELECT id, logradouro, numero, cep FROM imoveis WHERE logradouro = :logradouro")
        rs = con.execute(sql, logradouro=nome_rua)
        for linha in rs.fetchall():
            lista.append(converte_dict_para_imovel(linha))
        return lista
    