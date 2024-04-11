'''
3. Imprimindo Números em Intervalo Personalizado:
Crie um programa que peça ao usuário dois números como entrada e imprima todos os números ímpares no intervalo especificado (inclusive).

'''

numero1 = int(input('Número Inicial: '))
numero2 = int(input('Número Final: '))
numero2+=1

for i in range(numero1, numero2, 1):
    if i%2 != 0:
        print(i)


        '''
3. Imprimindo Números em Intervalo Personalizado:
Crie um programa que peça ao usuário dois números como entrada e imprima todos os números pares no intervalo especificado (inclusive).

'''

numero1 = int(input('Número Inicial: '))
numero2 = int(input('Número Final: '))
numero2+=1

for i in range(numero1, numero2, 1):
    if i%2 == 0:
        print(i)