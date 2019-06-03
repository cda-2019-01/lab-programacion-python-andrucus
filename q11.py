##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
#Punto q11
file = open('data.csv','r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]

data =[]
i = 0

for registro in file:
    data.append([])
    for e in registro:
        a = e.split(',')
        if (len(a) == 1):
            data[i].append(a[0])
        else:
            data[i].append(a)
    i +=1

for registro2 in data:
    print(registro2[0] + ',' + str(len(registro2[3])) + ',' + str(len(registro2[4])))