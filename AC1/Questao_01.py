dic = {
    "musicas": [
        {"nome": "Hey Jude", "banda" : "Beatles"},
        {"nome": "November Rain", "banda" : "Guns N' Roses"},
        {"nome": "How Deep Is Your Love", "banda" : "Bee Gees"},
    ],
    "filmes": {
        "X-men": ["Wolverine", "Xavier", "Tempestade", "Vampira", "Magneto", "Ciclope", "Gambit"],
        "Avengers": ["Homem de Ferro", "Hulk", "Thanos", "Capitão América", "Thor", "Capitã Marvel", "Homem-Aranha"],
        "Star Wars": ["Luke", "Leia", "C-3PO", "Darth Vader", "Obi-wan", "Yoda", "R2-D2", "Han Solo", "Chewbacca"]
    }
}


def func1(a, b, c, d):
    for x in a:
        if x[b] == d:
            return x[c]
    return "naosei"


# print("Han Solo" in dic["filmes"]["Star Wars"]) #= TRUE

# print("Han Solo" in dic["jogos"]["Mortal Kombat II"]) # = ERROR

# print(dic["musicas"]["Bee Gees"] == "How Deep Is Your Love") # = ERROR

# print("Han Solo" in dic["jogos"]["Star Wars"]) # = ERROR

# print(func1(dic, ["filmes"], ["musicas"], "Avengers", "Capitão América")) # = ERROR

# print(dic["musicas"][0]["banda"] == "Beatles") # = TRUE

# print(dic["filmes"]["X-men"][3] == "Vampira") # = TRUE

# print("Chewbacca" in dic.filmes.Star Wars) # = ERROR

# print(dic["filmes"]["Star Wars"][2] == "Leia") # = FALSE

# print(func1(dic["filmes"], 1, 2, "Homem de Ferro")) # = naosei

# print("Homem de Ferro" in dic["musicas"][2]) # = FALSE

# print(dic[dic] + dic[dic[dic]]]) # = ERROR

# print("Hey Jude" in dic["musicas"]["Beatles"]) # = ERROR

# print(func1(dic["musicas"], "banda", "nome", "Hey Jude") == "Beatles") = FALSE

# print("Super-homem" in dic["filmes"]["Avengers"]) = FALSE

# print(func1(dic["musicas"], "banda", "nome", "Guns N' Roses") == "November Rain") = TRUE

# print("Thor" in dic["filmes"]["Avengers"]) = TRUE

# print(dic["musicas"][2]["nome"] == "How Deep Is Your Love") = TRUE

# print("November Rain" == dic["musicas"][1]["banda"]) = FALSE

# print("Hey Jude" == dic["musicas"][0]) = FALSE