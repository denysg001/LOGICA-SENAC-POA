# 3. 
# Faça um programa que leia dois valores x e y. 
# O programa deve trocar os valores lidos, 
# de forma que, ao final, 
# x contenha o valor que foi inicialmente atribuído em y, 
# e y contenha o valor que foi inicialmente atribuído a x. 
# Imprima os valores de x e y logo após a leitura, 
# e depois imprima novamente após a troca. 

print(" 3. Faça um programa que leia dois valores x e y. \nO programa deve trocar os valores lidos, \nde forma que, ao final, \nx contenha o valor que foi inicialmente atribuído em y, \ne y contenha o valor que foi inicialmente atribuído a x. \nImprima os valores de x e y logo após a leitura, \ne depois imprima novamente após a troca. ")

X = int(input("\nDigite o valor de X: "))
Y = int(input("Digite o valor de Y: "))

X1 = X
Y1 = Y

print("\nVocê definiu o valor de X como",+X)
print("Você definiu o valor de X como",+Y)

X = Y1
Y = X1

print("\nApós a conversão, X virou:",X)
print("Após a conversão, Y virou:",Y)

