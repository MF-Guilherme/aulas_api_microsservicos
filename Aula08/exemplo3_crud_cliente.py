
import requests

def entradaDados():
	nome = input("Digite o nome: ")
	sexo = input("Digite o sexo: ")
	cabelo = input("Digite a cor do cabelo: ")

	dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}
	
	return dados

def testePost():
	dados = entradaDados()
	x = requests.post("http://localhost:5002/pessoa", json = dados)
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.text) 
	
def testePut():
	id_pessoa = int(input('Digite o id da pessoa que deseja alterar: '))
	dados = entradaDados()
	x = requests.put("http://localhost:5002/pessoa/"+str(id_pessoa), json = dados)
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.text) 

def testeGetId():
	id_pessoa = int(input('Digite o id da pessoa que deseja buscar: '))
	x = requests.get("http://localhost:5002/pessoa/"+str(id_pessoa))
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.text) 	

def testeDelete():
	id_pessoa = int(input('Digite o id da pessoa que deseja excluir: '))
	x = requests.delete("http://localhost:5002/pessoa/"+str(id_pessoa))
	if x.status_code != 200:
		print(f"[{x.status_code}] {x.text}")
	else:
		print(x.text) 		

print('------------------------------------------\n')		
print('Tentando a rota /pessoa com POST\n')
testePost()

print('------------------------------------------\n')	
print('Tentando a rota /pessoa com POST novamente \n')	
testePost()

print('------------------------------------------\n')	
print('Tentando a rota /pessoa com PUT \n')	
testePut()	
	
print('------------------------------------------\n')	
print('Tentando a rota /pessoa com GET e pessoa específica\n')	
testeGetId()

print('------------------------------------------\n')	
print('Tentando a rota /pessoa com DELETE\n')	
testeDelete()
