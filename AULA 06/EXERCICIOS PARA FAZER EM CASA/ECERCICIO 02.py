
'''Calculadora Simples com if-elif-else: 
Crie um programa que simule uma calculadora. 
Peça ao usuário que escolha uma operação (soma, subtração, multiplicação ou divisão) e, 
em seguida, solicite dois números. 
Realize a operação escolhida e mostre o resultado.'''

OPCAO = int(input("Escolha uma operação: \n1 - SOMA \n2 - SUBTRAÇÃO \n3 - DIVISÃO \n4 - MULTIPLICAÇÃO \nEscolha a opção desejada:  "))

while OPCAO:
    OPERACAO = [1 , 2 , 3 , 4]
    while True:
        try:
            NUMERO_1 = int(input("\nDigite o primeiro numero:"))
            NUMERO_2 = int(input("\nDigite o segundo numero: "))  
            break
        except:
            print("\nValor deve ser inteiro")

    if OPCAO == OPERACAO[0]:
        RESULTADO = NUMERO_1 + NUMERO_2
        print(f'O Resultado da soma de {NUMERO_1} com {NUMERO_2} é: {RESULTADO}')
        
    elif OPCAO == OPERACAO[1]:
        RESULTADO = NUMERO_1 - NUMERO_2
        print(f'O Resultado da subtração de {NUMERO_1} com {NUMERO_2} é: {RESULTADO}')
        
    elif OPCAO == OPERACAO[2]:
        RESULTADO = NUMERO_1 / NUMERO_2
        print(f'O Resultado da divisão de {NUMERO_1} com {NUMERO_2} é: {RESULTADO}')
        

    elif OPCAO == OPERACAO[3]:
        RESULTADO = NUMERO_1 * NUMERO_2
        print(f'O Resultado da multiplicação de {NUMERO_1} com {NUMERO_2} é: {RESULTADO}')
    
    else:
        print()

print("\nVocê não digitou nenhuma opção, fim do programa")
