"""
> QR_Generator
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
"""


from PIL import Image


class QR:

    def __init__(self, s=11):
        self.s = s
        self.gap = 2

        self.finder_size = 7
        self.dims = [dim + (2 * self.gap) for dim in (s, s)]

        self.img = Image.new('RGB', self.dims, color='white')
        self.pix = self.img.load()

        self.insert_timing()
        self.insert_finder()

        self.img.save('image.png')

    def square(self, x, y, size, color=(0, 0, 0), step=1):
        for i in range(y, y + size, step):
            for j in range(x, x + size, step):
                self.pix[i, j] = color

    def insert_timing(self):
        x, y = self.gap, self.gap
        for i in range(y, y + self.s, 2):
            for j in range(x, x + self.s, 2):
                if j == 2 or i == 2:
                    self.pix[i, j] = (0, 0, 0)

    def insert_finder(self):
        size = self.finder_size
        x, y = (self.gap, self.gap)
        self.square(x, y, size)
        self.square(x + 1, y + 1, size - 2, (255, 255, 255))
        self.square(x + 2, y + 2, size - 4)


if __name__ == "__main__":
    QR(17)
