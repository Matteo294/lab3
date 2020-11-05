from matplotlib import pyplot as plt 
import numpy as np 

R1 = 1e6
R2 = 100
R = 100e3
C = 10e-9
K = R2/(R1+R2)

y = np.concatenate((-np.logspace(4, 0, 1000), np.logspace(0, 4, 1000))) # Im(z)
x = -1/(4*K**2) * y**2 # Re(z)

plt.plot(x, y)
# Origin axes
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xlabel(r"$\mathcal{R}\mathcal{e}(Z)$")
plt.ylabel(r"$\mathcal{I}\mathcal{m}(Z)$")
plt.show()