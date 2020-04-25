import os
import json

path = "./pictogramas/"
repoimgpath="https://raw.githubusercontent.com/teabreaktime/pictogramas/master/pictogramas/"

categories=os.listdir(path)
pictograms={}
for c in categories:
    pictograms[c.replace('.png','')]=repoimgpath+c

with open('pictogramas.json', 'w') as outfile:
    json.dump(pictograms, outfile)
    
