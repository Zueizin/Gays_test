# Solicita ao usuário que insira um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é válido
if n <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Imprime os n primeiros números ímpares
    print(f"Os {n} primeiros números ímpares são:")
    for i in range(1, 2 * n, 2):
        print(i, end=" ")
    print()  # Para pular uma linha após a impressão