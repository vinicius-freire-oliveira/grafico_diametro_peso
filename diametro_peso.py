import numpy as np  # Importa a biblioteca NumPy para operações com arrays
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para plotagem

# Supondo que 'dado' seja um array NumPy definido anteriormente, aqui está um exemplo fictício:
# dado = np.array([...])

# Exemplo de definição fictícia de 'dado' para fins de correção:
dado = np.random.rand(10000, 2)  # Cria um array de números aleatórios para simular 'dado'

# Dividindo 'dado' em duas partes: laranjas e toranjas
diametro_laranja = dado[:5000, 0]
diametro_toranja = dado[5000:, 0]
peso_laranja = dado[:5000, 1]
peso_toranja = dado[5000:, 1]

# Plotando os dados de diâmetro versus peso para laranjas e toranjas
plt.figure(figsize=(8, 6))  # Define o tamanho da figura

# Plotagem dos dados de laranjas (primeiras 5000 linhas)
plt.plot(diametro_laranja, peso_laranja, 'bo', label='Laranjas')

# Plotagem dos dados de toranjas (últimas 5000 linhas)
plt.plot(diametro_toranja, peso_toranja, 'ro', label='Toranjas')

# Adicionando legendas, título e rótulos dos eixos
plt.legend()  # Adiciona a legenda com base nos rótulos 'label' fornecidos acima
plt.title('Relação Diâmetro vs. Peso de Laranjas e Toranjas')
plt.xlabel('Diâmetro')
plt.ylabel('Peso')

# Exibe o gráfico
plt.show()
