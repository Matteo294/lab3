from libphysics import *
import numpy as np
from math import*
from scipy.optimize import curve_fit
from uncertainties import ufloat as uf
from uncertainties import unumpy as unp
from uncertainties.umath import *

################# DATA #################
R = 100e3
C = 100e-9

file = "data3.csv"
[R1, R2, dt, sigma_dt] = readCSV(file, skiprows=1)

R1 = numpify(R1)
R2 = numpify(R2)
T_exp = numpify(dt)

r = R1/(R1+R2)
tau = R*C


################# MODEL ################

T_teo = tau/2*np.log((1+r)/(1-r))

T_fit = lambda r,q: tau/2*np.log((1+r)/(1-r)) + q
fit = curve_fit(T_fit, r, T_exp)
q = fit[0]
print("q = {}".format(q))

if(0):
    plt.subplot(1, 2, 1)
    plt.scatter(np.log((1+r)/(1-r)), T_exp, label="Data", color='k')
    plt.plot(np.log((1+r)/(1-r)), T_teo*4, label="Model", c='yellowgreen')
    plt.xlabel(r"$\log{\frac{1+r}{1-r}}$")
    plt.title(r"$T = 2 \tau \log \left( \frac{1+r}{1-r} \right)$")
    plt.ylabel(r"$T~[s]$")
    plt.legend()


    plt.subplot(1,2,2)
    plt.scatter(np.log((1+r)/(1-r)), T_exp, label="Data", color='k')
    plt.plot(np.log((1+r)/(1-r)), T_teo, label="Model", c='yellowgreen')
    plt.xlabel(r"$\log{\frac{1+r}{1-r}}$")
    plt.ylabel(r"$T~[s]$")
    plt.title(r"$T = \frac{\tau}{2} \log \left( \frac{1+r}{1-r} \right)$")
    plt.legend()

    plt.tight_layout()
    plt.show()


################### PLOT ###################
C = 10e-9
R = 10e3
tau = R*C
r = 1/2
Vsat = 12

semiT = tau *log((1+r)/(1-r))
t1 = tau*log(1/(1-r))

dt1 = np.linspace(0, t1, 100)
dt2 = np.linspace(t1, t1+semiT, 100)
dt3 = np.linspace(t1 + semiT, t1+2*semiT, 100)
dt4 = np.linspace(t1+2*semiT, t1+3*semiT, 100)
dt5 = np.linspace(t1+3*semiT, t1+4*semiT, 100)
dt = np.concatenate((dt1, dt2, dt3, dt4, dt5))
n = 100

# Vout
V1 = Vsat*np.ones(n)
V2 = -Vsat*np.ones(n)
V3 = V1
V4 = V2
V5 = V1
Vout = np.concatenate((V1, V2, V3, V4, V5))

# V+
V1 = r*Vsat*np.ones(n)
V2 = -r*Vsat*np.ones(n)
V3 = V1
V4 = V2
V5 = V1
Vplus = np.concatenate((V1, V2, V3, V4, V5))

# V-
V1 = Vsat*(1-np.exp(-dt1/tau))
V2 = Vsat*(1+r)*np.exp(-(dt2-t1)/tau) - Vsat
V3 = Vsat*(1+r)*(1-np.exp(-(dt3-(t1 + semiT))/tau)) - Vsat*r
V4 = Vsat*(1+r)*np.exp(-(dt4 - (t1 + 2*semiT))/tau) - Vsat
V5 = V3 = Vsat*(1+r)*(1-np.exp(-(dt5-(t1 + 3*semiT))/tau)) - Vsat*r
Vminus = np.concatenate((V1, V2, V3, V4, V5))

if(0):
    plt.plot(dt, Vout, color='k', label=r"$V_{out}$")
    plt.plot(dt, Vplus, c="red", label=r"$V_{+}$")
    plt.plot(dt, Vminus, c='royalblue', label = r"$V_-$")

    # set ticks
    plt.xticks([0,t1, t1+semiT, t1+2*semiT, t1+3*semiT, t1+4*semiT], [r'0', r'$t_1$', r'$t_1 + T/2$', r'$t_1 + T$', r'$t_1 + 3T/2$', r'$t_1 + 2T$'])
    plt.yticks([Vsat, r*Vsat, 0, -r*Vsat, -Vsat], [r"$V_{sat}$", r"$rV_{sat}$", 0, r"$-rV_{sat}$", r"$-V_{sat}$"])

    # text boxes
    text1 = r"1"
    text2 = r"2"
    text3 = r"3"
    plt.text(t1/3, r*Vsat+1, text1)
    plt.text(t1+t1/10, 0, text2)
    plt.text(t1+semiT/2, -r*Vsat-2, text3)

    plt.title("Relaxation oscillator")
    plt.legend(loc="lower right")
    plt.show()

file = "waveforms2/scope_6.csv"
[t, V] = readCSV(file, skiprows=10)

if(1):
    plt.plot((t-t[0])*1e3, V, c='k')
    plt.xlabel(r"$t~[ms]$")
    plt.ylabel(r"$V_{out}~[V]$")
    plt.tight_layout()
    plt.show()




###################### LAST PART ################À
file = "waveforms3/scope_8.csv"
[t, V] = readCSV(file, skiprows=2)

if(1):
    plt.plot((t-t[0])*1e3, V, c='k')
    plt.xlabel(r"$t~[ms]$")
    plt.ylabel(r"$V_{out}~[V]$")
    plt.tight_layout()
    plt.show()
