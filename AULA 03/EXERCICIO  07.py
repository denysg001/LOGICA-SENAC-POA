#7. 
# Escreva uma expressão lógica 
# que seja verdadeira no caso do valor lido do teclado estar compreendido entre 10 e 50. 
# O programa deve imprimir na tela o resultado da expressão lógica (True ou False). 


VALOR = int(input("Digite um valor: "))

if VALOR <= 50 and VALOR >= 10:
    print("True")
else:
    print("False")
