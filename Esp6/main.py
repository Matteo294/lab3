from libphysics import *
from sample import sample
from math import *

files = ['Waveforms/Sine/scope_' + str(i) + '.csv' for i in range(4)]
eps = [0.3, 0.5, 0.6, 0.7]
f = [50, 100, 200, 900]
titles = ["f = " + str(freq) + " Hz" for freq in f]
for (i, f) in enumerate(files):
    #---------------------------------------
    # USE THE SAMPLING FUNCTION
    t, V, ts, Vs = sample(f, eps[i])

    # plt.plot(t, V, c='k')
    # plt.scatter(ts, Vs, c='r')
    # plt.show()

    #----------------------------------------
    # RECONSTRUCT THE FUNCTION WITH SINC
    dts = numpify([ts[i+1]-ts[i] for i in range(len(ts)-1)]) # find sampling period by averaging over the time intervals
    Ts = np.average(dts)
    fs = 1/Ts

    ksinc = lambda x: np.sin(pi*x/Ts)/ (pi*x/Ts)

    n = np.arange(len(Vs))

    r = lambda t: np.sum(Vs * ksinc(t - n*Ts))

    t_line = np.linspace(t[0], t[-1], 5000)
    r = numpify([r(t) for t in t_line])

    plt.plot(t, V, c='k')
    plt.scatter(ts, Vs, c='r')
    plt.plot(t_line, r)
    plt.title(titles[i])
    plt.show()

    


