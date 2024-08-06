import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('./SHREYAS/data.csv')
df.dropna()
df.plot.scatter(x='Duration', y='Calories', c='Violet') 
plt.show()
df['Calories'].plot.hist(color="red",edgecolor='black')
plt.show()

