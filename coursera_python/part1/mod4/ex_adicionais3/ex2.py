n = int(input("Digite um numero inteiro positivo: "))
x = 0
y = 0
sim = True
x = n % 10
n = n // 10
while n > 0 and sim == True:
    y = n % 10
    if x == y:
        print("sim")
        sim = False
    x = y
    n = n // 10
if sim == True:
    print("não")