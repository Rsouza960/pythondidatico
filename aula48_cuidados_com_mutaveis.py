"""
Cuidados com dados mutáveis
= - copiando o valor(imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Renan', 'Marias', 1, True, 2.5]
lista_b = lista_a.copy()

lista_a[0]= 'Qualquer coisa'
print(lista_b)
print(lista_a)