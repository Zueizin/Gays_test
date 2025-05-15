valor_da_compra = float(input("Digite o valor da compra: "))
if valor_da_compra < 10:
    valor_da_venda = valor_da_compra * 1.7
elif valor_da_compra < 30:
    valor_da_venda = valor_da_compra * 1.5
elif valor_da_compra < 50:
    valor_da_venda = valor_da_compra * 1.4
else:
    valor_da_venda = valor_da_compra * 1.3
print(f"Valor da venda: {valor_da_venda:.2f}")