#!/usr/bin/env python3

from PIL import Image, ImageDraw

# Constants
BG = (255, 255, 255)
QR_COLOR = (0, 0, 0)

SIZE = 280
SIZE = (SIZE, SIZE)

def drawCorner(x, y):
    w = 10
    rect = [(0 + i, 0 + i, 6 - i, 6 - i) for i in range(3)]
    rect = [((c[0] + x) * w, (c[1] + y) * w, (c[2] + x) * w, (c[3] + y) * w) for c in rect]
    draw.rectangle(rect[0], fill=QR_COLOR)
    draw.rectangle(rect[1], fill=BG)
    draw.rectangle(rect[2], fill=QR_COLOR)

# with Image.open("hopper.jpg") as im:
with Image.new('RGB', SIZE, color=(29, 184, 245)) as im:

    draw = ImageDraw.Draw(im)

	# Corners
    drawCorner(0, 0)
    drawCorner(22, 0)
    drawCorner(0, 22)
    # draw.rectangle((0, 0, 6, 6), fill=QR_COLOR)
    # draw.rectangle((1, 1, 5, 5), fill=BG)
    # draw.rectangle((2, 2, 4, 4), fill=QR_COLOR)



    # Debug cross
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)

    # write to stdout
    im.save("qr.png")

print("Thanks for using this code, I hope you liked it.")
print("See more projects like this one on https://github.com/jkutkut/")
