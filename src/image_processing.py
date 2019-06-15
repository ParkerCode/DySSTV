from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


# Retrieves data from images for pixel processing
# img = mpimg.imread('flower.jpg')
# gray = rgb2gray(img)
# mpimg.imsave('flower.png', img)
# plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
# plt.show()
