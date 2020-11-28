from libphysics import *
from sample import sample
from math import *
import sys
from scipy.optimize import curve_fit

#--------------------------------------------------
# SAMPLING OF SINUSOIDAL WAVES
#--------------------------------------------------

#--------------------------------------------------
# LOOP PARAMETERS
files_sine = ['Waveforms/Sine/scope_' + str(i) + '.csv' for i in range(4)]
eps = [0.3, 0.5, 0.6, 0.7]
f = [50, 100, 200, 900]
titles = [r"$f = $" + str(freq) + " Hz" for freq in f]

#--------------------------------------------------
# DEFINE THE FIGURES AND SOME VARS FOR FIGURES
idx_for_subplots = [(0,0), (0,1), (1, 0), (1,1)]
fig_sine_sinc = plt.figure(1)
fig_sine_lin = plt.figure(2)
gs_sine_sinc = fig_sine_sinc.add_gridspec(2, 2)
gs_sine_lin = fig_sine_lin.add_gridspec(2, 2)
# fig_sh = plt.figure(1)


for (i, file) in enumerate(files_sine):
    #--------------------------------------------------
    # USE THE SAMPLING FUNCTION
    t, Vin, V, ts, Vs = sample(file, eps[i])
    t = t - ts[0]
    ts = ts - ts[0]
    # if i == 1:
        # plt.figure(1)
        # plt.plot(t, Vin, label="Signal", c='k')
        # plt.plot(t, V, label=r"S\&H", c='r')
        # plt.plot(ts, Vs, '.', ms=16, label="Recognized samples", c='royalblue')
        # plt.xlabel(r"$t$ [s]")
        # plt.ylabel(r"[V]")
        # plt.legend(bbox_to_anchor=(0.9, -0.3), ncol=3)
        # plt.tight_layout()
        # plt.show()
    #--------------------------------------------------
    #--------------------------------------------------
    # RECONSTRUCT THE FUNCTION
    dts = numpify([ts[i+1]-ts[i] for i in range(len(ts)-1)]) # find sampling period by averaging over the time intervals
    Ts = np.average(dts)    # sample period
    fs = 1/Ts               # sample freq
    n = np.arange(len(Vs))
    t_line = np.linspace(t[0], t[-1], 5000)
    #--------------------------------------------------
    # WITH SINC
    ksinc = lambda x: np.sin(pi*x/Ts)/ (pi*x/Ts)
    r_sinc = lambda t: np.sum(Vs * ksinc(t - n*Ts))
    r_sinc = numpify([r_sinc(t) for t in t_line])

    # # extract frequency for the aliasing of the 900 hertz signal
    # sinefit = lambda x, A, w: np.sin(w*x) + A*np.cos(w*x)
    # if i == 3:
    #     fit = curve_fit(sinefit, t_line[1000:4000], r_sinc[1000:4000])
    #     [A, w] = fit[0]
    #     print("\nSine wave at 900 Hz: the frequency of the reconstructed function is {} Hz".format(w/(2*pi)))
    #     plt.figure()
    #     plt.plot(t_line, r_sinc)
    #     plt.plot(t_line[1000:4000], sinefit(t_line[1000:4000], A, w))
    #     plt.show()
    #--------------------------------------------------
    # WITH LINEAR KERNEL
    def klin(x):
        output = np.zeros(len(x))
        for i, el in enumerate(x):
            if abs(el) <= Ts:
                output[i] = (Ts- abs(el))/Ts
            else:
                output[i] = 0
        return output

    r_lin = lambda t: np.sum(Vs * klin(t - n*Ts))
    r_lin = numpify([r_lin(t) for t in t_line])
    #---------------------------------------------------
    #---------------------------------------------------
    # PLOT THE SAMPLING WITH SINC
    plot_sinc = fig_sine_sinc.add_subplot(gs_sine_sinc[idx_for_subplots[i]])
    psignal_s, = plot_sinc.plot(t, Vin, c ='gray', lw=1.5,label = "Signal")
    psample_s, =  plot_sinc.plot(ts, Vs, '.', markersize=7, c='black', label="Samples")
    palias_s, = plot_sinc.plot(t_line, r_sinc, c='red', label="Reconstruction")
    plot_sinc.set_title(titles[i])
    plot_sinc.set_xlabel(r"$t$ [s]")
    plot_sinc.set_ylabel(r"[V]")
    #---------------------------------------------------
    # PLOT THE SAMPLING WITH LINEAR KERNEL
    plot_lin = fig_sine_lin.add_subplot(gs_sine_lin[idx_for_subplots[i]])
    psignal_l, = plot_lin.plot(t, Vin, c ='gray', lw=1.5, label = "Signal")
    psample_l, =  plot_lin.plot(ts, Vs, '.', markersize=5, c='k', label="Samples")
    palias_l, = plot_lin.plot(t_line, r_lin, c='red', label="Reconstruction")
    plot_lin.set_title(titles[i])
    plot_lin.set_xlabel(r"$t$ [s]")
    plot_lin.set_ylabel(r"[V]")
    
