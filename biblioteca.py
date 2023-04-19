from sqlalchemy import create_engine
from sqlalchemy.sql import text

#quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///biblioteca.db')

#mas se quisesse uma solução mais robusta, poderia
#usar mudando o código muito pouco
#engine = create_engine('postgresql://usuario:senha@localhost:5432/imobiliaria')


#criar a tabela
def criar_tabelas():
    with engine.connect() as con:    
        create_tabela_aluno = """
        CREATE TABLE IF NOT EXISTS Aluno (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """    
        rs = con.execute(create_tabela_aluno)
        create_tabela_livro = """
        CREATE TABLE IF NOT EXISTS Livro (
            id_livro INTEGER PRIMARY KEY,
            id_aluno INTEGER,
            descricao TEXT NOT NULL,
            FOREIGN KEY(id_aluno) REFERENCES Aluno(id)  
        )
        """   
        rs = con.execute(create_tabela_livro)

def criar_alunos():
    with engine.connect() as con:     
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (1,'Lucas Mendes', 'lucas.mendes@exemplo.com');"
        rs = con.execute(add_aluno)
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (2,'Helena O. S.', 'helena@exemplo.com');"
        rs = con.execute(add_aluno)
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (3,'Mirtes', 'teescrevoumemail@exemplo.com');"
        rs = con.execute(add_aluno)

def criar_livros():
    with engine.connect() as con:
        add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (1,1,'Python completo e total')"
        rs = con.execute(add_livro)
        add_livro = "INSERT INTO Livro (id_livro, descricao) VALUES (2,'Memorias póstumas de brás cubas')"
        rs = con.execute(add_livro)
        add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (3,2,'Gravidade')"
        rs = con.execute(add_livro)

#criar_tabelas()
#criar_alunos()

class AlunoNaoExisteException(Exception):
    pass
#estamos definindo uma classe AlunoNaoExisteException, que
#herda todas as funcionalidades, todos os métodos e atributos,
#de Exception
#no lugar do pass, escreveríamos as mudanças,
#as coisas que AlunoNaoExisteException faz diferente de Exception
#mas não fizemos mudança nenhuma (por isso pass)




# 1) Crie uma função consulta_aluno que recebe a id de um aluno e devolve
# um dicionário com os dados desse aluno

#idéia da query no sql
"SELECT * FROM aluno WHERE id = 2"

def consulta_aluno(id_aluno):
    with engine.connect() as con:   #conectar ao banco de dados 
        sql_consulta = text ("SELECT * FROM aluno WHERE id = :id_do_aluno")
        # id          : nome da coluna da tabela
        # id_aluno    : nome da variavel python que a funcao recebeu
        # id_do_aluno : nome do "buraco" definido na query sql_consulta
        #               nome passado como argumento do con.execute
        rs = con.execute(sql_consulta, id_do_aluno = id_aluno)
        #executamos a query definida em sql_consulta, preenchendo o "buraco" :id_do_aluno
        result = rs.fetchone()
        # fetchone: pega uma linha do resultado
        # se tiver mais linhas, podemos pegar a próxima com outro fetchone
        # se não tiver mais linhas, receberemos um None
        if result == None: #se a query retornou 0 linhas, o primeiro fetchone já resulta None
            raise AlunoNaoExisteException
        # As linhas que o sqlalchemy devolve são parecidas com dicionários,
        # mas não é exatamente a mesma coisa. Por isso, fazemos uma conversão
        return dict(result)


#1b) Crie uma função todos_alunos que retorna um lista com um dicionario
# para cada aluno
def todos_alunos():
    with engine.connect() as con:
        lista_alunos = []
        sql_consulta = text ("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        result = rs.fetchall() # retorna uma lista de tuplas que contém os 
        # valores. Quando converto a tupla para dict, ele vem com o nome da coluna como chave
        for row in result:
            lista_alunos.append(dict(row))
    return lista_alunos

#1c) Crie uma função todos_livros que retorna um lista com um dicionario
# para cada livro
def todos_livros():
    with engine.connect() as con:
        lista_livros = []
        sql_consulta = text('SELECT * FROM livro')
        rs = con.execute(sql_consulta)
        result = rs.fetchall()
        for row in result:
            lista_livros.append(dict(row))
    return lista_livros

# 2) Crie uma função cria livro que recebe os dados de um livro (id e descrição)
# e o adiciona no banco de dados
def cria_livro(id, descricao):
    with engine.connect() as con:
        sql = text('INSERT INTO Livro (id_livro, descricao) VALUES (:id, :descricao)')
        rs = con.execute(sql, id=id, descricao=descricao)
        

# 3) Crie uma função empresta_livro, que recebe a id de um livro, a id de um aluno
# e marca o livro como emprestado pelo aluno
def empresta_livro(id_livro, id_aluno):
    with engine.connect() as con:
        sql = text('UPDATE Livro SET id_aluno = :id_aluno WHERE id_livro = :id_livro')
        rs = con.execute(sql, id_livro=id_livro, id_aluno=id_aluno)

# 4) Crie uma função devolve_livro, que recebe a id de um livro, e marca o livro
# como disponível
def devolve_livro(id_livro):
    with engine.connect() as con:
        sql = ('UPDATE Livro SET id_aluno = NULL WHERE id_livro = :id_livro')
        rs = con.execute(sql, id_livro=id_livro)

# 5) Crie uma função livros_parados que devolve a lista de todos os livros que não estão emprestados
# por ninguém (uma lista de dicionários, um para cada livro)
def livros_parados():
    with engine.connect() as con:
        lista_parados = []
        sql = ('SELECT * FROM Livro WHERE id_aluno ISNULL')
        rs = con.execute(sql)
        resultado = rs.fetchall()
        for row in resultado:
            lista_parados.append(dict(row))
    return lista_parados

# 6) Crie uma função livros_do_aluno, recebe o nome do aluno e devolve a lista de todos
# os livros que estão com o aluno no momento

def livros_do_aluno(nome_aluno):
    with engine.connect() as con:
        lista_livros_aluno = []
        sql = """SELECT id_livro, id_aluno, descricao FROM Livro as l
                INNER JOIN Aluno as a
                On a.id = l.id_aluno
                WHERE a.nome = :nome_aluno
                """
        rs = con.execute(sql, nome_aluno=nome_aluno)
        resultado = rs.fetchall()
        for row in resultado:
            lista_livros_aluno.append(dict(row))
    return lista_livros_aluno