n = int(input())
lista = [] 
SumaFeteVizibile=0
SumaTotalaZaruri =n * 21
for x in range(n):
    lista.append(input())
for x in range(len(lista)): 
    for y in range(len(lista[x])): 
        if lista[x][y] != ' ': 
          SumaFeteVizibile= SumaFeteVizibile + int(lista[x][y])
SumaFeteInvizibile = SumaTotalaZaruri -SumaFeteVizibile
print(SumaFeteInvizibile)
