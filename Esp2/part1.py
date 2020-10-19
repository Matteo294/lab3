from libphysics import *
from matplotlib import pyplot as plt 
import numpy as np 
import sys

file_confA = './misure1/A/data.csv'
file_confB = './misure1/B/data.csv'
file_confC = './misure1/C/data.csv'

parts = {
            'A': True,
            'B' : False,
            'C': False
}

if len(sys.argv) > 1:
    parts['A'] = False
    parts['B'] = False
    parts['C'] = False
    for arg in sys.argv[1:]:
        if arg in ['A', 'B', 'C']:
            parts[arg] = True

parallelo = lambda Z1, Z2: Z1*Z2/(Z1+Z2)

Rosc = 1e6
Cosc = 120e-12
R = 100e3
C = 10e-9

Z_Cosc = lambda w: 1/(1j*w*Cosc)
Z_osc = lambda w: parallelo(Z_Cosc(w), Rosc)

''' Part A '''
if parts['A']:
    # Impedances
    Z_C = lambda w: 1/(1j*w*C)
    Zeq1 = lambda w: parallelo(Z_C(w), (R + Zeq2(w)))
    Zeq2 = lambda w: parallelo(Z_C(w), Z_osc(w))
    Z_out = lambda w: parallelo(Z_C(w), R + parallelo(R, Z_C(w)))

    # Transfer function
    H_teo = lambda w,s: 1/(1 + 3*R*s*C + (R*s*C)**2)  # devo ancora metterci l'osc

    # Getting data from csv
    data = readCSV(file_confA, skiprows=1, cols=[0,1,2,3])
    f = data[0]
    Vin = data[1]
    Vout = data[2]
    phi = data[3]*f * 360 # phase = deltaT/T * 360
    fig = bodeplot(f, Amp=Vout/Vin, Phase=phi, deg=True)


    # Model
    fline = np.logspace(0, 3, 1000)
    Hline = H_teo(2*np.pi*fline, -1j*2*np.pi*fline)
    Hline_abs = np.absolute(Hline)
    Hline_phase = np.angle(Hline) * 180/np.pi
    fig = bodeplot(fline, Amp=Hline_abs, Phase=Hline_phase, figure=fig, asline=True)

    # plot stile
    ax = fig.axes[0]
    handles,_ = ax.get_legend_handles_labels()
    fig.legend(handles, labels=["Data", "Model"], loc ='lower center', ncol=2)
    fig.subplots_adjust(hspace=0.4, left=0.1)
    plt.tight_layout()
    plt.show()

    # Output impedance
    fig = bodeplot(fline, Amp=Z_out(2*np.pi*fline), Phase=Hline_phase, asline=True)
    ax1, ax2 = fig.axes
    ax1.set_ylabel(r"Z [$\Omega$]")
    ax1.set_title(r"$Z_{out}$")
    plt.tight_layout()
    # plt.show()




''' Part B '''
if parts['B']:
    # Impedances
    Z_C = lambda w: 1/(1j*w*C)
    H0 = lambda w: Z_C(w) / (Z_C(w) + R) # Just a useful intermediate step
    Zeq1 = lambda w: parallelo(Z_C(w), Z_osc(w))
    
    # Transfer function
    H_teo = lambda w: H0(w) * Zeq1(w)/(Zeq1(w)+R)

    # Getting data from csv
    data = readCSV(file_confB, skiprows=1, cols=[0,1,2,3])
    f = data[0]
    Vin = data[1]
    Vout = data[2]
    phi = -data[3]*f * 360 # phase = deltaT/T * 360
    fig = bodeplot(f, Amp=Vout/Vin, Phase=phi, deg=True)

     # Model
    fline = np.logspace(0, 3, 1000)
    Hline = H_teo(2*np.pi*fline)
    Hline_abs = np.absolute(Hline)
    Hline_phase = np.angle(Hline) * 180/np.pi
    fig = bodeplot(fline, Amp=Hline_abs, Phase=Hline_phase, figure=fig, asline=True)
    
    # plot stile
    ax = fig.axes[0]
    handles,_ = ax.get_legend_handles_labels()
    fig.legend(handles, labels=["Data", "Model"], loc ='lower center', ncol=2)
    fig.subplots_adjust(hspace=0.4, left=0.1)
    plt.tight_layout()
    plt.show()


    # Output impedance
    fig = bodeplot(fline, Amp=np.absolute(Zeq1(2*np.pi*fline)), Phase=np.angle(Zeq1(2*np.pi*fline)), asline=True)
    ax1, ax2 = fig.axes
    ax1.set_ylabel(r"Z [$\Omega$]")
    ax1.set_title(r"$Z_{out}$")
    plt.tight_layout()
    plt.show()



''' Part C '''
if parts['C']:
    # Impedances
    Z_C = lambda w: 1/(1j*w*C)
    H0 = lambda w: Z_C(w) / (Z_C(w) + R) # Just a useful intermediate step
    # Transfer function
    H_teo = lambda w: np.power(H0(w), 2)

    # Getting data from csv
    data = readCSV(file_confC, skiprows=1, cols=[0,1,2,3])
    f = data[0]
    Vin = data[1]
    Vout = data[2]
    phi = -data[3]*f * 360 # phase = deltaT/T * 360
    fig = bodeplot(f, Amp=Vout/Vin, Phase=phi, deg=True)

     # Model
    fline = np.logspace(0, log10(2000), 1000)
    Hline = H_teo(2*np.pi*fline)
    Hline_abs = np.absolute(Hline)
    Hline_phase = np.angle(Hline) * 180/np.pi
    fig = bodeplot(fline, Amp=Hline_abs, Phase=Hline_phase, figure=fig, asline=True)
    
    # plot stile
    ax = fig.axes[0]
    handles,_ = ax.get_legend_handles_labels()
    fig.legend(handles, labels=["Data", "Model"], loc ='lower center', ncol=2)
    fig.subplots_adjust(hspace=0.4, left=0.1)
    plt.tight_layout()
    plt.show()


    # Output impedance
    fig = bodeplot(fline, Amp=np.absolute(Z_osc(2*np.pi*fline)), Phase=np.angle(Z_osc(2*np.pi*fline)), asline=True)
    ax1, ax2 = fig.axes
    ax1.set_ylabel(r"Z [$\Omega$]")
    ax1.set_title(r"$Z_{out}$")
    plt.tight_layout()
    plt.show()