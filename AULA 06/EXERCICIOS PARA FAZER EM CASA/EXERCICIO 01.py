'''Programa de Contagem com Loop For: 
Escreva um programa que solicite ao usuário um número e, 
em seguida, use um loop for para contar de 1 até esse número, 
exibindo cada número no processo.
'''

NUMERO = int(input("Digite um numero: "))
NUMERO += 1
for i in range(NUMERO):
    print(i)