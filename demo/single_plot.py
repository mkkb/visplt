import visplt.visplt as plt
import numpy as np

def main():
    N = 2**17
    Fs = 200e3
    f0 = 2e3
    f1 = 15e3

    t = np.arange(N)/Fs
    y = np.cos(2*np.pi*f0*t) + np.sin(2*np.pi*f1*t)

    plt.figure('A vispy plot')
    plt.plot(t, y, label='Sinus')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude [V]')

    plt.show()


if __name__ == '__main__':
    main()
