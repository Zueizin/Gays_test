a = float(input("Valor A: "))
b = float(input("Valor B: "))
c = float(input("Valor C: "))
menor = min(a, b, c)
maior = max(a, b, c)
meio = (a + b + c) - menor - maior  
print(f"Ordem decrescente: {maior}, {meio}, {menor}")