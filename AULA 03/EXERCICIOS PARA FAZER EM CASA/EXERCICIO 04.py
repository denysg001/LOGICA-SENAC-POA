#4. 
# Faça um programa que lê o nome de um produto
# a quantidade comprada
# o valor unitário
# e o percentual de desconto a ser aplicado para o pagamento. 
# Imprima na tela o nome do produto 
# e o valor total da venda. 

NOME_PRODUTO = input("Digite o nome do produto: ")
QUANTIDADE_PRODUTO = int(input("Digite a quantidade de "+NOME_PRODUTO+" que você esta comprando: "))
VALOR_UNITARIO = float(input("Digite o valor unítario de "+NOME_PRODUTO+" em R$: "))
PERCENTUAL_DESCONTO_PRODUTO = int(input("Digite o Percentual de Desconto de "+NOME_PRODUTO+" em porcentagem: "))

VALOR_TOTAL = QUANTIDADE_PRODUTO * VALOR_UNITARIO
VALOR_DO_DESCONTO = (PERCENTUAL_DESCONTO_PRODUTO * VALOR_TOTAL) / 100
VALOR_TOTAL_COM_DESCONTO = VALOR_TOTAL - VALOR_DO_DESCONTO

print("\nVocê comprou:",NOME_PRODUTO)
print("A quantidade foi:",QUANTIDADE_PRODUTO)
print("O valor unítario é R$:",VALOR_UNITARIO)
print("A porcentagem de desconto é de:",PERCENTUAL_DESCONTO_PRODUTO,"%")

print("\nO Valor total sem desconto é R$",VALOR_TOTAL)
print("O valor do desconto é de R$: ",VALOR_DO_DESCONTO)
print("O Valor total com desconto é: ",VALOR_TOTAL_COM_DESCONTO)
