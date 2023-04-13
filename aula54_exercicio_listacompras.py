"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    print('selecione uma opção')
    opcao = input('[i]inserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Qual item deseja inserir: ')
        lista.append(valor)


    elif opcao == 'a':
        for i, valor in enumerate(lista):
            print(i, valor)
        indice_str = input( 'Escolha o indice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um numero inteiro')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system ('cls')

        if len(lista) == 0:
            print('Nada para listas')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha entre "i" para inserir, "a" para apagar ou "l" para listar.')    
    