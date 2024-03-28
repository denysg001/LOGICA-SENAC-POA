# 3. Ler três valores numéricos e escrever a média aritmética. 

N1 = float(input("Digite o primeiro valor: "))
N2 = float(input("Digite o segundo valor: "))
N3 = float(input("Digite o terceiro valor: "))


MEDIA = (N1 + N2 + N3) / 3

print(f"O valor da Média é {Media: .2f}")
print(f"O valor da Média é {round((N1 + N2 + N3) / 3,2)}")