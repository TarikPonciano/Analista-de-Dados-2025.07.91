import pandas as pd

import matplotlib.pyplot as plt

# Produzir um dataframe com uma coluna chamada bimestre contendo Bimestre 1, Bimestre 2, Bimestre 3, Bimestre 4 e outra coluna contendo as notas de cada bimestre. Produza um gráfico de linhas ou de barras que exibe as notas do aluno em cada bimestre ao longo do tempo.

df = pd.DataFrame(
    {
        "bimestres": ["Bimestre 1", "Bimestre 2", "Bimestre 3", "Bimestre 4"],
        "notas": [8, 9.5, 6, 7]
    }
)

plt.plot(df["bimestres"], df["notas"], color="cyan", marker="o", label="Notas")
plt.title("Notas X Bimestres")
plt.xlabel("Bimestre")
plt.ylabel("Nota")
plt.ylim(0,10)
plt.grid(True)

for i in range(len(df["bimestres"])):
    plt.text(
        df.loc[i, "bimestres"],
        df.loc[i, "notas"],
        f"{df.loc[i, "notas"]:.1f}",
        ha="center",
        va="bottom"
)

plt.show()

# Adapte seus dados para ter notas de cada bimestre de Matemática e Química e faça um gráfico que mostra os dois grupos de nota simultaneamente.