from scipy import signal as sg
import struct
import numpy as np
import matplotlib.pyplot as plt

# Matplotlib signal test
t = np.linspace(0, 1, 500, endpoint=False)
plt.plot(t, np.sin(2 * np.pi * 5 * t))
plt.ylim(-2, 2)
plt.show()


sampling_rate = 44100
freq = 1500
samples = 44100
x = np.arange(samples)

# Sine
y = 100 * np.sin(2 * np.pi * freq * x / sampling_rate)

# Square
# y = 100 * sg.square(2 * np.pi * freq * x / sampling_rate)

# Square with duty cycle
# y = 100 * sg.square(2 * np.pi * freq * x / sampling_rate, duty=0.9)

# Sawtooth
# y = 100 * sg.sawtooth(2 * np.pi * freq * x / sampling_rate)

f = open('test.wav', 'wb')

for i in y:
    f.write(struct.pack('b', int(i)))
f.close()

# Use command:
# play -t raw -r 44.1k -e signed -b 8 -c 1 test.wav
