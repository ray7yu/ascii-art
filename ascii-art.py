from PIL import Image
import numpy as np
im = Image.open("pineapple-on-beach.jpg")
image_array = np.array(im)
# print(image_array.shape)