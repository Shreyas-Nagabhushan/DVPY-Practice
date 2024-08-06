import pandas as pd
# import matplotlib.pyplot as plt 

# df = pd.read_csv('./SHREYAS/data.csv')
# df.dropna()
# print(df)
# df.plot.scatter(x='Duration', y='Calories') 

import numpy as np

data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'z': np.random.rand(100),
    'a': np.random.rand(100),
    'b': np.random.rand(100),
    'c': np.random.rand(100),
    'd': np.random.rand(100),
    'e': np.random.rand(100),
    'f': np.random.rand(100),
    'g': np.random.rand(100),
})

data.plot.scatter(x='x', y='y') 