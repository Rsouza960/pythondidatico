"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um codigo nao tem fim
"""
condicao = True 

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break
print('você saiu')