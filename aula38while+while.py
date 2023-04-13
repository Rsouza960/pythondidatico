"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um codigo nao tem fim, será contado enquanto for True
o 'continue', para uma execução e volta o laço de codigos
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1


    linha += 1

print('Acabou')    
