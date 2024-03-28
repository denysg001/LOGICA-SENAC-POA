#4. Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média. 

N1 = float(input("Digite o primeiro valor: "))
N2 = float(input("Digite o segundo valor: "))
N3 = float(input("Digite o terceiro valor: "))
N4 = float(input("Digite o quarto valor: "))
N5 = float(input("Digite o quinto valor: "))

TOTAL_SOMA = N1 + N2 + N3 + N4 + N5
MEDIA = TOTAL_SOMA / 5

print(f"\nA soma de {N1} + {N2} + {N3} + {N4} + {N5} é {TOTAL_SOMA: .2f}.\n A média é: {MEDIA: .2f}")