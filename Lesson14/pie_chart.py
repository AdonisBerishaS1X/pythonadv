import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lesson14.csv")

nobel_prizes = df.groupby("Continent")['Nobel Prices'].sum()

no_of_countinents = nobel_prizes.count()

colors = ['gold','lightcoral','yellow','orange','lightskyblue','aquamarine','burlywood']


plt.figure(figsize=(10,10))


nobel_prizes.plot(kind="pie",colors=colors,autopct="%1.1f%%")

plt.show()