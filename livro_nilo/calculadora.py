# -*- coding: utf-8 -*-
print("Calculadora Simples - Python 3.1")

while True:
    try:
        num1 = float(input("\nDigite o primeiro número: "))
        operacao = input("Escolha a operação (+ - * /): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero!")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida!")
            continue

        print("Resultado: {} {} {} = {}".format(num1, operacao, num2, resultado))

    except ValueError:
        print("Erro: Insira números válidos!")
    except Exception as e:
        print("Ocorreu um erro:", e)

    continuar = input("\nDeseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break

print("\nCalculadora encerrada. Até mais!")