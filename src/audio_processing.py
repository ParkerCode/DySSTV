from scipy import signal as sg
import struct
import numpy as np
import matplotlib.pyplot as plt
import wave

# Matplotlib signal test
# t = np.linspace(0, 1, 500, endpoint=False)
# plt.plot(t, np.sin(2 * np.pi * 5 * t))
# plt.ylim(-2, 2)
# plt.show()

sampling_rate = 44100
freq = 400
channels = 1
sample_width = 2
x = np.arange(sampling_rate)

# Sine
y = 100 * np.sin(2 * np.pi * freq * x / sampling_rate)
# y = 100 * sin(2pi * freq * x / sampling_rate

# Square
# y = 100 * sg.square(2 * np.pi * freq * x / sampling_rate)

# Square with duty cycle
# y = 100 * sg.square(2 * np.pi * freq * x / sampling_rate, duty=0.9)

# Sawtooth
# y = 100 * sg.sawtooth(2 * np.pi * freq * x / sampling_rate)

wav = wave.open('test.wav', 'wb')
wav.setnchannels(channels)
wav.setsampwidth(sample_width)
wav.setframerate(sampling_rate)

for i in y:
    wav.writeframesraw(struct.pack('b', int(i)))
wav.close()

# wave.open('test.wav', mode='rb')

# Use command:
# play -t raw -r 44.1k -e signed -b 8 -c 1 test.wav