fig_sine_sinc.subplots_adjust(bottom=0.210, hspace=0.5, top=0.945, left=0.085, right=0.945)
plot_sinc.legend(handles=[psignal_s, psample_s, palias_s], bbox_to_anchor=(0.5, -0.3), ncol=3)
plot_lin.legend(handles=[psignal_l, psample_l, palias_l], bbox_to_anchor=(0.5, -0.3), ncol=3)
fig_sine_lin.subplots_adjust(bottom=0.210, hspace=0.5, top=0.945, left=0.085, right=0.945)



#--------------------------------------------------
# SAMPLING OF TRIANGULAR WAVES
#--------------------------------------------------    

#--------------------------------------------------
# LOOP PARAMETERS
files_triang = ['Waveforms/Triangular/scope_' + str(i+4) + '.csv' for i in range(4)]
eps = [0.3, 0.5, 0.4, 0.7]
f = [50, 100, 200, 900]
titles = [r"$f = $" + str(freq) + " Hz" for freq in f]

#--------------------------------------------------
# DEFINE THE FIGURES AND SOME VARS FOR FIGURES
idx_for_subplots = [(0,0), (0,1), (1, 0), (1,1)]
fig_triang_sinc = plt.figure(3)
fig_triang_lin = plt.figure(4)
gs_triang_sinc = fig_triang_sinc.add_gridspec(2, 2)
gs_triang_lin = fig_triang_lin.add_gridspec(2, 2)


for (i, file) in enumerate(files_triang):
    #--------------------------------------------------
    # USE THE SAMPLING FUNCTION
    t, Vin, V, ts, Vs = sample(file, eps[i])
    t = t - ts[0]
    ts = ts - ts[0]
    #--------------------------------------------------
    #--------------------------------------------------
    # RECONSTRUCT THE FUNCTION
    dts = numpify([ts[i+1]-ts[i] for i in range(len(ts)-1)]) # find sampling period by averaging over the time intervals
    Ts = np.average(dts)    # sample period
    fs = 1/Ts               # sample freq
    n = np.arange(len(Vs))
    t_line = np.linspace(t[0], t[-1], 5000)
    #--------------------------------------------------
    # WITH SINC
    ksinc = lambda x: np.sin(pi*x/Ts)/ (pi*x/Ts)
    r_sinc = lambda t: np.sum(Vs * ksinc(t - n*Ts))
    r_sinc = numpify([r_sinc(t) for t in t_line])
    #--------------------------------------------------
    # WITH LINEAR KERNEL
    def klin(x):
        output = np.zeros(len(x))
        for i, el in enumerate(x):
            if abs(el) <= Ts:
                output[i] = (Ts- abs(el))/Ts
            else:
                output[i] = 0
        return output
    r_lin = lambda t: np.sum(Vs * klin(t - n*Ts))
    r_lin = numpify([r_lin(t) for t in t_line])
    #---------------------------------------------------
    #---------------------------------------------------
    # PLOT THE SAMPLING WITH SINC
    plot_sinc = fig_triang_sinc.add_subplot(gs_sine_sinc[idx_for_subplots[i]])
    psignal_s, = plot_sinc.plot(t, Vin, c ='gray', lw=1.5,label = "Signal")
    # ptest_s = plot_sinc.plot(t, V, c ='blue', lw=1.5,label = "Original Sampling") uncomment to see the original sampling wave (square wave)
    psample_s, =  plot_sinc.plot(ts, Vs, '.', markersize=7, c='black', label="Samples")
    palias_s, = plot_sinc.plot(t_line, r_sinc, c='red', label="Reconstruction")
    plot_sinc.set_title(titles[i])
    plot_sinc.set_xlabel(r"$t$ [s]")
    plot_sinc.set_ylabel(r"[V]")
    #---------------------------------------------------
    # PLOT THE SAMPLING WITH LINEAR KERNEL
    plot_lin = fig_triang_lin.add_subplot(gs_sine_lin[idx_for_subplots[i]])
    psignal_l, = plot_lin.plot(t, Vin, c ='gray', lw=1.5, label = "Signal")
    psample_l, =  plot_lin.plot(ts, Vs, '.', markersize=5, c='k', label="Samples")
    palias_l, = plot_lin.plot(t_line, r_lin, c='red', label="Reconstruction")
    plot_lin.set_title(titles[i])
    plot_lin.set_xlabel(r"$t$ [s]")
    plot_lin.set_ylabel(r"[V]")
    
fig_triang_sinc.subplots_adjust(bottom=0.210, hspace=0.5, top=0.945, left=0.085, right=0.945)
plot_sinc.legend(handles=[psignal_s, psample_s, palias_s], bbox_to_anchor=(0.5, -0.3), ncol=3)
plot_lin.legend(handles=[psignal_l, psample_l, palias_l], bbox_to_anchor=(0.5, -0.3), ncol=3)
fig_triang_lin.subplots_adjust(bottom=0.210, hspace=0.5, top=0.945, left=0.085, right=0.945)
plt.show()


    


