from matplotlib import pyplot as plt 
import numpy as np 
import sys

R1 = 1e6
R2 = 100
R = 100e3
C = 10e-9
tau = R*C 
K = R2/(R1+R2)
eps = 0.03 # vary eps to obatin visible plots
R = 1

color1 = "springgreen"
color2 = "red"
color3 = "deepskyblue"

# Imaginary of the intersection points
y_inter1 = 2*K/(eps*tau) # intersection with the smaller circle
y_inter2 = 2*K/(R*tau) # intersection with the larger circle


''' Modified Nyquist Path '''
# Semicircles
t = np.linspace(-np.pi/2, np.pi/2, 1000)
xeps = eps*np.cos(t)
yeps = eps*np.sin(t)
xR = R*np.cos(t)
yR = R*np.sin(t)
# Segments
ys1 = np.linspace(-R, -eps, 1000)
ys2 = np.linspace(eps, R, 1000)
xs = np.zeros(len(ys1))
# Plots
plt.plot(xs, ys1, color=color1, linewidth=2.5)
plt.plot(xs, ys2, color=color1, linewidth=2.5)
plt.plot(xeps, yeps, color=color2, linewidth=2.5)
plt.plot(xR, yR, color=color3)
plt.axis("equal")
plt.xlabel(r"$\mathcal{R}\mathcal{e}(z)$", fontsize=20)
plt.ylabel(r"$\mathcal{I}\mathcal{m}(z)$", fontsize=20)
ax=plt.gca()
ax.get_xaxis().set_ticks([0])
ax.get_yaxis().set_ticks([0])
plt.show()

''' Normal plot '''
# Larger circle
theta1 = np.linspace(np.pi/2, -np.pi/2, 1000)
g1 = (1+2*K*eps*tau*np.exp(1j*theta1))/(eps**2*tau**2*np.exp(2j*theta1))
x1 = np.real(g1)
y1 = np.imag(g1)
# Smaller circle
theta2 = np.linspace(-np.pi/2, np.pi/2, 1000)
g2 = (1+2*K*R*tau*np.exp(1j*theta2))/(R**2*tau**2*np.exp(2j*theta2))
x2 = np.real(g2)
y2 = np.imag(g2)
ya = np.linspace(-y_inter2, -y_inter1, 1000)
yb = np.linspace(y_inter1, y_inter2, 1000)
xa = -1/(4*K**2)*ya**2
xb = -1/(4*K**2)*yb**2
# Plot
plt.plot(x1, y1, '--', color=color3, linewidth=2.0)
plt.plot(x2, y2, color=color1, linewidth=2.0)
plt.plot(xa, ya, color=color2, linewidth=2.0)
plt.plot(xb, yb, color=color2, linewidth=2.0)
# Center axis and other options
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xlabel(r"$\mathcal{R}\mathcal{e}(z)$", fontsize=20)
plt.ylabel(r"$\mathcal{I}\mathcal{m}(z)$", fontsize=20)
ax.xaxis.set_label_coords(0.95,0.5)
ax.yaxis.set_label_coords(0.5,0.95)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.set_xlim(min(xa)-10000000, max(x1)+10000000)
ax.set_ylim(min(y1)-10000000, max(y1)+10000000)
plt.show()


''' Zoomed plot '''
# Smaller circle: upper and lower parts
theta1 = np.linspace(np.pi/2, 1/2.2*np.pi, 1000)
theta2 = np.linspace(-1/2.2*np.pi, -np.pi/2, 1000)
g1 = (1+2*K*R*tau*np.exp(1j*theta1))/(R**2*tau**2*np.exp(2j*theta1))
g2 = (1+2*K*R*tau*np.exp(1j*theta2))/(R**2*tau**2*np.exp(2j*theta2))
x1 = np.real(g1)
y1 = np.imag(g1)
x2 = np.real(g2)
y2 = np.imag(g2)
# Parabola
ya = np.linspace(y_inter2, 1.5*y_inter2, 1000)
yb = np.linspace(-y_inter2, -1.5*y_inter2, 1000)
xa = -1/(4*K**2)*ya**2
xb = -1/(4*K**2)*yb**2
# Plots
plt.plot(x1, y1, color=color1, linewidth=2.0)
plt.plot(x2, y2, color=color1, linewidth=2.0)
plt.plot(xa, ya, color=color2, linewidth=2.0)
plt.plot(xb, yb, color=color2, linewidth=2.0)
# Center axis and other options
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_label_coords(1,0.5)
ax.yaxis.set_label_coords(0.5,1)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
plt.axis("equal")
plt.show()