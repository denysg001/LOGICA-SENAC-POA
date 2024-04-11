from datetime import date

ANO = date.today().year
DIA = date.today().day
MES = date.today().month

NOME = input("Digite seu nome: ")

while NOME.upper != "FIM": #.upper vai sempre converter tudo pra MAIUSCULO
    Ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    idade = ANO - Ano_nascimento
    print(f"{NOME} tem {idade}, nasceu em {Ano_nascimento}")
    
    NOME = input("\nDigite seu nome: ")

else:
    print("Programa encerrado!")