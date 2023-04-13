#exemplo while
'''texto = 'Python'
i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)

    i += 1
'''
'''
senha_salva = '123456'
repeticoes = 0
senha_digitada = ''

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repeticoes infinitas')  
'''  
texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')


text = 'Hello, World'
new_text = ''
for letter in text:
    new_text += f'*{letter}'
    print(letter)
print(new_text)