# Faça os programas individuais para calcular os perímetros e as áreas das figuras geométricas abaixo. Alguns programas precisarão de vários valores de entrada

########  ATENÇÃO  #######
# Para melhor compreensão dos das variaveis inseridas nesse exercicio, esteja com o PDF do exercicio aberto para acompanhamento das nomenclaturas através das figuras.
# As formas de execução dos comandos pode variar um pouco ao decorrer de cada figura para demonstrar formas diferentes de chegar no mesmo resultado. 

print("Vamos calcular as formas geométricas do exercicio 4 da segunda aula")

print("\nFigura 1")

A_FIGURA_1 = int(input("\nDigite o valor de A da Figura 1: "))
B_FIGURA_1 = int(input("Digite o valor de B da Figura 1: ")) 
C_FIGURA_1 = int(input("Digite o valor de C da Figura 1: ")) 
H_FIGURA_1 = int(input("Digite o valor de H da Figura 1: "))

PERIMETRO_FIGURA_1 = A_FIGURA_1 + B_FIGURA_1 + C_FIGURA_1
AREA_FIGURA_1 = (B_FIGURA_1 * H_FIGURA_1) / 2

print("\nPerímetro Figura 1:",PERIMETRO_FIGURA_1,"\nAŕea Figura 1:",AREA_FIGURA_1)









print("\n\n\nFigura 2 - QUADRADO")

LADO_FIGURA_2 = int(input("\nDigite o Valor de um lado do quadrado:"))
print("\nVocê definiu o lado do quadrado como",LADO_FIGURA_2)

PERIMETRO_FIGURA_2 = LADO_FIGURA_2 *4
AREA_FIGURA_2 = LADO_FIGURA_2 ** 2

print("\nPerímetro da figura 2 - QUADRADO é:",PERIMETRO_FIGURA_2,"\nÁrea:",AREA_FIGURA_2)









print("\n\n\nFigura 3 - RETANGULO")

A_FIGURA_3 = int(input("\nDigite o Valor de A do Retangulo:"))
B_FIGURA_3 = int(input("Digite o Valor de B do Retangulo:"))
print("\nVocê definiu que o Valor de A do Retangulo é:",A_FIGURA_3,"e o valor de B é:",B_FIGURA_3)

PERIMETRO_FIGURA_3 = (A_FIGURA_3 * 2) + (B_FIGURA_3 * 2)
AREA_FIGURA_3 = A_FIGURA_3 * B_FIGURA_3

print("\nPerimetro da Figura 3 - Retangulo:",PERIMETRO_FIGURA_3," - Área:",AREA_FIGURA_3)









print("\n\n\nFigura 4")

A_FIGURA_4 = int(input("\nDigite o valor de A da figura 4:"))
B_FIGURA_4 = int(input("\nDigite o valor de B da figura 4:"))
H_FIGURA_4 = int(input("\nDigite o valor de H da figura 4:"))

PERIMETRO_FIGURA_4 = (A_FIGURA_4 * 2) + (B_FIGURA_4 *2)
AREA_FIGURA_4 = A_FIGURA_4 * H_FIGURA_4

print("\nPerímetro Figura 4:",PERIMETRO_FIGURA_4)
print("Área Figura 4:",AREA_FIGURA_4)









print("\n\n\nFigura 5")

D1_FIGURA_5 = int(input("\nDigite o valor de D da figura 5:"))
D2_FIGURA_5 = int(input("Digite o valor de d da figura 5:"))
L_FIGURA_5 = int(input("Digite o valor de L da figura 5:"))

print("\nVocê difiniu o valor de D maiusculo como:",D1_FIGURA_5)
print("Você difiniu o valor de d minusculo como:",D2_FIGURA_5)
print("Você difiniu o valor de L como:",L_FIGURA_5)

PERIMETRO_FIGURA_5 = L_FIGURA_5 * 4
AREA_FIGURA_5 = (D1_FIGURA_5 * D2_FIGURA_5) / 2

print("\nPerimetro da Figura 5:",PERIMETRO_FIGURA_5)
print("Área da Figura 5:",AREA_FIGURA_5)









print("\n\n\nFigura 6")

A_FIGURA_6 = int(input("\nDigite o valor de A da figura 6:"))
B1_FIGURA_6 = int(input("Digite o valor de B maiusculo da figura 6:"))
B2_FIGURA_6 = int(input("Digite o valor de b minusculo da figura 6:"))
C_FIGURA_6 = int(input("Digite o valor de C da figura 6:"))
H_FIGURA_6 = int(input("Digite o valor de H da figura 6:"))

PERIMETRO_FIGURA_6 = A_FIGURA_6 + B1_FIGURA_6 + B2_FIGURA_6 + C_FIGURA_6
AREA_FIGURA_6 = ((B1_FIGURA_6 + B2_FIGURA_6) / 2) * H_FIGURA_6

print("\nPerimetro da Figura 6:",PERIMETRO_FIGURA_6)
print("Área da Figura 6:",AREA_FIGURA_6)

print("\nFim!")









print("\n\n\nFigura 7")

R_FIGURA_7 = int(input("Digite o raio da Circunferência: "))

print("\nVocê digitou que o Raio é:",R_FIGURA_7)

pi = 3.14
DIAMETRO = R_FIGURA_7 * 2
AREA = pi * (R_FIGURA_7 ** 2)    # O ** dentro do Parenteses significa exponenciação. EX: RAIO = 3 então é como se fosse 3²
PERIMETRO = (2 * pi) * R_FIGURA_7

print("\nA Area da Circunferência é:",AREA)
print("O Diâmetro é:",DIAMETRO)
print("O Perímetro é:",PERIMETRO)

print("\nFIM!")