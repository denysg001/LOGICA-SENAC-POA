'''
8. Encontrando o Menor Número em uma Lista:
Crie um programa que encontre o menor número em uma lista de números.

'''

lista = []

for numero in range(1,11):
    numero_usuario = float(input('Digite um número: '))
    lista.append(numero_usuario)
    print(lista)
    for menor_numero in lista:
        menor = min(lista)
print(f'O menor número da lista é: {menor}')