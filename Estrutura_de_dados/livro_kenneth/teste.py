import math

# Função para calcular as propriedades da esfera
def calcular_esfera(raio):
    # Diâmetro da esfera
    diametro = 2 * raio

    # Circunferência da esfera
    circunferencia = 2 * math.pi * raio

    # Área da superfície da esfera
    area_superficie = 4 * math.pi * raio**2

    # Volume da esfera
    volume = (4/3) * math.pi * raio**3

    return diametro, circunferencia, area_superficie, volume

# Entrada do usuário
raio = float(input("Digite o raio da esfera: "))

# Cálculos
diametro, circunferencia, area_superficie, volume = calcular_esfera(raio)

# Saída dos resultados
print(f"Diâmetro da esfera: {diametro:.2f}")
print(f"Circunferência da esfera: {circunferencia:.2f}")
print(f"Área da superfície da esfera: {area_superficie:.2f}")
print(f"Volume da esfera: {volume:.2f}")