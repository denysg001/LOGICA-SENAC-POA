#Faça um programa que recebe o lado de um quadrado, calcular a área e o perímetro do mesmo.

LADO1 = int(input("DIGITE O TAMANHO DE UM LADO DO QUADRADO: "))

AREA = LADO1 ** 2    # O ** dentro do Parenteses significa exponenciação. EX: LADO1 = 3 então é como se fosse 3²
PERIMETRO = LADO1 *4

print("\nA área do quadrado é:",AREA,"e o Perímetro do quadrado é:",PERIMETRO)
print("\nFim!")
