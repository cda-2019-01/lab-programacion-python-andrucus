##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
#Punto q04
file = open('data.csv','r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]
data =file

resultado ={}

for registro in data:
    resultado[registro[2].split('-')[1]]=0
 
for registro in data:
    resultado[registro[2].split('-')[1]]= resultado[registro[2].split('-')[1]] + 1
    
for key in sorted(resultado):
    print(key + ',' + str(resultado[key]))