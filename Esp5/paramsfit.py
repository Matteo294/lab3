import numpy as np 
from libphysics import readCSV
from scipy.optimize import curve_fit as fit
from matplotlib import pyplot as plt

# Moving Vout from the other side of equality...
def VanDerPol(M, A, B, C, p1, p2):
    Vdot = M[:,0]
    Vddot = M[:,1]
    return -A*Vddot + B*(p1 - p2*V**2)*Vdot + C

t, V = readCSV('./waveforms1/scope_0.csv', skiprows=2)
t -= t[0]
dt = t[1] - t[0]
# Discard first points
t = t[50:]
V = V[50:]
N = len(V) # number of points

n = 150 # number of points to approximate derivative as a finite difference ratio

Vdot = (V[n:] - V[:-n]) / (n*dt) # First derivative
Vddot = (Vdot[n:] - Vdot[:-n]) / (n*dt) # Second derivative

# Resize data
t = t[:-2*n]
V = V[:-2*n]
Vdot = Vdot[:-n]

M = np.transpose(np.vstack((Vdot, Vddot)))
print(M.shape)

# Fit with the Van der Pol eq.
params = fit(VanDerPol, M, V)
p = params[0]

Vfit = VanDerPol(M, p[0], p[1], p[2], p[3], p[4])

plt.plot(Vfit, Vdot, '.', color='deepskyblue', label='Fit')
plt.plot(V, Vdot, '.', color='chartreuse', label='Experimental data')
plt.legend()
plt.ylabel(r'$\dot V_{out}$', fontsize=22)
plt.xlabel(r'$V_{out}$', fontsize=22)
plt.show()