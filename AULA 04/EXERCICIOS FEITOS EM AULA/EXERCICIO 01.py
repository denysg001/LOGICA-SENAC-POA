#Faça um programa que recebe um nome de candidato a motorista
#  e seu ano de nascimento
# , informar se  pode tirar a CNH ou não

NOME = input("Digite seu nome: ")

NASCIMENTO = int(input("Digite o ano de nascimento: "))

from datetime import date

ANO = date.today().year
DIA = date.today().day
MES = date.today().month


IDADE_ATUAL = ANO - NASCIMENTO


if IDADE_ATUAL >= 18:
    print(f"{NOME}, voce pode fazer sua CNH, voce tem {IDADE_ATUAL} anos")

else:
    print(f"{NOME}, você tem {IDADE_ATUAL}anos , falta {18 - IDADE_ATUAL} anos para você poder tirar sua carteira")


    #COMO PEGAR ANO ATUAL DO SISTEMA EM PYTHON


data_atual = date.today()

print(data_atual)

dia = data_atual.day
mes = data_atual.month
ano = data_atual.year

print('{}/{}/{}'.format(dia, mes, ano))