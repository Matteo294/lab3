import numpy as np 
from matplotlib import pyplot as plt 

N = 1000

''' Circuit 1 '''
Is = 1e-9
n = 1.5
beta = 40
R1 = 21e3
R0 = 10e3
RD = 50e3
rho = lambda w: w/(2*Is*np.sinh(beta*w/n))
Rx = lambda w: R1*(RD+rho(w)) / (R1+RD+rho(w)) # Some parameters are set to 1

wline = np.linspace(0, 0.8, N)
Rxline = Rx(wline)

ax = plt.plot(wline, Rxline/1000, color='deepskyblue', linewidth=3.0)
plt.plot(wline, np.full(N, 2*R0/1000), '--', color='black', linewidth=3.0)
plt.xlabel('Diode Voltage $[V]$', fontsize=18)
plt.ylabel(r'Dynamic Feedback Resistance $[k\Omega]$', fontsize=18)
plt.text(0.5, 20.15, r'$2R_0$', fontsize=22)
plt.grid()
plt.show()