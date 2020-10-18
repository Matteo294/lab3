from libphysics import *
from matplotlib import pyplot as plt 
from math import *
import numpy as np 
from scipy.optimize import curve_fit
import sys

file_A = "misure1/Pulse_response/A.csv"
file_B = "misure1/Pulse_response/B.csv"
file_C = "misure1/Pulse_response/C.csv"
file_Shallen = "misure2/Pulse_response/Shallen.csv"

# per mostrare una o più parti
if len(sys.argv) > 1:
    parts['A'] = False
    parts['B'] = False
    parts['C'] = False
    for arg in sys.argv[1:]:
        if arg in ['A', 'B', 'C']:
            parts[arg] = True

Rosc = 1e6
Cosc = 120e-12
R = 100e3
C = 10e-9
tau = R*C

Z_Cosc = lambda w: 1/(1j*w*Cosc)
Z_osc = lambda w: parallelo(Z_Cosc(w), Rosc)

############# A #############

# load data
[t, Vin, V] = readCSV(file_A, skiprows=180)

# model 
s1 = 1/(tau*2) * (-3 + sqrt(5))
s2 = 1/(tau*2) * (-3 - sqrt(5))

def G_A(t):
    return 1/((tau**2) * (s1-s2)) * (np.exp(s1*t) - np.exp(s2*t))

def G_A_fit(t, a, b, c):
    return a * (np.exp(b*t) - np.exp(c*t))
    
fit = curve_fit(G_A_fit, t, V)  # Vout = G * Vin
[a, b, c] = fit[0]

print("Valori attesi\n\ts1 = {}\ts2 = {} \ttau = {}\t a = {}".format(s1, s2, tau, 1/((tau**2) * (s1-s2))))
print("Valori calcolati\n\ts1 = {}\ts2 = {} \ta = {}".format(b, c, a))

# plot 
plt.plot(t, V)
plt.plot(t, G_A(t))
plt.plot(t, G_A_fit(t, a, b, c))
plt.show()
