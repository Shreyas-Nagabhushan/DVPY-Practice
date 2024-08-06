import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
print(df.head())
print(df.tail())

print(df.info())
print(df.describe())

plt.hist(df['Calories'], bins=10, edgecolor='black')
plt.show()
plt.scatter(df['Calories'], df['Duration'])
plt.show()
plt.plot(df['Duration'], df['Calories'])
plt.show()

