##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##

#Punto q05
file = open('data.csv','r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]
data =file

resultado ={}


for registro in data:
	resultado[registro[0]] = []

for registro in data:
	resultado[registro[0]].append(int(registro[1]))

for key in sorted(resultado.keys()):
    print(key + ','+ str(max(resultado[key])) + ',' + str(min(resultado[key])))