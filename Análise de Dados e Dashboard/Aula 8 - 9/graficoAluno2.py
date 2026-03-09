# Adapte seus dados para ter notas de cada bimestre de Matemática e Química e faça um gráfico que mostra os dois grupos de nota simultaneamente.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "bimestre": ["Bimestre 1", "Bimestre 2", "Bimestre 3", "Bimestre 4"],
        "matematica": [7,8.5,6,10],
        "quimica": [4,3,6.7,8]
    }
)

estilo_linha_1 = dict(
color = "red",
marker= "o",
linestyle = "solid",
linewidth = 2
)

plt.figure(figsize=(8,5))

plt.plot(df["bimestre"], df["matematica"], **estilo_linha_1, label="Matemática")
plt.plot(df["bimestre"], df["quimica"], color="blue", marker="s", linestyle="dashed",linewidth=3, label="Química")

plt.title("Notas Bimestrais")
plt.xlabel("Bimestres")
plt.ylabel("Notas")
plt.ylim(0,12)
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
plt.grid(True)
plt.legend()

for i in range(len(df["bimestre"])):
    plt.text(
        df.loc[i, "bimestre"],
        df.loc[i, "matematica"],
        f"{df.loc[i, "matematica"]:.1f}",
        ha="center",
        va="bottom"
)
    plt.text(
        df.loc[i, "bimestre"],
        df.loc[i, "quimica"],
        f"{df.loc[i, "quimica"]:.1f}",
        ha="center",
        va="bottom"
)
    

plt.show()


