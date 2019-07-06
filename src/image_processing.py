import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import wave
import sys
import os
# import pysnooper


# @pysnooper.snoop()
def image_np_array(image):
    raw_image = (
        Image.open(image)
        .convert('RGB')
    )

    image_array = np.array(raw_image)

    raw_image = Image.fromarray(image_array).convert('RGB')
    print(image_array)

    raw_image.show()
    # raw_image.save(image[:-4] + '.8' + '.png', optimize=True)


def wave_processing(audio):
    with wave.open(audio, 'r') as spf:
        signal = spf.readframes(-1)
        signal = np.fromstring(signal, np.int16)

        # Convert stereo waveform to mono, if necessary
        if spf.getnchannels() is 2:
            signal = np.array(signal[::2])

        return signal
