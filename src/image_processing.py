from PIL import Image
import numpy as np


def binary_image(image, target, threshold):
    # Converts image to a binary image
    # The threshold will determine the strength of the effect.
    # 0 => Pure White(255), 255 = Pure Black(000)
    raw_image = Image.open(image)
    mono_image = raw_image.convert('L')  # Converts to grayscale
    mono_image = np.array(mono_image)

    # Converts grayscale pixel array into binary (0 OR 255 brightness)
    for i in range(len(mono_image)):
        for j in range(len(mono_image[0])):
            if mono_image[i][j] > threshold:
                mono_image[i][j] = 255
            else:
                mono_image[i][j] = 0

    mono_image = Image.fromarray(mono_image)
    mono_image.save(target)
