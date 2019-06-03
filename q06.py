##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
#Punto q06
file = open('data.csv', 'r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]

data = []
i = 0
for registro in file:
	data.append([])
	for e in registro:
		a = e.split(',')
		if(len(a) == 1):
			data[i].append(a[0])
		else:
			data[i].append(a)
	i += 1

resultado = {}

for registro2 in data:
	for el in registro2[4]:
		aux = el.split(':')
		resultado[aux[0]] = []

for registro2 in data:
	for el in registro2[4]:
		aux = el.split(':')
		resultado[aux[0]].append(int(aux[1]))

for key in sorted(resultado.keys()):  
     print(key + ',' + str(min(resultado[key])) + ',' + str(max(resultado[key])))