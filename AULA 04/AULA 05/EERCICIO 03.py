''' 3. Imprimindo Números em Intervalo Personalizado:
Crie um programa que peça ao usuário dois números como entrada e imprima todos os números ímpares no intervalo especificado (inclusive).
 '''

NUMERO_01 = int(input("Digite o primeiro numero: "))
NUMERO_02 = int(input("Digite o segundo numero: "))
NUMERO_02+= 1

for i in range(NUMERO_01, NUMERO_02, 1):
    if i%2 != 0:
        print(i)
