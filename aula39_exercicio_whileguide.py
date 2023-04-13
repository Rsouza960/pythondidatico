"""
Iterando strings com while
"""
#       012345678910
nome = 'Renan Souza' #strings sao iteraveis
#     1110987654321 negativos

tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)


nome2 = 'Eleusine Souza'
tamanho_nome2 = len(nome2)
indice2 = 0
while indice2 < len(nome2):
    letra2 = nome2[indice2]
    novo_nome2 += f'*{letra2}'
    indice2 += 1
print(novo_nome2)