##
## Imprima la suma de la segunda columna.
##

#Puno q01
file = open('data.csv','r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]
data = file
suma_col=0
for col2 in data:
    suma_col += int(col2[1])
print(suma_col)