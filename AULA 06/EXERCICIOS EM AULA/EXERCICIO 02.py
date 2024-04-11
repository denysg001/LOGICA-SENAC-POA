SENHA = input("Digite a senha: ")   #Esta digitando tua senha

contador=1  #Contador começa em 1

while SENHA != ("SenhaCorreta"): #enquanto a senha for diferente de SenhaCorreta, ele vai executar os comandos dentro da identação
    print("Senha invalida") #Esta monstrando na tela "Senha invalida"
    if contador >=3:    #Esta fazendo uma pergunta se o contador é igual ou maior que 3 - Caso seja, vai executar as linhas abaixo.
        print(f"tentativa {contador} / 3")  # Esta fazendo um print da quantidade de tentativa das senhas digitadas
        print("Programa encerrado") #
        break
        
    print(f"tentativa {contador} / 3")
    contador+=1
    SENHA = input("Digite a senha: ")

else:
    

    print("senha OK")