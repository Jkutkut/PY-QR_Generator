#!/usr/bin/env python3

import sys
from PIL import Image, ImageDraw

# Constants
BG = (255, 255, 255)
SIZE = (128, 128)

# with Image.open("hopper.jpg") as im:
with Image.new('RGB', SIZE, color=BG) as im:

    draw = ImageDraw.Draw(im)



	# Debug cross
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)

    # write to stdout
    im.save("qr.png")

print("Thanks for using this code, I hope you liked it.")
print("See more projects like this one on https://github.com/jkutkut/")
