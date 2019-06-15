import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import wave


def grayscale_image(image, title, r, g, b):
    # The luminosity of images depend more greatly on the green component more
    # than any other color, at least when it comes to human vision.
    # This is why this blend of components looks better than most
    # traditional true b/w images (i.e, 0.33, 0.33, 0.33)

    # TODO might just get rid of this whole thing in lieu of Image.convert('L')

    # r_component = 0.30
    # g_component = 0.59
    # b_component = 0.11
    r_component = r
    g_component = g
    b_component = b

    raw_image = Image.open(image).convert('RGB')
    image_array = np.array(raw_image)
    # print(image_array[1][1][0])
    # for i in range(len(image_array)):
    #     for j in range(len(image_array[0])):
    #         image_array[i][j] = r_component * image_array[i][j][0] \
    #                             + g_component * image_array[i][j][1] \
    #                             + b_component * image_array[i][j][2]

    for i in range(len(image_array)):
        for j in range(len(image_array[0])):
            image_array[i][j][0] = r_component * image_array[i][j][0]
            image_array[i][j][1] = g_component * image_array[i][j][1]
            image_array[i][j][2] = b_component * image_array[i][j][2]
    #  TODO compress three-value pixel value into one value
    #       This would save a bit of memory but at the moment isn't worth the hassle
    grayscale = Image.fromarray(image_array)
    grayscale.convert('RGB')
    grayscale.save(image + title + '.jpg', quality=100, optimize=True, progressive=True)
    # plt.figure(1)
    # plt.title(title)
    # plt.imshow(grayscale)

    # return grayscale


path = '../data/field test/play/00field.jpg'
grayscale_image(path, 'Red', 1.00, 0.00, 0.00)
grayscale_image(path, 'Green', 0.00, 1.00, 0.00)
grayscale_image(path, 'Blue', 0.00, 0.00, 1.00)
grayscale_image(path, 'Gray', 0.30, 0.59, 0.11)
grayscale_image(path, 'TrueGray', 0.333, 0.333, 0.333)
