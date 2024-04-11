contador = 0
while(contador <= 5):
    print(contador)
    contador+= 1
else:
    print(f"\nA contagem terminou!")
print(f"\nFIM!")


contador = 0
while(contador <= 5):
    print(contador)
    contador+= 1
    if contador == 16:
        break   #Encerra o programa sem terminar 
else:
    print(f"\nA contagem terminou!")
print(f"\nFIM!")