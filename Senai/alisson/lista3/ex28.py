a = int(input("Digite o valor do primeiro lado: "))
b = int(input("Digite o valor do segundo lado: "))
c = int(input("Digite o valor do terceiro lado: "))
maximo = max(a, b, c)
if maximo >= a + b + c - maximo:
    print("Os lados não formam um triângulo")
else:
    print("Os lados formam um triângulo")