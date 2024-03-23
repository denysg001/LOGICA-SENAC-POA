# Faça um programa que recebe o raio de uma circunferência, calcular a área e o perímetro da mesma.

RAIO = int(input("Digite o raio da Circunferência: "))

print("\nVocê digitou que o Raio é:",RAIO)

pi = 3.14
DIAMETRO = RAIO * 2
AREA = pi * (RAIO ** 2)    # O ** dentro do Parenteses significa exponenciação. EX: RAIO = 3 então é como se fosse 3²
PERIMETRO = (2 * pi) * RAIO

print("\nA Area da Circunferência é:",AREA)
print("O Diâmetro é:",DIAMETRO)
print("O Perímetro é:",PERIMETRO)
