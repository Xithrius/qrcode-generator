"""
> QR_Generator
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
"""


from PIL import Image


class QR:

    def __init__(self, I, dims=(33, 33)):
        self.check_dimensions(dims)

        self.dims = dims
        self.s = dims[0]
        self.I = I
        self.forbidden = []
        self.safe = dims[0] // 10
        self.finder_size = 7

        self.img = Image.new('RGB', self.dims, color='white')
        self.pix = self.img.load()

        self.insert()

        self.img.save('image.png')

    def check_dimensions(self, dims):
        checks = [
            (dims[0] != dims[1], 'Dimensions must be equivilant.'),
            (dims[0] > 177, 'Dimensions cannot be larger than 177.'),
            (dims[0] < 11, 'Dimensions cannot be smaller than 11.')
        ]
        checks = [c for c in checks if c[0]]
        if len(checks) >= 1:
            assert False, checks[0][1]

    def insert(self):
        size = self.finder_size
        g = self.safe

        # Inserting finder patterns
        pos = [
            (g, g),
            (self.dims[0] - size - g, g),
            (g, self.dims[1] - size - g)
        ]
        for x, y in pos:
            for i in range(3):
                self.square(x + i, y + i, size - (i * 2), (255, 255, 255) if i == 1 else None)

        # Insert Timing Patterns
        pos = self.finder_size + g - 1
        inner = self.s - (2 * g) - (2 * self.finder_size)
        self.square(pos, pos, inner, step=2)
        self.square(pos + 2, pos + 2, inner, (255, 255, 255), 2, False)

        # Insert Alignment pattern(s)
        pos += inner - 1
        for i in range(3):
            self.square(pos + i, pos + i, 5 - i * 2, (255, 255, 255) if i == 1 else None)

        # Show forbidden spots
        return
        for pos in self.forbidden:
            x, y = pos
            self.pix[x, y] = (255, 0, 0)

    def square(self, x, y, size, color=(0, 0, 0), step=1, forbid=True):
        color = (0, 0, 0) if not color else color
        for i in range(y, y + size, step):
            for j in range(x, x + size, step):
                self.pix[i, j] = color
                if forbid:
                    self.forbidden.append((i, j))
                else:
                    try:
                        self.forbidden.remove((i, j))
                    except ValueError:
                        pass


if __name__ == "__main__":
    QR('Hello World')