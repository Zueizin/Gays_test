import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Dados fornecidos
dados = [
    [21.9, 152.4], [22.2, 157.5], [23.2, 162.6], [23.3, 162.6], [23.5, 165.1],
    [23.7, 165.1], [23.8, 165.1], [23.8, 165.1], [23.8, 165.1], [23.8, 165.7],
    [24.1, 166.4], [24.1, 166.4], [24.3, 167.6], [24.6, 167.6], [24.6, 167.6],
    [25.1, 167.6], [25.1, 168.3], [25.1, 172.7], [25.4, 172.7], [25.4, 175.3],
    [25.6, 175.3], [25.7, 175.3], [25.9, 175.9], [26.0, 177.8], [26.2, 177.8],
    [26.4, 177.8], [26.7, 179.1], [26.7, 180.3], [26.7, 180.3], [26.8, 180.3],
    [27.5, 182.3], [27.8, 182.9], [27.9, 184.8], [27.9, 185.4], [28.1, 185.4],
    [28.6, 185.4], [28.7, 189.2], [28.8, 190.5], [29.2, 193.7], [29.2, 195.0]
]

# Separar os dados
comprimento_pe = [x[0] for x in dados]
altura = [x[1] for x in dados]

# Criar o gráfico
plt.figure(figsize=(10, 6))
sns.scatterplot(x=comprimento_pe, y=altura, color='blue', s=100)
plt.title('Relação entre Comprimento do Pé e Altura', fontsize=16)
plt.xlabel('Comprimento do Pé (cm)', fontsize=12)
plt.ylabel('Altura (cm)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Adicionar linha de regressão
sns.regplot(x=comprimento_pe, y=altura, scatter=False, color='red')

# Calcular e mostrar coeficiente de correlação
correlacao = np.corrcoef(comprimento_pe, altura)[0, 1]
plt.text(22, 190, f'Correlação: {correlacao:.2f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

plt.show()