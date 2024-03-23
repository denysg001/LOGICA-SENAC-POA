# 6. 
# Faça um programa que lê um valor em reais
#  e calcule o valor equivalente em dólares. 
# O usuário deve informar, 
# além do valor em reais da compra, 
# o valor da cotação do dólar. 


VALOR_REAIS = float(input("Digite o valor em R$: "))
COTACAO_DOLAR = float(input("Digite a cotação do dolar atual $:"))

VALOR_COMPRA_DOLAR = VALOR_REAIS / COTACAO_DOLAR

print("\nO valor em reais digitado é R$:",VALOR_REAIS)
print("A cotação do dolar atual é $:",COTACAO_DOLAR)

print("\nO Valor de R$:",VALOR_REAIS," em dolares é $:",VALOR_COMPRA_DOLAR)
