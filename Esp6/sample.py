from libphysics import *

file = "Waveforms/Sine/scope_0.csv"

def sample(file, eps):
    ''' Calculates the sampling points '''
    t, Vin, V = readCSV(file, skiprows = 5)

    samples = []
    ts = []

    i = 1

    #-----------------------------------------------
    # REMOVE ISOLATED POINTS
    toremove = []
    while(i<len(V)-1):
        if (abs(V[i]-V[i-1]) > 0.05 and abs(V[i]-V[i+1]) > 0.05):
            toremove.append(i)
        i += 1

    toremove.sort(reverse=True)

    for idx in toremove:
        t = np.delete(t, idx)
        V = np.delete(V, idx)
        Vin = np.delete(Vin, idx)
    #------------------------------------------------
    # FIND THE VALUE OF THE SAMPLES
    i = 0
    last = 0
    eps = 0.07

    while(i < len(V)-1):
        if (abs(V[i]-V[i+1])> eps or (abs(V[i+1]-V[last]) > 0.02 and i-last >= 38)): # the cases in which i found a "new plateu"
            ts.append(t[i+1])
            samples.append(V[i+1])
            last = i+1
            i +=1
            
        else:
            i += 1


    ts = numpify(ts)
    samples = numpify(samples)

    return t, Vin, V, ts, samples
