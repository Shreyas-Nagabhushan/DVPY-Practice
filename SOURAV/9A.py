import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./iris.csv")
df.plot()
df.plot.scatter(x="sepal_length", y="petal_length")
colors = []

for row in df['species']:
    if row == 'setosa':
        colors.append('red')
    elif row == 'virginica':
        colors.append('green')
    else:
        colors.append('blue')

df.plot.scatter(x="sepal_length", y="petal_length", c=colors)
plt.figure()
df['sepal_length'].plot(kind='hist')
plt.show() 