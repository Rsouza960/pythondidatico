'''
Listas em python
tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i](CRUD)
'''

lista= [10, 20, 30, 40]
'''
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])'''

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
valor_removido = lista.pop(3)
print(lista, 'Removido o', valor_removido)


