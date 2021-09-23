from Classes.colors import Color;
from PIL import Image, ImageDraw


class QR:
    '''Class responsible of generating QR codes.'''
    
    def __init__(self, text: str):
        print("hello world!")

        self.draw: ImageDraw

        self.SIZE = 28
        self.SIZE = (self.SIZE, self.SIZE)

        # with Image.open("hopper.jpg") as im:
        with Image.new('RGB', self.SIZE, color=(29, 184, 245)) as im:

            self.draw = ImageDraw.Draw(im)

            # Corners
            self.drawCorner(0, 0)
            self.drawCorner(22, 0)
            self.drawCorner(0, 22)

            # Debug cross
            self.draw.line((0, 0) + im.size, fill=128)
            self.draw.line((0, im.size[1], im.size[0], 0), fill=128)

            # write to stdout
            im.save("qr.png")

    def drawCorner(self, x: int, y: int):
        w = 1
        rect = [(0 + i, 0 + i, 6 - i, 6 - i) for i in range(3)]
        rect = [((c[0] + x) * w, (c[1] + y) * w, (c[2] + x) * w, (c[3] + y) * w) for c in rect]
        self.draw.rectangle(rect[0], fill=Color.QR_COLOR)
        self.draw.rectangle(rect[1], fill=Color.BG)
        self.draw.rectangle(rect[2], fill=Color.QR_COLOR)