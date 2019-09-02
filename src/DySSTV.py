__author__ = "John Parker"
__version__ = "v0.0.4"

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import wave
import os
import math
import struct
import random
from itertools import *
import argparse


def vis_code_generator():
    # Generates the VIS code for identification at the beginning of the signal.
    """
    TODO Hard 15 bit limit on sizes?
    Could be 32767^2 pixels in resolution, that's probably enough.
        Possible implementation:
        1 000000000000000 000000000000000 0
        This is really important so might need more parity bits

    """

    # Signal frequency for transmitting binary data
    # 1300 is logical 0, 1100 is logical 1, 1200 is for stop bits
    signal_low, signal_mid, signal_high = \
        [1300, 1200, 1100]
    # Tones used for luminosity/color transmission and syncronization of signal
    # 1500 is black, 1900 is gray, 2300 is white
    tone_low, tone_mid, tone_high = \
        [1500, 1900, 2300]


def image_np_array(image, mode):
    # TODO Remove, or find use for.
    raw_image = Image.open(image).convert(mode)
    image_array = np.array(raw_image)

    return image_array


# Converts an image to its YCbCr components
def y_cb_cr_breakdown(image_path):
    # TODO Remove.
    # Just so I don't forget how to do this
    image = np.array(Image.open(image_path).convert('YCbCr'))
    image_y = Image.fromarray(image[:, :, 0])
    image_cb = Image.fromarray(image[:, :, 1])
    image_cr = Image.fromarray(image[:, :, 2])

    # Use this to glue them back together
    Image.merge('YCbCr', [image_y, image_cb, image_cr]).show()


# Takes in wav file and returns sanitized np.array of waveform.
def input_wav_mono(audio):
    with wave.open(audio, 'r') as audio_data:
        signal = audio_data.readframes(-1)
        signal = np.fromstring(signal, np.int16)

        if audio_data.getnchannels() is 2:
            signal = np.array(signal[::2])

        return signal


# Calculate parity of binary VIS code
def parity_bit(binary_string):
    b_count = 0
    for i in range(len(binary_string)):
        b_count += int(binary_string[i])

    if b_count % 2 == 0:
        return 0
    else:
        return 1


# Converts a one-dimensional array of numbers to a waveform
def output_wav(array):
    output_file = wave.open('./data/temp/output.wav', mode='wb')
    output_file.setparams([1, 2, 44100, 0, 'NONE', 'NONE'])
    output_file.writeframesraw(array)
    output_file.close()


def input_wav(size, file):
    # TODO convert waveform to binary data, possibly useless
    input_file = wave.open(file, mode='rb')
    image_array = np.frombuffer(input_file.readframes(-1), np.uint8)
    image_array = image_array.reshape(size)
    Image.fromarray(image_array).show()


# Removes any temporary files created during the encoding or decoding
def cleanup():
    print("Cleaning up temporary files...")
    directory = './data/temp/'
    filelist = [f for f in os.listdir(directory) if not f.endswith(".remove")]
    for f in filelist:
        os.remove(os.path.join(directory, f))
    exit(0)


def main():
    # parser = argparse.ArgumentParser(description='Dynamic SSTV, encode images in an array of formats')
    # parser.add_argument('Image', metavar='I', help='Image file input. BMP, JPG, and PNG supported')
    # args = parser.parse_args()
    # image = image_np_array('./data/galgun.jpg', 'RGB')
    # output_wav(image)
    # input_wav((1920, 1080, 3), './data/temp/output.wav')
    # input_wav(image.shape, './data/temp/output.wav')
    # cleanup()

    # sample = 410
    # max_amplitude = 32767.0
    # samples = (int(sample * max_amplitude) for sample in samples)
    pass


if __name__ == '__main__':
    main()
