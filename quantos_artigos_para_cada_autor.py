#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import mincemeat
import glob
import csv

#A tarefa é fazer o cálculo de quantas vezes cada termo (no título da obra) acontece por autor
#agrupar por autor
#para cada termo, encontrado por auto, atribuir 1 ao contador do termo, do autor.
#procurar em cada arquivo do diretório

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

directory = "./data/*";

text_files = glob.glob(directory)

#return a dictionary with filename and file contents
source = dict((file_name, file_contents(file_name)) for file_name in text_files)

#map function for the task: Calculate how many times each term (in the title of the work) happens by author
#data structure: paper-id:::author1::author2::…. ::authorN:::title
#The field separator is ":::" and the authors tab is "::";
#Answer which are the two words that most happen to the following authors:
#a- "Grzegorz Rozenberg"
#b- "Philip S. Yu"

def mapfn(k, v):
        for line in v.splitlines():            
            if "Grzegorz Rozenberg" in line.split(':::')[1]: 
                yield "Grzegorz Rozenberg", 1
            if "Philip S. Yu" in line.split(':::')[1]: 
                yield "Philip S. Yu", 1

                
def reducefn(k, v):
    result = sum(v)
    L = list()
    L.append(result)
    return L


s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("./Ocorrencias.csv","w"))

for k, v in results.items():
        w.writerow([k, v[0]])