"""
Listas em python
Tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, +
"""

#         01234
#        -54321
string = 'ABCDE' #5 CARACTERES (len) 
#print(bool([])) #falsy
#print(lista, type(lista))

#         0     1          2        3   4
#neg     -5    -4         -3       -2  -1
lista = [123, True, 'Renan Souza', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
