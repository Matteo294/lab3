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
eps = numpify([1e-4, 1e-3, 1e-2, 1e-1])*1e-1
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
eps_log = np.logspace(-5, -2)
eps_lin = np.linspace(1e-4, 1e-1)

def y_teo (e, r0):
    return w0*(e/(1+e) + r0)  


# model without r0

############### PLOTS ##################

plt.subplot(1, 2, 1)
plt.plot(eps_lin/(1+eps_lin), y_teo(eps_lin, 0), c='k', label="Model")
plt.scatter(x, y, c="red", label="Data")
plt.legend()
plt.xlabel(r"$\frac{\epsilon}{1+\epsilon}$")
plt.ylabel(r"$1/\tau_D~[s^{-1}]$")
plt.title("Linear scale")

plt.subplot(1, 2, 2)
plt.semilogx(eps_log/(1+eps_log), y_teo(eps_log, 0), c='k', label="Model")
plt.scatter(x, y, c="red", label="Data")
plt.legend()
plt.xlabel(r"$\frac{\epsilon}{1+\epsilon}$")
plt.ylabel(r"$1/\tau_D~[s^{-1}]$")
plt.title("Log scale")

plt.tight_layout()
plt.show()


# model with r0
fit = curve_fit(y_teo, eps, y)
[r0] = fit[0]

print("r0 = {}".format(r0*w0))
print("quando epsilon = 0 -> tau = {}".format(1/(r0*w0)))

############### PLOTS ##################

plt.subplot(1, 2, 1)
plt.plot(eps_lin/(1+eps_lin), y_teo(eps_lin, r0), c='k', label="Model")
plt.scatter(x, y, c="red", label="Data")
plt.legend()
plt.xlabel(r"$\frac{\epsilon}{1+\epsilon}$")
plt.ylabel(r"$1/\tau_D~[s^{-1}]$")
plt.title("Linear scale")

plt.subplot(1, 2, 2)
plt.semilogx(eps_log/(1+eps_log), y_teo(eps_log, r0), c='k', label="Model")
plt.scatter(x, y, c="red", label="Data")
plt.legend()
plt.xlabel(r"$\frac{\epsilon}{1+\epsilon}$")
plt.ylabel(r"$1/\tau_D~[s^{-1}]$")
plt.title("Log scale")

plt.tight_layout()
plt.show()