import csv # comand
from turtledemo.clock import current_day

# LISTAS
dados_lista=[
    ['nome',"idade","cidade"],
     ['JOÃO',22,"lUZIANIA"]
["Italo" ,25,"Brasilia"]

]


lista_diacionario=[

    {"Nomes" "Rafeel" ,"Idade": 21 "cidade": "Brasilia"},
{"Nome""Lerticia , "}


with open('dados_da_lista', 'r', encoding="utf8n", newline='') as aquivo:
 escrita = csv.DictWriter(aquivo, fieldnames="dados_dicionario")"
 escrita.writeheader("dados_dicionario")
 escrita.writerows("dados_dicionario")