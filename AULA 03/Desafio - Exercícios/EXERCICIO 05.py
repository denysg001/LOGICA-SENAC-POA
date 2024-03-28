 #5. Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa.
 #    Mostrar o conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca. 


va=float(input("Digite Valor va:"))
vb=float(input("Digite Valor vb:"))

x=va
y=vb
va=y
vb=x

aux=va
va=vb
vb=aux

va,vb = vb,va

print (f'va={va}  vb={vb}')