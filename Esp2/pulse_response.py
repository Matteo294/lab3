from libphysics import *
from matplotlib import pyplot as plt 
from math import *
import numpy as np 
from scipy.optimize import curve_fit
import sys

file_A = "misure1/Pulse_response/A.csv"
file_B = "misure1/Pulse_response/B.csv"
file_C = "misure1/Pulse_response/C.csv"
file_D = "misure2/Pulse_response/Shallen.csv"
file_Shallen = "misure2/Pulse_response/Shallen.csv"

# to show one or more parts of the analysis
parts = {
            'A': False,
            'B' : False,
            'C': False,
            'D': False
}
if len(sys.argv) > 1:
    parts['A'] = False
    parts['B'] = False
    parts['C'] = False
    parts['D'] = False
    for arg in sys.argv[1:]:
        if arg in ['A', 'B', 'C', 'D']:
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
[t, Vin, V] = readCSV(file_A, skiprows = 185)

# model 
t_model = t[10:]
s1 = 1/(tau*2) * (-3 + sqrt(5))
s2 = 1/(tau*2) * (-3 - sqrt(5))
t0 = 0.005*1/30     # 0.5% * period = 0.5% * 1/f

def G_A(t):
    return 5/((tau**2) * (s1-s2)) * ((1-exp(-s1*t0))*np.exp(s1*t)/s1 - (1-exp(-s2*t0))*np.exp(s2*t)/s2)

# plot 
if parts['A']:
    plt.plot(t, V, label="Data", c="red")
    plt.plot(t_model, G_A(t_model), label="Model", c="k", ls='--')

    plt.title(r"Impulse response -- Conf. A")
    plt.legend()
    plt.xlabel(r"$t$ [s]")
    plt.ylabel(r"$V_{out}$ [V]")
    plt.grid()
    plt.tight_layout()
    plt.show()


############# B #############

# load data
[t, Vin, V] = readCSV(file_B, skiprows=85)

# model 
t_model = t
s1 = 1/(tau*2) * (-3 + sqrt(5))
s2 = 1/(tau*2) * (-3 - sqrt(5))
t0 = 0.005*1/100    # 0.5% * period = 0.5% * 1/f

def G_A(t):
    return -5/tau * (t*np.exp(-t/tau)*(1-exp(t0/tau)) + t0*np.exp(-t/tau)*exp(t0/tau)) - 5*np.exp(-t/tau)*(1-exp(t0/tau))

# plot 
if parts['B']:
    plt.plot(t, V, label="Data", c="red")
    plt.plot(t_model, G_A(t_model), label="Model", c="k", ls='--')

    plt.title(r"Impulse response -- Conf. B")
    plt.legend()
    plt.legend()
    plt.xlabel(r"$t$ [s]")
    plt.ylabel(r"$V_{out}$ [V]")
    plt.grid()
    plt.tight_layout()
    plt.show()


############# C #############

# load data
[t, Vin, V] = readCSV(file_C, skiprows=250)

# model 
t_model = t
s1 = 1/(tau*2) * (-3 + sqrt(5))
s2 = 1/(tau*2) * (-3 - sqrt(5))
t0 = 0.005*1/50    # 0.5% * period = 0.5% * 1/f

def G_A(t):
    return -5/tau * (t*np.exp(-t/tau)*(1-exp(t0/tau)) + t0*np.exp(-t/tau)*exp(t0/tau)) - 5*np.exp(-t/tau)*(1-exp(t0/tau))

# plot 
if parts['C']:
    plt.plot(t, V, label="Data", c="red")
    plt.plot(t_model, G_A(t_model), label="Model", c="k", ls='--')
    
    plt.title(r"Impulse response -- Conf. C")
    plt.legend()
    plt.xlabel(r"$t$ [s]")
    plt.ylabel(r"$V_{out}$ [V]")
    plt.grid()
    plt.tight_layout()
    plt.show()


############# D - SALLEN-KEY #############

# load data
[t, Vin, V] = readCSV(file_D, skiprows=163)

# model 
t_model = t[30:]
s1 = 1/(tau*2) * (-3 + sqrt(5))
s2 = 1/(tau*2) * (-3 - sqrt(5))
t0 = 0.005*1/50    # 0.5% * period = 0.5% * 1/f

def G_A(t):
    return -5/tau * (t*np.exp(-t/tau)*(1-exp(t0/tau)) + t0*np.exp(-t/tau)*exp(t0/tau)) - 5*np.exp(-t/tau)*(1-exp(t0/tau))

# plot 
if parts['D']:
    plt.plot(t, V, label="Data", c="red")
    plt.plot(t_model, G_A(t_model), label="Model", c="k", ls='--')
    
    plt.title(r"Impulse response -- Sallen-Key")
    plt.legend()
    plt.xlabel(r"$t$ [s]")
    plt.ylabel(r"$V_{out}$ [V]")
    plt.grid()
    plt.tight_layout()
    plt.show()