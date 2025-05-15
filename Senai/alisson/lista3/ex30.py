import math
a = int(input("Digite o valor do primeiro lado: "))
b = int(input("Digite o valor do segundo lado: "))
c = int(input("Digite o valor do terceiro lado: "))
maximo = max(a, b, c)
minimo = min(a, b, c)
meio = a + b + c - maximo - minimo
catetos1 = a + b + c - maximo - minimo
cateto2 = a + b + c - maximo - meio
if maximo <= a + b + c - maximo:
    if maximo**2 == catetos1**2 + cateto2**2:
        print("Os lados formam um triângulo retângulo")
    seno1 = cateto2 / maximo

angulo1 = math.degrees(math.asin(seno1))    
angulo2 = 90 - angulo1
print(f"Os angulos do triângulo são: {angulo1:.2f} , {angulo2:.2f} e 90.00")