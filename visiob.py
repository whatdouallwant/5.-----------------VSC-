import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('GooglePlayStore_wild.csv')
df.info()
df['Rating'].plot(kind='hist', bins=5)
plt.show()