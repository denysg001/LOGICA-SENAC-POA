'''
Contagem Regressiva com Loop While: Crie um programa que inicie em 10 e conte regressivamente até 1 usando um loop while. Após a contagem, exiba uma mensagem, por exemplo, "Foguete lançado!".
'''

contador = 10
while contador > -1:
    print(contador)
    contador -= 1
print('Finalizada contagem!')

#############################
# Loop For
for i in range(10, -1, -1):
    print(i)
print('Finalizada contagem regressiva!')