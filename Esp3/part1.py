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
x = numpify(eps/(1+eps))
n = len(eps)

################ DATA ################

def exp_func (t, k, a):
    return a*np.exp(-t*k) # k è 1/tau

for i in range(n):
    file = "Newdata/eps" + str(i+1) + ".csv"
    # load data
    [t, V] = readCSV(file, skiprows=1)
    t = numpify(t) - t[0]
    # fit with exponential
    fit = curve_fit(exp_func, t, V)
    [k, a] = fit[0]
    if(i==-1):
        tpoints = np.linspace(0, 1)
        plt.scatter(t, V, label="Data")
        plt.plot(tpoints, exp_func(tpoints, k, a), label="Fit")
        plt.legend()
        plt.show()
    y.append(k)

y = numpify(y) # y = 1/tau

################ MODEL ################
x_teo = np.linspace(0, 1e-1)

def y_teo (e, r0):
    return w0*(e/(1+e)+r0)

fit = curve_fit(y_teo, eps, y)
[r0] = fit[0]

plt.plot(x_teo, y_teo(x_teo, r0), c='k', label="Model")
plt.scatter(x, y, c="red", label="Data")
plt.legend()
plt.xlabel(r"$\frac{\epsilon}{1+\epsilon}$")
plt.ylabel(r"$1/\tau$")
plt.tight_layout()
plt.show()