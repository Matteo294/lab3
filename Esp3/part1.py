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
eps = numpify([1e-4, 1e-3, 1e-2, 1e-1])
x = eps/(1+eps)
n = len(eps)

def exp_func (t, k, a):
    return a*np.exp(-t*k) # k è 1/tau

for i in range(n):
    file = "Newdata/eps" + str(i+1) + ".csv"
    # load data
    print(i)
    [t, V] = readCSV(file, skiprows=1)
    t = numpify(t) - t[0]
    # fit with exponential
    fit = curve_fit(exp_func, t, V)
    [k, a] = fit[0]
    if(i==0):
        tpoints = np.linspace(0, 1)
        plt.scatter(t, V, label="Data")
        plt.plot(tpoints, exp_func(tpoints, k, a), label="Fit")
        plt.legend()
        plt.show()
    y.append(k)

y = numpify(y)

plt.scatter(x*w0, y)
plt.show()