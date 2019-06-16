import matplotlib.pyplot as plt
import sys
import numpy as np
import wave

waveform = wave.open('test_sstv.bmp.bw8.data.wav', 'r')
print(waveform.getnframes())
print(waveform.getframerate())
print(waveform.getsampwidth())

# Extract the raw audio frames
signal = waveform.readframes(-1)
signal = np.frombuffer(signal, dtype=int, count=40000, offset=0)


if waveform.getnchannels() == 2:
    print("Error: Mono files only")
    sys.exit()

waveform_out = wave.open('test_chunk.wav', 'w')
waveform_out.setnchannels(1)
waveform_out.setframerate(11025)
waveform_out.setsampwidth(2)
waveform_out.writeframes(signal)
waveform_out.close()

plt.figure(1)
plt.title('Audio Waveform')
plt.plot(signal)
plt.show()
