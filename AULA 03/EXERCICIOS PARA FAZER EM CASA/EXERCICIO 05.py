#5. 
# Um círculo de raio 2 é colocando dentro de um retângulo de lados 5 e 7. 
# Faça um programa que informe o tamanho da área do retângulo que não está sendo ocupada pelo círculo.

RAIO_CIRCULO = 2
PI = 3.14
AREA_CIRCULO = PI * (RAIO_CIRCULO ** 2)
PERIMETRO_CIRCULO = (2 * PI) * RAIO_CIRCULO
DIAMETRO_CIRCULO = RAIO_CIRCULO * 2


RETANGULO_LADO_A = 5
RETANGULO_LADO_B = 7

PERIMETRO_RETANGULO = (2 * RETANGULO_LADO_A) +  (2 * RETANGULO_LADO_B)
AREA_RETANGULO = RETANGULO_LADO_A * RETANGULO_LADO_B

AREA_NAO_OCUPADA = AREA_RETANGULO - AREA_CIRCULO

print("O Raio do círculo é: ",RAIO_CIRCULO)
print("A área do círculo é: ",AREA_CIRCULO)
print("O perímetro do círculo é: ",PERIMETRO_CIRCULO)
print("O diâmetro do circulo é: ",DIAMETRO_CIRCULO)

print("\nO lado A do retângulo é: ", RETANGULO_LADO_A)
print("O lado B do retângulo é: ",RETANGULO_LADO_B)
print("A área do retângulo é: ",AREA_RETANGULO)
print("O perímetro do retângulo é:",PERIMETRO_RETANGULO)

print("\nO tamanho da área do retângulo que não esta sendo ocupada é: ",AREA_NAO_OCUPADA)
