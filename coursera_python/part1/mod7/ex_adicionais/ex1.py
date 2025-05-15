def eh_primo(num):
    if num < 2:
        return False
    divisor = 2
    while divisor <= num ** 0.5:
        if num % divisor == 0:
            return False
        divisor += 1
    return True
def n_primos(n):
    if n < 2:
        return 0
    contador = 0
    num = 2
    while num <= n:
        if eh_primo(num):
            contador += 1
        num += 1
    return contador
print("Contador de números primos")
print("-------------------------")
while True:
    
    n = int(input("Digite um número inteiro maior ou igual a 2 (ou 0 para sair): "))
        
    if n == 0:
        print("Encerrando o programa...")
        break
            
    if n < 2:
        print("Por favor, digite um número maior ou igual a 2.")
        continue
            
    quantidade = n_primos(n)
    print(f"Existem {quantidade} números primos entre 2 e {n}.")
    