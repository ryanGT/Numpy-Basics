import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,1,0.01)
y1 = np.sin(2*np.pi*t)

plt.figure(1)
plt.clf()
plt.plot(t,y1)
plt.xlabel('Time (sec.)')
plt.ylabel('$y_1(t)$')
plt.savefig('fig1.png',dpi=200)

y2 = 1.5*np.cos(3*np.pi*t)

plt.figure(2)
plt.clf()
plt.plot(t,y2)
plt.xlabel('Time (sec.)')
plt.ylabel('$y_2(t)$')

y3 = np.sin(4*np.pi*t)
plt.plot(t,y3)
plt.legend(['$y_2$','$y_3$'],loc=3)

plt.savefig('fig2.png',dpi=200)

plt.show()
