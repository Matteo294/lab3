'''	
	sinFit: fit a sine wave to extract amplitude.
	
	INPUTS:
		- t: time array
		- V: voltage array
		- f: sine frequency
		- dV: uncertainties in V. If not given V/100 is assumed
		- shoplots: True to show fit plot
	RETURNS:
		- amplitude of the sine wave
'''

from libphysics import *
import numpy as np

def sinFit(t, V, f, dV=None, showplots=False):
	if dV is None:
		dV = numpify(np.full(len(V), max(V)/100)) # Assigns 1% error if not given (always nice)
	else:
		if isinstance(dV, (int, float)):
			dV = np.full(len(V), dV)
		else:
			if len(dV) != len(V):
				print("dV and V's lengths do not match")
			else:
				dV = numpify(dV)
	w = 2*np.pi*f
	# Prepare features matrix
	M = np.zeros((len(V), 3))
	M[:,0] = np.ones(len(V))
	M[:,1] = np.cos(w*t)
	M[:,2] = np.sin(w*t)
	V_fit = lsq_fit(V, M, dV)
	C, A, B = V_fit["fit_out"]
	ampl = np.absolute(A-1j*B)	
	if showplots:
		plt.plot(t, V, '.', label='data')
		plt.plot(t, C + A*M[:,1] + B*M[:,2], label='fit')
		plt.legend()
		plt.grid()
		plt.title("Sin fit results")
		plt.show()
	if isinstance(ampl, np.ndarray):
		ampl = ampl[0]
	return ampl 
	
	
