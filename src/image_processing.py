from PIL import Image
import numpy as np


def grayscale_image(image, target):
    # The luminosity of images depend more greatly on the green component more
    # than any other color, at least when it comes to human vision.
    # This is why this blend of components looks better than most
    # traditional true b/w images (i.e, 0.33, 0.33, 0.33)

    # TODO might just get rid of this whole thing in lieu of Image.convert('L')

    r_component = 0.30
    g_component = 0.59
    b_component = 0.11

    raw_image = Image.open(image).convert('RGB')
    raw_image.convert('L').save('better_gray.jpg')
    raw_image.save('normal.jpg')
    image_array = np.array(raw_image)
    # print(image_array[1][1][0])
    for i in range(len(image_array)):
        for j in range(len(image_array[0])):
            image_array[i][j] = r_component * image_array[i][j][0] \
                                + g_component * image_array[i][j][1] \
                                + b_component * image_array[i][j][2]
    #  TODO compress three-value pixel value into one value
    #       This would save a bit of memory but at the moment isn't worth the hassle
    grayscale = Image.fromarray(image_array)
    grayscale.save(target)  # TODO return image instead of saving
    return grayscale


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
