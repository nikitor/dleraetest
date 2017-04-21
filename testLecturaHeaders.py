# coding=utf-8
import re
import requests
import json

# función que devuelve el set de palabras generadas,
# tomando en cuenta las posibles terminaciones de género
#
# Ejemplo:
#
# >>> generos('elegido, da.')
# ['elegido', 'elegida']

def generos(s) :
    t = s.rpartition(', ')
    return [t[0], t[0][0:t[0].rfind(t[2][0])] + t[2].rstrip('.')]

# si tiene coma, tiene terminaciones de genero, y devuelve True
def tieneTerminaciones(s) :
    pass
return ',' in s


s={"res": [{"header": "elegido, da.", "id": "EWZi1xA", "grp": 0}, {"header": "elegir.", "id": "EWh6Yvv", "grp": 1}], "approx": 0}

# for palabra in palabras :
#     r = requests.get('https://dle.rae.es/data/search?w=' + palabra, headers=headrs)
#     print(r.status_code)

a=[]
for i in s['res']:
    a += generos(i["header"]) if tieneTerminaciones(i["header"]) else [i["header"].rstrip(".")]
    # a.append(generos(i["header"]) if tieneTerminaciones(i["header"]) else i["header"])
    # a.append(i["header"])
print a



