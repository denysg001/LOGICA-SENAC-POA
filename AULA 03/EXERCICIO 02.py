# 2. Faça um programa que leia 3 valores e mostre a soma de seus inversos. 

print("Faça um programa que leia 3 valores e mostre a soma de seus inversos")

VALOR1 = int(input("\nDigite o valor 1:"))
VALOR2 = int(input("Digite o valor 2:"))
VALOR3 = int(input("Digite o valor 3:"))

INVERSO_VALOR1 = 1 / VALOR1
INVERSO_VALOR2 = 1 / VALOR2
INVERSO_VALOR3 = 1 / VALOR3

print("\nInverso de ",+VALOR1,INVERSO_VALOR1)
print("Inverso de ",+VALOR2,INVERSO_VALOR2)
print("Inverso de ",+VALOR2,INVERSO_VALOR3)


VALORES_INVERSOS_SOMADOS = INVERSO_VALOR1 + INVERSO_VALOR2 + INVERSO_VALOR3

print("\nA soma do inverso dos 3 valores é:",VALORES_INVERSOS_SOMADOS)
