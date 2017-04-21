# coding=utf-8
import re
import requests
import json
import ast

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
    return ',' in s

# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
# r = requests.get('https://dle.rae.es/data/search?w=hola', {'Authorization':'Basic cDY4MkpnaFMzOmFHZlVkQ2lFNDM0'})
# headers = {'user-agent': 'my-app/0.0.1'}
headrs = {'Authorization': 'Basic cDY4MkpnaFMzOmFHZlVkQ2lFNDM0', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
# palabras=["calibre","rinoceronte","elefante","caca","kaka","vacuno"]
# palabras=["vacuno","elefante"]
palabras=['peste']
for palabra in palabras :
    r = requests.get('https://dle.rae.es/data/search?w=' + palabra, headers=headrs)
    print(r.status_code)

    # save response json for word to its own file
    # with open("./json/"+palabra + '.json', 'w') as outfile:
    #     json.dump(r.json(), outfile)

    res = r.json()["res"]
    print res
    # rx = palabra + "[\.\,]]"
    rx = palabra + "[^\w]"
    print rx
    rxp = re.compile(rx)
    headers=[]
    for i in res :
        header = str(i['header']).rstrip('.')
        headers += [header] if not tieneTerminaciones(header) else generos(header)
    # print(palabra + ":" + str(any(rxp.search(i["header"]) for i in res)))
    print headers
    existe = palabra in headers
    print "la palabra '{}' {} existe".format(palabra,"NO"if not existe else "-")


    # save response json for word to its own file
    with open("./json/"+palabra + '.json', 'w') as outfile:
        # print "{{'{}':{}}}".format(palabra,existe)
        # outfile.write("{{"{}":{}}}".format(palabra,existe))
        json.dump({palabra:existe},outfile);
        # ":{}}}".format(palabra, existe))
        #     (r.json(), outfile)
        outfile.close()

