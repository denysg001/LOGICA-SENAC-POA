'''
Verificação de Número Primo com Loop For e if: Escreva um programa que solicite um número ao usuário e determine se esse número é primo ou não, usando um loop for e uma estrutura if.
'''

while True:
   while True:
      try:
         numero = int(input('Digite um número maior que 1: '))
         break
      except:
          print('Apenas números inteiros!')
   if numero == 0:
      print('Programa Encerrado!')
      break
   primo = True 
   for n in range(2, numero):
        print(n)
        if numero % n == 0: 
            print(f'{n} achou divisor')
            primo = False
        else:
           print(f'{n} é primo')
   if primo:
       print(f'{n} é primo')
   else:
       print(f'{n} não é primo')