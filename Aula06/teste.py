from pprint import pprint

lista_todos_corredores = [{'id': 14, 'nome': 'Usain Bolt', 'tempo': 9.63},     
 {'id': 21, 'nome': 'Sergey Litvinov', 'tempo': 10.1},
 {'id': 7, 'nome': 'Ryan Crouser', 'tempo': 10.2},
 {'id': 35, 'nome': 'Andreas Thorkildsen', 'tempo': 12.5}]

for i, item in enumerate(lista_todos_corredores):    
    if item['id'] == 21:
        lista_todos_corredores[i]['tempo'] = 9.5

pprint(lista_todos_corredores)