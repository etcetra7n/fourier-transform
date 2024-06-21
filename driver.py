import numpy as np
import matplotlib.pyplot as plt
from fourier import Fourier

def f(x):
    x = 2*np.pi*x
    return (np.sin(2*x)+np.sin(4*x)+np.sin(8*x))

fig, ax = plt.subplots(1, 3, figsize=(16, 5), facecolor = "#2D333B")
xd = np.array([])
yd = np.array([])

for x in np.arange(0, 2, 0.01):
    xd = np.append(xd, [x])
    yd = np.append(yd, [f(x)])

ax[0].plot(xd, yd, color="#81c995")
ax[0].set(xlabel='x', ylabel='f(x)')
ax[0].set_title('2Hz + 4Hz + 8Hz', color="#bdc1c6")
ax[0].set_facecolor("#303134")
ax[0].xaxis.label.set_color("#bdc1c6")
ax[0].yaxis.label.set_color("#bdc1c6")
ax[0].spines['left'].set_color("#3f4245")
ax[0].spines['top'].set_color("#3f4245")
ax[0].spines['right'].set_color("#3f4245")
ax[0].spines['bottom'].set_color("#3f4245")
ax[0].tick_params(axis='x', colors="#929296") #"#929296"
ax[0].tick_params(axis='y', colors="#929296")
ax[0].grid(True, color="#3f4245", linestyle=':', linewidth=1) #"#3f4245"

x, y = Fourier.transform(f, 0, 10, 0.01)
ax[1].plot(x[:100], y[:100], color="#81c995")
ax[1].set(xlabel='Frequency', ylabel='Probability')
ax[1].set_title('Fourier Transform', color="#bdc1c6")
ax[1].set_facecolor("#303134")
ax[1].xaxis.label.set_color("#bdc1c6")
ax[1].yaxis.label.set_color("#bdc1c6")
ax[1].spines['left'].set_color("#3f4245")
ax[1].spines['top'].set_color("#3f4245")
ax[1].spines['right'].set_color("#3f4245")
ax[1].spines['bottom'].set_color("#3f4245")
ax[1].tick_params(axis='x', colors="#929296") #"#929296"
ax[1].tick_params(axis='y', colors="#929296")
ax[1].grid(True, color="#3f4245", linestyle=':', linewidth=1) #"#3f4245"

ix, iy = Fourier.inverse(y, 0, 10, 0.01)
ax[2].plot(ix[:100], iy[:100], color="#81c995")
ax[2].set(xlabel='F(x)', ylabel='F\'(F(x))')
ax[2].set_title('Fourier Inverse', color="#bdc1c6")
ax[2].set_facecolor("#303134")
ax[2].xaxis.label.set_color("#bdc1c6")
ax[2].yaxis.label.set_color("#bdc1c6")
ax[2].spines['left'].set_color("#3f4245")
ax[2].spines['top'].set_color("#3f4245")
ax[2].spines['right'].set_color("#3f4245")
ax[2].spines['bottom'].set_color("#3f4245")
ax[2].tick_params(axis='x', colors="#929296") #"#929296"
ax[2].tick_params(axis='y', colors="#929296")
ax[2].grid(True, color="#3f4245", linestyle=':', linewidth=1) #"#3f4245"

fig.savefig('fft_demonstration.png')
plt.show()
