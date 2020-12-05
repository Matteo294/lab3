from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd 

data = pd.read_csv('numerical.csv')

plt.plot(data['t'], data['x'])
plt.show()

plt.plot(data['x'], data['xdot'])
plt.show()