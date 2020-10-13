from scipy.optimize import curve_fit as fit
import numpy as np

# Is, n fit parameters. Assuming Vt = 25.4 mV (22°C)
def shockley(V, n, Is):
    return Is*np.exp(V/(n*25.4e-3) - 1)

def shockley_fit(I, V):
    params = fit(shockley, V, I, )
    n = params[0][0]
    Is = params[0][1]
    return [n, Is]
