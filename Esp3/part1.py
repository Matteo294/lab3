from libphysics import *
import numpy as np
from math import *
from scipy.optimize import curve_fit

# valori componenti
R = 100e3
C = 10e-9
R2 = 100
w0 = 1/(R*C)
# R1 variabile

# ciclo sugli epsilon
y = []      # vettore dove metterò 1/tau stimato
eps = numpify([1e-4, 1e-2, 1e-1])
x = eps/(1+eps)
n = len(eps)

def exp_func (t, k, a):
    return a*np.exp(-t*k) # k è 1/tau

for i in range(n-1):
    file = "Data/1/e" + str(i+1) + ".csv"
    # load data
    [t, V] = readCSV(file, skiprows=1)
    # fit with exponential
    fit = curve_fit(exp_func, t, V)
    [k, a] = fit[0]
    y.append(k)


plt.plot(x[:2]*w0, y)
plt.show()