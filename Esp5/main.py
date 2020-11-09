from libphysics import *
import numpy as np 
from matplotlib import pyplot as plt 

selector = {
    'part1': False,
    'part2': True
}


''' Circuit 1 '''
if selector['part1']:
    base_filename = './waveforms1/scope_'
    C = 10e-9
    R = 100e3
    Rd_arr, deltat_arr, Vpp_arr, dt_arr, dV_arr = readCSV('data1.csv', skiprows=1)
    for i in range(4):
        filename = base_filename + str(i) + '.csv'
        t, V = readCSV(filename, skiprows=2)
        t -= t[0]
        N = len(V) # number of points
        w = 1/(R*C) # omega

        print("f =", 1/deltat_arr[i], "teorica", 1/(2*np.pi*R*C))
        
        # Preparing fit matrix
        M = np.zeros((N,5))
        M[:,0] = np.ones(N)
        M[:,1] = np.cos(w*t)
        M[:,2] = np.sin(w*t)
        M[:,3] = np.cos(3*w*t)
        M[:,4] = np.sin(3*w*t)
        
        # Fit y = Acos(wt + phi1) + Bsin(wt + phi2)
        params = lsq_fit(V, M, 0.5*np.ones((N,1)))
        C0, C1, C2, C3, C4 = params['fit_out']
        A = np.abs(C1-1j*C2)
        B = np.abs(C3-1j*C4)
        print("Vout(t) = %.3fcos(wt) + %.3fsin(wt)" %(A, B))
        
        plt.plot(t, V)
        plt.plot(t, C0 + C1*np.cos(w*t) + C2*np.sin(w*t) + C3*np.cos(3*w*t) + C4*np.sin(3*w*t))
        plt.show()




''' Circuit 2 '''
if selector['part2']:
    base_filename = './waveforms2/scope_'
    C = 10e-9
    R = 100e3
    deltat, Vpp, dt, dV = readCSV('data2.csv', skiprows=1)
    for i in range(4):
        filename = base_filename + str(4+i) + '.csv'
        t, V = readCSV(filename, skiprows=2)
        t -= t[0]
        N = len(V) # number of points
        w = 1/(R*C) # omega

        print("f =", 1/deltat, "teorica", 1/(2*np.pi*R*C))
        
        # Preparing fit matrix
        M = np.zeros((N,5))
        M[:,0] = np.ones(N)
        M[:,1] = np.cos(w*t)
        M[:,2] = np.sin(w*t)
        M[:,3] = np.cos(3*w*t)
        M[:,4] = np.sin(3*w*t)
        
        # Fit y = Acos(wt + phi1) + Bsin(wt + phi2)
        params = lsq_fit(V, M, 0.5*np.ones((N,1)))
        C0, C1, C2, C3, C4 = params['fit_out']
        A = np.abs(C1-1j*C2)
        B = np.abs(C3-1j*C4)
        print("Vout(t) = %.3fcos(wt) + %.3fsin(wt)" %(A, B))
        
        plt.plot(t, V)
        plt.plot(t, C0 + C1*np.cos(w*t) + C2*np.sin(w*t) + C3*np.cos(3*w*t) + C4*np.sin(3*w*t))
        plt.show()
