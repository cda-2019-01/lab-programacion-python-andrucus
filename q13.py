##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##

#Punto q13
file = open('data.csv','r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]

data = []
i=0
for registro in file:
    data.append([])
    for e in registro:
        a = e.split(',')
        if (len(a) == 1):
            data[i].append(a[0])
        else:
            data[i].append(a)
    i += 1


resultado = {}

for registro2 in data:
    aux = 0
    for a in registro2[4]:
        aux += int(a.split(':')[1])
    print(registro[0] + ',' + str(aux))