__author__ = "John Parker"
__version__ = "v0.0.1"

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import wave
import argparse


def image_np_array(image, mode):
    raw_image = Image.open(image).convert(mode)
    image_array = np.array(raw_image)

    return image_array


# Returns mono waveform data as ndarray
# Most SSTV protocols only support mono waveforms
def input_wav_mono(audio):
    with wave.open(audio, 'r') as audio_data:
        signal = audio_data.readframes(-1)
        signal = np.fromstring(signal, np.int16)

        if audio_data.getnchannels() is 2:
            signal = np.array(signal[::2])

        return signal


def output_wav(size, data):
    # TODO create custom wave file that encodes image dimensions
    output_file = wave.open('./data/temp/output.wav', mode='wb')
    output_file.setnchannels(1)
    output_file.setsampwidth(2)
    output_file.setframerate(11050)
    output_file.writeframes(data)
    output_file.close()


def input_wav(file):
    # TODO convert waveform to binary data
    input_file = wave.open(file, mode='rb')
    image_array = np.frombuffer(input_file.readframes(-1), np.uint8)
    image_array = image_array.reshape(256, 320, 3)
    Image.fromarray(image_array).show()


def main():
    # parser = argparse.ArgumentParser(description='Dynamic SSTV, encode images in an array of formats')
    # parser.add_argument('Image', metavar='I', help='Image file input. BMP, JPG, and PNG supported')
    # args = parser.parse_args()
    image = image_np_array('./data/flower.jpg', 'RGB')
    output_wav(image.shape, image)
    input_wav('./data/temp/output.wav')


if __name__ == '__main__':
    main()
