# gabor_chirps.py
#
# Author: Ronaldo de Freitas Zampolo
# Date: 20 Apr. 2022

import numpy as np
import matplotlib.pyplot as plt
import scipy.fft

t_ini = -3  # initial time
t_fin =  10 # final time
L = 1024    # number of samples
T = (t_fin - t_ini)/L # sampling period
fs = 1/T    # sampling frequency

t = np.linspace( t_ini, t_fin, L ) # time vector

# Gabor chirp parameters 
xi = 20 # frequency shift
a = 1   # scaling factor
b = 10   # time decay
u = 3   # time shift

# Gabor chirp function
# define different functions with params variations
f = a * np.exp(1j*xi*t -b*(t-u)**2)

# Plot time function
# tdl: axis labels, title, save figure
plt.figure()
plt.plot(t,np.real(f), color = 'blue')
plt.plot(t,np.imag(f), color = 'red')
plt.plot(t,np.abs(f), color = 'magenta')
#plt.plot(t,np.unwrap(np.angle(f)), color = 'green')
plt.grid(True)
#plt.show()


# FFT calculation
F = scipy.fft.fftshift(scipy.fft.fft(f,n=L))
w = np.linspace(-np.pi*fs, np.pi*fs, L) 

# Plot fft
# tdl: axis labels, title, save figure
plt.figure()
#plt.plot(w,np.real(f), color = 'blue')
#plt.plot(w,np.imag(f), color = 'red')
plt.plot(w,np.abs(F), color = 'magenta')
#plt.plot(t,np.unwrap(np.angle(f)), color = 'green')
plt.grid(True)
plt.show()
