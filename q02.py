##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

#Punto q02
file = open('data.csv','r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]
data =file

resultado ={}
for registro in data:
    resultado[registro[0]]=0
 
for registro in data:
    resultado[registro[0]]= resultado[registro[0]] + 1
    
for key in sorted(resultado):
    print(key + ',' + str(resultado[key]))