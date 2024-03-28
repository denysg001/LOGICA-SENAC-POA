# Faça um programa que transforme uma temperatura fornecida em Celsius para a correspondente em Fahrenheit 
# e receba  uma temperatura fornecida em Fahrenheit  para a correspondente em Celcius. 

# Fahrenheit para Celsius - (°F - 32) x 5/9 =°C
# Celsius para Fahrenheit - (°C x 9/5) + 32 =°F

print("Celsius para Fahrenhiet")

TEMPERATURA_C = int(input("\nDigite a temperatura em Celsius que você deseja converter para Fahrenheit:"))
print("\nVocê definiu a temperatura como:",TEMPERATURA_C)

FAHRENHEIT = (TEMPERATURA_C * 9/5) + 32

print("\nA temperatura em Fahrenheit é:",FAHRENHEIT)



print("\n\n\nFahrenhiet para Celsius:")

TEMPERATURA_F = int(input("\nDigite a temperatura em Fahrenhiet que você deseja converter para Celsius:"))
print("\nVocê definiu a temperatura como:",TEMPERATURA_F)

CELSIUS = (TEMPERATURA_F -32) * 5/9

print("\nA temperatura em Fahrenheit é:",CELSIUS)
