import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\democracia.csv")
dataset = pd.DataFrame(dataset)

# Dividindo os dados entre pré-ditadura, ditadura e pós-ditadura
dataset = dataset[dataset['Entity']=="Brazil"]
predit = dataset[(dataset['Year']>=1928) & (dataset['Year']<=1964)]
dit = dataset[(dataset['Year']>=1964) & (dataset['Year']<=1985)]
posdit = dataset[dataset['Year']>=1985]

# Achando médias dos índices pré, durante e pós-ditadura
mediaant = predit['electdem_vdem_owid'].mean()
mediadit = dit['electdem_vdem_owid'].mean()
mediapos = posdit['electdem_vdem_owid'].mean()
print("Média da Estimativa Central do Nível de Democracia pré-ditadura: ",mediaant)
print("Média da Estimativa Central do Nível de Democracia durante a ditadura: ",mediadit)
print("Média da Estimativa Central do Nível de Democracia pós-ditadura: ",mediapos)

# Comparando índices
print("\nApós a ditadura, a média da Estimativa Central do Nível de Democracia ficou",round(mediapos/mediaant,2),"vezes maior do que antes da ditadura, em média.")
print("Após a ditadura, a média da Estimativa Central do Nível de Democracia ficou",round(mediapos/mediadit,2),"vezes maior do que durante a ditadura, em média.")

# Plotando gráfico
g = sns.lineplot(x=predit['Year'],y=predit['electdem_vdem_owid'],label="Pré-ditadura")
g = sns.lineplot(x=dit['Year'],y=dit['electdem_vdem_owid'],label="Ditadura")
g = sns.lineplot(x=posdit['Year'],y=posdit['electdem_vdem_owid'],label="Pós-ditadura")
g.set_xlabel("Ano")
g.set_ylabel("Estimativa Central do Nível de Democracia")
plt.show()
