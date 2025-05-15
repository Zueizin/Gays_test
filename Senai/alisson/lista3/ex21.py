saldo_medio = float(input("Digite o saldo médio do último ano (R$): "))
if saldo_medio <= 500:
    credito = 0
elif saldo_medio <= 1000:
    credito = saldo_medio * 0.30
elif saldo_medio <= 3000:
    credito = saldo_medio * 0.40
else:
    credito = saldo_medio * 0.50
credito_com_juros = credito * 0.98
print(f"\nSaldo médio: R$ {saldo_medio:.2f}")
print(f"Valor do crédito antes dos juros: R$ {credito:.2f}")
print(f"Valor do crédito com juros (2%): R$ {credito_com_juros:.2f}")