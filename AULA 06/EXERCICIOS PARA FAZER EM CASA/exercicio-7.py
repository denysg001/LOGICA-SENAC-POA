'''
Adivinhe o Número com Loop While e if: Implemente um jogo em que o programa gera um número aleatório entre 1 e 100, e o usuário tenta adivinhá-lo. O programa deve fornecer dicas ("maior" ou "menor") até que o usuário adivinhe o número correto, usando um loop while e comandos if.
'''

import random

x = random.random()
y = int(x*100)
numero_usuario = int(input('Escolha um número entre 1 e 100: '))

while numero_usuario != y:
    if numero_usuario > y:
        print('Maior')
    else:
        print('Menor')   
     
    numero_usuario = int(input('Escolha um número entre 1 e 100: '))
else:
    print(f'Número: {y}')
    print(f'Número digitado: {numero_usuario}')
    print('Acertou!')
    
