import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./iris.csv")

print(df.head(5))
print(df.tail(5))
print(df.info())
print(df.describe())
df.plot()
plt.show()
