from PIL import Image
import numpy as np
im = Image.open("pineapple-on-beach.jpg")
image_array = np.array(im)
# print(image_array.shape)

char_list = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
for y in image_array:
    for x in y:
        x = (x[0] + x[1] + x[2]) // 3
        print(char_list[x // 4], end='')
    print('')