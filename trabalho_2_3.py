import mincemeat
import glob
import csv

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

text_files = glob.glob("C:\\Temp\\arq.exerc\\join\\*")

source = dict((file_name, file_contents(file_name)) for file_name in text_files)

def mapfn(k, v):
        print 'map ' + k        
        for line in v.splitlines():
                if k == 'C:\\Temp\\arq.exerc\\join\\2.2-vendas.csv':
                    yield line.split(';')[0], 'V' + ':' + line.split(';')[5]
                if k == 'C:\\Temp\\arq.exerc\\join\\2.2-filiais.csv':
                    yield line.split(';')[0], 'F' + ':' + line.split(';')[1]

def reducefn(k, v):
    print 'reduce' + k
    total = 0
    for index, item in enumerate(v):
        if item.split(":")[0] == 'V':
            total = int(item.split(":")[1]) + total
        if item.split(":")[0] == 'F':
            NomeFilial = item.split(":")[1]
    L = list()
    L.append(NomeFilial + " , " + str(total))
    return L

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("C:\\Temp\\arq.exerc\\Result.csv","w"), delimiter=';', lineterminator="\r")
for k, v in results.items():
        w.writerow([k, v])