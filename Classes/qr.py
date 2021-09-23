from typing import Generator
from Classes.colors import Color;
from PIL import Image, ImageDraw


class QR:
    '''Class responsible of generating QR codes.'''
    
    def __init__(self, text: str):
        print("hello world!")

        self.draw: ImageDraw

        self.SIZE = 28
        self.SIZE = (self.SIZE, self.SIZE)

        with Image.new('RGB', self.SIZE, color=(29, 184, 245)) as im:

            self.draw = ImageDraw.Draw(im)

            # Debug cross
            self.draw.line((0, 0) + im.size, fill=128)
            self.draw.line((0, im.size[1], im.size[0], 0), fill=128)

            # Corners
            self.drawCorner(0, 0)
            self.drawCorner(22, 0)
            self.drawCorner(0, 22)

            #  Timing

            # write to stdout
            im.save("qr.png")

    def drawCorner(self, x: int, y: int):
        w = 1
        rect = [(-1 + i, -1 + i, 7 - i, 7 - i) for i in range(4)]
        rect = [((c[0] + x) * w, (c[1] + y) * w, (c[2] + x) * w, (c[3] + y) * w) for c in rect]

        color = QR.blinkColor()

        for r in rect:
            self.draw.rectangle(r, next(color))


    def blinkColor() -> Generator[tuple, None, None]:
        while(True):
            yield Color.BG
            yield Color.QR_COLOR