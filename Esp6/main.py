import numpy as np 
from matplotlib import pyplot as plt 
import libphysics as lp 

for i in range(3):
    time, V1, V2 = lp.readCSV('Waveforms/Sine/scope_' + str(i) + '.csv', skiprows=3)
    fcamp = 1.067e3 # sampling frequency 1kHz
    Tcamp = 1/fcamp
    time = time[10:] # skip some points
    V1 = V1[10:]
    V2 = V2[10:]
    time -= time[0]
    period_idx = (np.where( abs(time-Tcamp) == min(abs(time-Tcamp)))[0]).item()
    Tcamp = time[period_idx]
    N = int(time[-1]/Tcamp) # number of samples
    t = [k*Tcamp for k in range(N)] # sampling times
    idx = [k*period_idx for k in range(N)]

    V = V2[idx]

    plt.plot(time, V1)
    plt.plot(time, V2)
    plt.plot(t, V, '.', markersize=16)
    plt.show()