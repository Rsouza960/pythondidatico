"""
Lista de listas e seus indices
"""

salas = [
    # 0        1
    ['Maria', 'Helena', ],  #indice 0
    # 0
    ['Elaine', ],  #indice 1
    # 0       1       2        
    ['Luiz', 'João', 'Eduarda', ],  #indice 2
]

#print(salas[1][0])
#print(salas[0][1])
#print(salas[2][2])
#print(salas[2][3][2])


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

