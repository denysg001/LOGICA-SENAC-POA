a1 = float(input("digite a aresta 1 do triangulo: "))
a2 = float(input("digite a aresta 2 do triangulo: "))
a3 = float(input("digite a aresta 3 do triangulo: "))

p1 = a1 + a2 + a3 

print("\nPerimetro do triangulo 1 é: ", p1)

b1 = float(input("\ndigite a aresta 1 do triangulo: "))
b2 = float(input("digite a aresta 2 do triangulo: "))
b3 = float(input("digite a aresta 3 do triangulo: "))

p2 = b1 + b2 + b3 

print("\nPerimetro do triangulo 2 é: ", p2)

if p1 > p2:
    print("\nTriangulo 1 é maior!")

else:
    print("\nTriangulo 2 é maior!")
