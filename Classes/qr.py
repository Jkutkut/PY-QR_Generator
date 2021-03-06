from typing import Generator
from Classes.colors import Color;
from PIL import Image, ImageDraw


class QR:
    '''Class responsible of generating QR codes.'''
    
    def __init__(self, text: str):

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
            color = QR.blinkColor()
            for i in range(7, 22, 1):
                c = next(color)
                self.drawPixel(i, 6, c)
                self.drawPixel(6, i, c)

            # Alignment
            self.drawPositioning(22, 22)

            # write to stdout
            im.save("qr.png")

    def drawPixel(self, x: int, y: int, color: tuple = Color.QR_COLOR) -> None:
        '''Draws a 1x1 rectangle on the given location.'''
        self.drawRect((x, y, x, y), color)

    def drawRect(self, coord: tuple, color: tuple) -> None:
        '''Draws a rectangle on the given coordinate (xi, yi, xf, yf) with the given RGB color.'''
        self.draw.rectangle(coord, color)

    
    # Positioning and orientation
    def drawPositioning(self, x: int, y: int):
        '''Draws a positioning square on the given location.'''
        rect = [(-2 + i, -2 + i, 2 - i, 2 - i) for i in range(3)]
        rect = [(c[0] + x, c[1] + y, c[2] + x, c[3] + y) for c in rect]

        color = QR.blinkColor(firstBG=False)
        for r in rect:
            self.drawRect(r, next(color))

    def drawCorner(self, x: int, y: int):
        '''Draws a corner of the QR on the given coordinates.'''
        w = 1
        rect = [(-1 + i, -1 + i, 7 - i, 7 - i) for i in range(4)]
        rect = [((c[0] + x) * w, (c[1] + y) * w, (c[2] + x) * w, (c[3] + y) * w) for c in rect]

        color = QR.blinkColor()
        for r in rect:
            self.drawRect(r, next(color))


    def blinkColor(firstBG:bool=True) -> Generator[tuple, None, None]:
        '''Generator that blinks between the background and color of the QR.'''
        if firstBG:
            yield Color.BG

        while(True):
            yield Color.QR_COLOR
            yield Color.BG