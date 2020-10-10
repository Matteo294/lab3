from libphysics import *
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from data_fix import dataFix
import sys
from shockley_fit import shockley_fit, shockley
from sinFit import sinFit

# Set True to display related figures
flags_figures = {
                    'inverting': False, 
                    'non-inverting': False, 
                    'differential': True,
                    'derivator': False,
                    'diode': False 
                }

print()

''' Inverting amplifier '''
print("# Inverting amplifier")
t, V1, V2= dataFix("Data/Newfile1.csv")
V1_ampl = sinFit(t, V1, f=1e3)
V2_ampl = sinFit(t, V2, f=1e3)
print("In wave Vpp:", 2*V1_ampl)
print("Out wave Vpp:", 2*V2_ampl)
print("G =", V2_ampl/V1_ampl) 
if flags_figures['inverting']:
    # Plot measured data
    plt.plot(t, V1, label='Vin')
    plt.plot(t, V2, label='Vout')
    plt.xlabel('t [s]')
    plt.ylabel('V [V]')
    plt.grid()
    plt.legend()
    plt.show()

print()

''' Non-inverting amplifier '''
print("# Non-inverting amplifier")
t, V1, V2 = dataFix("Data/Newfile6.csv")
V1_ampl = sinFit(t, V1, f=1e3)
V2_ampl = sinFit(t, V2, f=1e3)
print("In wave Vpp:", 2*V1_ampl)
print("Out wave Vpp:", 2*V2_ampl)
print("G =", V2_ampl/V1_ampl)
if flags_figures['non-inverting']:
    # Plot measured data
    plt.plot(t, V1, label='Vin')
    plt.plot(t, V2, label='Vout')
    plt.xlabel('t [s]')
    plt.ylabel('V [V]')
    plt.grid()
    plt.legend()
    plt.show()

print()

''' Differential amplifier '''
print("# Differential amplifier")
### Same input waveforms
# Vin1, Vin2 20 deg shift
t, V1, V2 = dataFix("Data/Newfile13.csv")
# Vout
t, V = dataFix("Data/Newfile15.csv")
V1_ampl = sinFit(t, V1, f=1e3)
V2_ampl = sinFit(t, V2, f=1e3)
V_ampl = sinFit(t, V, f=1e3)
print("In waves Vpp:", 2*V1_ampl, 2*V2_ampl)
print("Out wave Vpp:", 2*V_ampl)
if flags_figures['differential']:
    plt.plot(t, V1, label='Vin1')
    plt.plot(t, V2, label='Vin2')
    plt.plot(t, V, label='Vout')
    plt.xlabel('t [s]')
    plt.ylabel('V [V]')
    plt.grid()
    plt.legend()
    plt.show()
    # Display picture of the beat phenomenon
    beat_img = mpimg.imread('Data/1.png')
    plt.figure()
    plt.imshow(beat_img)
    plt.show()

print()

''' Differentiator '''
print("# Differentiator")
### Input sine waveform
t, V1, V2 = dataFix("Data/Newfile17.csv")
V1_ampl = sinFit(t, V1, f=1e3)
V2_ampl = sinFit(t, V2, f=1e3)
print("In wave Vpp:", 2*V1_ampl)
print("Out wave Vpp:", 2*V2_ampl)
if flags_figures['derivator']:
    # Plot measured data
    plt.plot(t, V1, label='Vin')
    plt.plot(t, V2, label='Vout')
    plt.xlabel('t [s]')
    plt.ylabel('V [V]')
    plt.grid()
    plt.legend()
    plt.show()
### Input triangle waveform
t, V1, V2 = dataFix("Data/Newfile19.csv")
if flags_figures['derivator']:
    # Plot measured data
    plt.plot(t, V1, label='Vin')
    plt.plot(t, V2, label='Vout')
    plt.xlabel('t [s]')
    plt.ylabel('V [V]')
    plt.grid()
    plt.legend()
    plt.show()
### Input square waveform
t, V1, V2 = dataFix("Data/Newfile21.csv")
if flags_figures['derivator']:
    # Plot measured data
    plt.plot(t, V1, label='Vin')
    plt.plot(t, V2, label='Vout')
    plt.xlabel('t [s]')
    plt.ylabel('V [V]')
    plt.grid()
    plt.legend()
    plt.show()
if flags_figures['derivator']:
    # Display picture of the triangle wave input-output
    triangle_img = mpimg.imread('Data/2.png')
    plt.figure()
    plt.imshow(triangle_img)
    plt.show()

print()

''' Diode curve - Shockley '''
print("# Diode")
t, V1, V2 = dataFix("Data/Newfile23.csv")
I = (V2/1e3) * 1e3 # 1 kOhm resistance, transfom I in mA
n, Is = shockley_fit(I, V1)
print("Shockley params:   n =", n, "  Is =", Is, "mA")
if flags_figures['diode']:
    # Plot measured data
    xline = np.linspace(min(V1), max(V1), 1000)
    Iline = shockley(xline, n=n, Is=Is)
    plt.plot(V1, I, label='Vout')
    plt.plot(xline, Iline, label='Fit')
    plt.xlabel(' [V]')
    plt.ylabel('I [mA]')
    plt.grid()
    plt.legend()
    plt.show()
