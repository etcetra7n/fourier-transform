import numpy as np
import matplotlib.pyplot as plt
from fourier import Fourier

def f(x):
    x = 2*np.pi*x
    return (np.sin(2*x)+np.sin(4*x)+np.sin(8*x))

fig, ax = plt.subplots(1, 3, figsize=(16, 5))
xd = np.array([])
yd = np.array([])

for x in np.arange(0, 2, 0.01):
    xd = np.append(xd, [x])
    yd = np.append(yd, [f(x)])

ax[0].plot(xd, yd)
ax[0].set(xlabel='x', ylabel='f(x)')
ax[0].set_title('2Hz + 4Hz + 8Hz')
ax[0].grid() #"#3f4245"

x, y = Fourier.transform(f, 0, 10, 0.01)
ax[1].plot(x[:100], y[:100])
ax[1].set(xlabel='Frequency', ylabel='Probability')
ax[1].set_title('Fourier Transform')
ax[1].grid() #"#3f4245"

ix, iy = Fourier.inverse(y, 0, 10, 0.01)
ax[2].plot(ix[:100], iy[:100])
ax[2].set(xlabel='F(x)', ylabel='F\'(F(x))')
ax[2].set_title('Fourier Inverse')
ax[2].grid() #"#3f4245"

fig.savefig('fft_demonstration.png')
plt.show()
