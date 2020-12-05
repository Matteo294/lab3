from libphysics import *
import numpy as np

dt = 50
clk = []
D = []
Q = []
Qbar = []

for i in range(9):
    if i%2 == 0:
        for j in range(dt):
            clk.append(0)
    else :
        for j in range(dt):
            clk.append(1)
    if (i%4) == 0 or i%4 == 3:
        for j in range(dt):
            D.append(1)
            Q.append(0)
            Qbar.append(1)
    else:
        for j in range(dt):
            D.append(0)
            Q.append(1)
            Qbar.append(0)
D = np.array(D) - 2
Q = np.array(Q) - 4
Qbar = np.array(Qbar) - 6
plt.plot(clk, c='r', label='CLK')
plt.plot(D, label=r"$D$")
plt.plot(Q, label=r'$Q$')
plt.plot(Qbar, label=r'$\overline{Q}$')
plt.axis('off')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# PART 2 - COUNTER

dt = 50
clk = []
Q0  = []
Q1 = []
Q2 = []

for i in range(19):
    if i%2 == 0:
        for j in range(dt):
            clk.append(1)
    else :
        for j in range(dt):
            clk.append(0)

    if i%4 in [0,1]:
        for j in range(dt):
            Q0.append(0)
    else:
        for j in range(dt):
            Q0.append(1)

    if i%8 in [1, 2, 3, 0]:
        for j in range(dt):
            Q1.append(0)
    else:
        for j in range(dt):
            Q1.append(1)

    if i%16 in [1,2,3,4,5,6,7,0]:
        for j in range(dt):
            Q2.append(0)
    else:
        for j in range(dt):
            Q2.append(1)

Q0 = np.array(Q0) - 2
Q1 = np.array(Q1) - 5
Q2 = np.array(Q2) - 7


plt.plot(clk, c='r', label='CLK')
plt.plot(Q0, label=r"$\overline{Q_0}$")
plt.plot(Q1, label=r'$\overline{Q_1}$')
plt.plot(Q2, label=r'$\overline{Q_2}$')
plt.axis('off')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()