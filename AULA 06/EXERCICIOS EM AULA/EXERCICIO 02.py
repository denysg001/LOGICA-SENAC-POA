SENHA = input("Digite a senha: ")

contador=1

while SENHA != ("SenhaCorreta"):
    print("Senha invalida")
    if contador >=3:
        print(f"tentativa {contador} / 3")
        print("Programa encerrado")
        break
        
    print(f"tentativa {contador} / 3")
    contador+=1
    SENHA = input("Digite a senha: ")

else:
    

    print("senha OK")