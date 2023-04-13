"""
Iterável -> str, range, etc (__iter__)
Iterador -> Quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
texto = 'Renan' # iteravel

#iterador = iter(texto)  #iterator

#while True:
#   try:
#       letra = next(iteratador)
#       print(letra)
#   except StopInteration:
#       break

for letra in texto:
    print(letra)