from uncertainties import ufloat as uf
from math import pi, sqrt

# harmonic oscillator with original values
dt = uf(6.30, 0.01)*1e-3
w = 2*pi/dt
print("\nHarmonic oscillator with original values\n")
print("w0 = {}\n".format(w))

# harmonic oscillator with modified inverting gain
dt = uf(4.26, 0.01)*1e-3
w = 2*pi/dt
w_teo = 1e3*sqrt(2)
print("Harmonic oscillator with modified inverting gain")
print("R1 = 10k\t R2 = 22k\t w0 = {}\n".format(w))
print("Expected w = {}\n". format(w_teo))

# harmonic oscillator with different C
dt = uf(617e-6, 0.01e-6)
w = 2*pi/dt
print("w0 = {}\n".format(w))