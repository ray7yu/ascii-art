#!/usr/bin/env python3
from PIL import Image
from subprocess import Popen, PIPE
import numpy as np
import time

p1 = Popen(["imagesnap","-w","2","snapshot.jpg"], stdout=PIPE)
time.sleep(3)
im = Image.open("snapshot.jpg")

while(im.size[0] > 700 or im.size[1]>400):
    im = im.resize((round(im.size[0]*0.75), round(im.size[1]*0.75)))
image_array = np.array(im)

char_list = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
for y in image_array:
    for x in y:
        x = round(0.21*x[0] + 0.72*x[1] + 0.07*x[2])
        print(char_list[x // 4], end='')
        print(char_list[x // 4], end='')
    print('')