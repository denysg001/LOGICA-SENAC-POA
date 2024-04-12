"""Faça um programa que leia um mumero não determinado de nomes de alunos e suas duas notas.
Calcular sua média aritimética e informar se >= 7
"""

NOME = input("Digite seu nome: ")

while NOME.upper() != "FIM": #.upper vai sempre converter tudo pra MAIUSCULO
    NOTA01 = float(input("Digite sua primeira nota "))
    NOTA02 = float(input("Digite sua segunda nota "))
    
    RESULTADO = (NOTA01 + NOTA02) / 2

    if RESULTADO >= 7:
        print(F"{NOME}, Você esta aprovado com a média: {RESULTADO}")
    else:
        print(f"{NOME}, você esta reprovado, sua média é: {RESULTADO}")

    NOME = input("Digite seu nome: ")
else:
    print("Programa encerrado!")