'''**Tabuada de Multiplicar:**
Faça um programa que calcule um número não determinado de tabuadas. O programa deve pedir para o usuário 
digitar um número inteiro e, em seguida, imprima a tabela de multiplicação para esse número de 1 a 10.
Por exemplo, se o usuário digitar 3, o programa deve imprimir a tabuada de multiplicar de 3.
Encerrar o programa quando o usuário digitar um numero <=0 
'''

NUMERO_DIGITADO = int(input("Digite um numero de qualquer valor acima de 0 para exibir a tabuada do numero correspondente, Digite 0 para sair: "))

while NUMERO_DIGITADO != 0:
    print(f"O numero digitado foi: {NUMERO_DIGITADO}, exibindo a tabuada do: {NUMERO_DIGITADO} \n")
    for i in range(1,11,1):
        print(i * NUMERO_DIGITADO)
    
    NUMERO_DIGITADO = int(input("DIGITE UM NUMERO: "))

else:
    print(f"Você digitou 0, Fim do programa!")