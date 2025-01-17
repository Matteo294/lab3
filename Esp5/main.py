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
    params = fit(lambda t, A, phi1, B, phi2, C: func(t, ws, A, phi1, B, phi2, C), t, V, p0=[1, 3*np.pi/4, 1, 3*np.pi/4, 0]) 
    A, phi1, B, phi2, C = params[0]

    print("A = %.2f \t phi1 = %.2f \t B = %.2f \t phi2 = %.2f \t C = %.2f" %(A, phi1 % (2*np.pi), B/ws, phi2 % (2*np.pi), C))
    print("Coefficient ratio (x100) %.2f" %(100*B/ws*A))
    
    plt.subplot(121)
    plt.plot(t*1000, V, color='royalblue', linewidth=2.0, label='Experimental data')
    plt.plot(t*1000, func(t, ws, A, phi1, B, phi2, C), color='springgreen', linewidth=2.0, label='Fit prediction')
    plt.xlabel(r'Time $[ms]$', fontsize=20)
    plt.ylabel(r'Voltage $[V]$', fontsize=20)
    plt.legend(loc=1)

    plt.subplot(122)
    plt.plot(t*1000, 1000*(func(t, ws, A, phi1, B, phi2, C) - V), '.', color='red', markersize=8, label='Residuals')
    plt.xlabel(r'Time $[ms]$', fontsize=20)
    plt.ylabel(r'Voltage difference $[mV]$', fontsize=20)
    plt.legend(loc=8)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.show()

''' Circuit 2 - Wien bridge oscillator '''
base_filename = './waveforms2/scope_'
C = 10e-9
R = 102.8e3
ws = 1/(R*C) # omega
Rd_arr, deltat_arr, Vpp_arr, dt_arr, dV_arr = readCSV('data1.csv', skiprows=1)
for i in range(4):
    filename = base_filename + str(i+4) + '.csv'
    t, V = readCSV(filename, skiprows=2)
    t -= t[0]
    N = len(V) # number of points

    print("Measured frequency =", 1/deltat_arr[i], "(expected %1f)" %(ws/(2*np.pi)))
    
    # I use lambdas to change fit parameters (in this case I decided to set w and fit phi)
    params = fit(lambda t, A, phi1, B, phi2, C: func(t, ws, A, phi1, B, phi2, C), t, V) 
    A, phi1, B, phi2, C = params[0]
    
    
    plt.subplot(121)
    plt.plot(t*1000, V, color='royalblue', linewidth=2.0, label='Experimental data')
    plt.plot(t*1000, func(t, ws, A, phi1, B, phi2, C), color='springgreen', linewidth=2.0, label='Fit prediction')
    plt.xlabel(r'Time $[ms]$', fontsize=20)
    plt.ylabel(r'Voltage $[V]$', fontsize=20)
    plt.legend(loc=1)

    plt.subplot(122)
    plt.plot(t*1000, 1000*(func(t, ws, A, phi1, B, phi2, C) - V), '.', color='red', markersize=8, label='Residuals')
    plt.xlabel(r'Time $[ms]$', fontsize=20)
    plt.ylabel(r'Voltage difference $[mV]$', fontsize=20)
    plt.legend(loc=8)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.show()