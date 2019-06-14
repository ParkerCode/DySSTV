import image_processing as ip
# Easy reading of command-line arguments
# import argparse


def dsstv():
    # image = Image.open('flower.jpg')
    # rgb_image = image.convert('RGB')
    # r, g, b = rgb_image.getpixel((1, 1))
    # print(r, g, b)
    # ip.binary_image('flower.jpg', 'flower.bw.bmp', 64)
    ip.binary_image('flower.jpg', 'bw.jpg', 64)


def main():
    dsstv()


if __name__ == "__main__":
    main()
