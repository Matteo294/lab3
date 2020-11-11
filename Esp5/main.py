from libphysics import *
import numpy as np 
from matplotlib import pyplot as plt 
from scipy.optimize import curve_fit as fit

# Fit function (first two terms of the Van der Pol equation)
def func(t, w, A, phi1, B, phi2, C):
    return C + A*np.cos(w*t + phi1) - B/w*np.sin(3*w*t + phi2)

''' Circuit 1 - Wien bridge oscillator '''
base_filename = './waveforms1/scope_'
C = 10e-9
R = 102.8e3
ws = 1/(R*C) # omega
Rd_arr, deltat_arr, Vpp_arr, dt_arr, dV_arr = readCSV('data1.csv', skiprows=1)
for i in range(4):
    filename = base_filename + str(i) + '.csv'
    t, V = readCSV(filename, skiprows=2)
    t -= t[0]
    N = len(V) # number of points

    print("Measured frequency =", 1/deltat_arr[i], "(expected %1f)" %(ws/(2*np.pi)))
    
    # I use lambdas to change fit parameters (in this case I decided to set w and fit phi)
    params = fit(lambda t, A, phi1, B, phi2, C: func(t, ws, A, phi1, B, phi2, C), t, V) 
    A, phi1, B, phi2, C = params[0]

    plt.plot(t, V)
    plt.plot(t, func(t, ws, A, phi1, B, phi2, C))
    plt.show()