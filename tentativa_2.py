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
    print('selecione uma opção: ')
    opcao = input('[I]inserir, [A]apagar, [L]listar: ')
    
    for i, item in enumerate(lista):
        
            print(i, item)

    if opcao == 'i':
        os.system('cls')
        item = input('digite o item que deseja incluir na lista: ')
        lista.append(item)
    
    elif opcao == 'a':
        for i, item in enumerate(lista):
         print( i, item)
        excluir = input('Qual item deseja excluir?: ')

        try:
           indice = int(excluir)
           del lista[indice]
        except ValueError:
           print('Por favor digite um numero inteiro')
        except IndexError:
           print('Indice não existe na lista')
        except Exception:
           print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
           print('lista vazia')

        for i, item in enumerate(lista):
            print(i, item)    






        


