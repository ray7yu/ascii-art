from PIL import Image
import numpy as np
im = Image.open("pineapple-on-beach.jpg")
image_array = np.array(im)
# print(image_array.shape)

while(im.size[0] > 700 or im.size[1]>400):
    im = im.resize((round(im.size[0]*0.75), round(im.size[1]*0.75)))
char_list = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
for y in image_array:
    for x in y:
        x = round(0.21*x[0] + 0.72*x[1] + 0.07*x[2])
        print(char_list[x // 4], end='')
        print(char_list[x // 4], end='')
    print('')