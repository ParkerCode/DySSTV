import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import wave


def convert_image(image_path):
    raw_img = Image.open(image_path)
    raw_img.load()
    data = np.asarray(raw_img, dtype=int)
    return data


def save_image(npdata, out_file):
    # img = Image.fromarray(np.asanyarray(np.clip(npdata, 0, 255), dtype='int'), 'L')
    img = Image.frombuffer(npdata.size, npdata)
    img.save(out_file)


array = convert_image('../data/flower.gray.jpg')
# for i in array:
#     for j in array[0]:
#         array[i][j] = int(array[i][j])/4
plt.figure(1)
plt.title('Image')
compressor_value = 128
array = array/compressor_value
array = np.around(array, 0)
plt.imshow(array, cmap='gray', interpolation='nearest', vmin=0, vmax=255/compressor_value)
plt.imsave('../data/flower.gray.compressed.bmp', array, cmap='gray', vmin=0, vmax=255/compressor_value)
array = array.flatten()
print(array)
print(len(array))
# plt.show()
