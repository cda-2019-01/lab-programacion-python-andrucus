##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

#Punto q03
file = open('data.csv','r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]
data =file

resultado ={}

for registro in data:
    resultado[registro[0]]=0
 
for registro in data:
    resultado[registro[0]]= resultado[registro[0]] + int(registro[1])
    
for key in sorted(resultado):
    print(key + ',' + str(resultado[key]))