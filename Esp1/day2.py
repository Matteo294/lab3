from libphysics import *
import numpy as np
from matplotlib import pyplot as plt 
from data_fix import dataFix

''' Inverting amplifier '''
t, V1, V2, dV1, dV2 = dataFix("Data/Newfile1.csv", ncols=3, errs=True)
# Plot measured data
plt.plot(t, V1, label='Vin')
plt.plot(t, V2, label='Vout')
plt.xlabel('t [ss]')
plt.ylabel('V [V]')
plt.grid()
plt.show()

''' Non-inverting amplifier '''
t, V1, V2, dV1, dV2 = dataFix("Data/Newfile6.csv", ncols=3, errs=True)
# Plot measured data
plt.plot(t, V1, label='Vin')
plt.plot(t, V2, label='Vout')
plt.xlabel('t [ss]')
plt.ylabel('V [V]')
plt.grid()
plt.show()