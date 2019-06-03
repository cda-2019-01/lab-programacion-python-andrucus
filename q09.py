##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
#Punto q09
file = open('data.csv', 'r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]
data = file

resultado = {}

for elemento in data:
    resultado[elemento[1]]= []
for elemento in data:
    resultado[elemento[1]].append(elemento[0])


resultado2 = {}

for i in sorted(resultado.items()):
    unicos = set(i[1])
    unicos = list(unicos)
    resultado2[i[0]] = sorted(unicos)

for i in sorted(resultado2.items()):
    print (i)