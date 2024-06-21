import numpy as np
from scipy.fft import fft, ifft, fftfreq

class Fourier:
    def transform(f, start, end, step):
        xd = np.array([])
        yd = np.array([])
        for x in np.arange(start, end, step):
            xd = np.append(xd, [x])
            yd = np.append(yd, [f(x)])
        N = int((end-start)*(1/step))
        T = step
        yf = fft(yd)
        xf = fftfreq(N, T)[:N//2]
        return [xf[1:N//2], 2.0/N * np.abs(yf[1:N//2])]

    def inverse(yd, start, end, step):
        N = int((end-start)*(1/step))
        T = step
        yf = ifft(yd)
        xf = fftfreq(N, T)[:N//2]
        return [xf[1:N//2], 2.0/N * np.abs(yf[1:N//2])]
