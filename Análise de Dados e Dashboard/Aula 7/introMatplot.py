import pandas as pd
import matplotlib.pyplot as plt

# Bibliotecas necessárias:

# pip install pandas
# pip install openpyxl
# pip install matplotlib

df = pd.DataFrame(
    {
        "mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "valor": [1200, 1500, 1800, 1600, 1850, 2100]
    }
)

plt.figure(figsize=(8,5))

plt.plot(df["mes"], df["valor"], color="red", marker="o", linewidth=2, linestyle='-')

# bar, barh, pie, scatter, plot
# Crie um gráfico de linha (plot) com marcadores e em que a linha é vermelha
plt.title("Análise Mês x Faturamento")
plt.xlabel("Mês")
plt.ylabel("Faturamento")
plt.grid(True)
plt.show()