# coding=utf-8
import re
import requests
import json

# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
# r = requests.get('https://dle.rae.es/data/search?w=hola', {'Authorization':'Basic cDY4MkpnaFMzOmFHZlVkQ2lFNDM0'})
# headers = {'user-agent': 'my-app/0.0.1'}
headrs = {'Authorization': 'Basic cDY4MkpnaFMzOmFHZlVkQ2lFNDM0', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
# palabras=["calibre","rinoceronte","elefante","caca","kaka","vacuno"]
# palabras=["vacuno","elefante"]
palabras=['elegida']
for palabra in palabras :
    r = requests.get('https://dle.rae.es/data/search?w=' + palabra, headers=headrs)
    print(r.status_code)

    # save response json for word to its own file
    with open("./json/"+palabra + '.json', 'w') as outfile:
        json.dump(r.json(), outfile)

    res = r.json()["res"]
    print res
    # rx = palabra + "[\.\,]]"
    rx = palabra + "[^\w]"
    print rx
    rxp = re.compile(rx)
    # print(palabra + ":" + str(any(i["header"] == palabra + "." for i in r.json()["res"])))
    # print(palabra + ":" + str(any(i["header"] == palabra + "." for i in r.json()["res"])))
    print(palabra + ":" + str(any(rxp.search(i["header"]) for i in res)))

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
