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

fig = bodeplot(f, Amp=Vout/Vin, Phase=phi, deg=True, color='k')

# model
H_teo = lambda s: 1/(tau**2 * s**2 + 2*tau*s + 1)
fline = np.logspace(0, 3, 1000)
Hline = H_teo(-1j*2*np.pi*fline)

fig = bodeplot(fline, H=Hline, asline=True, figure=fig, color='k')



idx20 = np.where(f==20)
idx50 = np.where(f==50)
idx10 = np.where(f==10)
idx = [idx20, idx50, idx10]
vals = [Vout[i][0]/Vin[i][0] for i in idx]
print("Amplitudes at f = 20Hz, 50Hz, 10Hz", 20*np.log10(vals))	


############## COMPARISON WITH C #################

Z_C = lambda w: 1/(-1j*w*C)
H0 = lambda w: Z_C(w) / (Z_C(w) + R) # Just a useful intermediate step
# Transfer function
H_teo = lambda w: np.power(H0(w), 2)

# Getting data from csv
data = readCSV("misure1/C/data.csv", skiprows=1, cols=[0,1,2,3])
f = data[0]
Vin = data[1]
Vout = data[2]
phi = data[3]*f * 360 # phase = deltaT/T * 360
fig = bodeplot(f, Amp=Vout/Vin, Phase=phi, deg=True, figure=fig, color="royalblue")

# Model
fline = np.logspace(0, log10(2000), 1000)
Hline = H_teo(2*np.pi*fline)
Hline_abs = np.absolute(Hline)
Hline_phase = np.angle(Hline) * 180/np.pi
fig = bodeplot(fline, Amp=Hline_abs, Phase=Hline_phase, figure=fig, asline=True, color='royalblue')

# plot stile
ax = fig.axes[0]
handles,_ = ax.get_legend_handles_labels()
fig.legend(handles, labels=["Sallen-Key", "Model", "C", "Model"], loc ='lower center', ncol=2)
fig.subplots_adjust(hspace=0.4, left=0.1)
plt.tight_layout()
plt.show()