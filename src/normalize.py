# Normalizes the images for use in SSTV protocols

import PIL.Image

# jpg = PIL.Image.open('flower.jpg')
# print(jpg.bits, jpg.size, jpg.format)


def stream(image):
    # Mainly test code
    try:
        processed_image = PIL.Image.open(image)
        bit_depth = processed_image.bits
        # size_x = processed_image.size.x
        # print((processed_image.getdata()))
        return bit_depth

        return processed_image
    except FileNotFoundError:
        print("File not found")



