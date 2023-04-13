'''
Exercicio
exiba os indices da lista
0 Maria
1 Helena
2 Renan
'''

lista = ['Maria', 'Helena', 'Renan']
indices = range(len(lista))
print(indices)

for indice in indices:
    print(indice, lista[indice] )