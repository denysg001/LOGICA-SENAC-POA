#2 - Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menor do que sete;
#   A mensagem "Aprovado com Distinção", se a média for igual a dez.

NOTA01 = float(input("Digite a primeira nota: "))
NOTA02 = float(input("Digite a segunda nota: "))

MEDIA = (NOTA01 + NOTA02) / 2

if MEDIA >= 7 and MEDIA < 10:
    print(f"Você esta aprovado, sua nota é {MEDIA}")

elif MEDIA == 10:
    print(f"Você esta aprovado com Distinção, sua média é {MEDIA}")

else:
    print(f"Voce esta Reprovado, sua media foi de {MEDIA}")

