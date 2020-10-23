from libphysics import *
from matplotlib import pyplot as plt 
import numpy as np 

R = 100e3
C = 10e-9
tau = R*C

# load data
file = "misure2/data.csv"
[f, Vin, Vout, dt] = readCSV(file, skiprows=1)
phi = dt*f*360

fig = bodeplot(f, Amp=Vout/Vin, Phase=phi, deg=True)

# model
H_teo = lambda s: 1/(tau**2 * s**2 + 2*tau*s + 1)
fline = np.logspace(0, 3, 1000)
Hline = H_teo(-1j*2*np.pi*fline)

fig = bodeplot(fline, H=Hline, asline=True, figure=fig)

# plot stile
ax = fig.axes[0]
handles,_ = ax.get_legend_handles_labels()
fig.legend(handles, labels=["Data", "Model"], loc ='lower center', ncol=2)
fig.subplots_adjust(hspace=0.4, left=0.1)
plt.tight_layout()
plt.show()

idx20 = np.where(f==20)
idx50 = np.where(f==50)
idx10 = np.where(f==10)
idx = [idx20, idx50, idx10]
vals = [Vout[i][0]/Vin[i][0] for i in idx]
print("Amplitudes at f = 20Hz, 50Hz, 10Hz", 20*np.log10(vals))	
