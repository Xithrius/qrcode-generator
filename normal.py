"""
> QR_Generator
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
"""


from PIL import Image


class QR:

    def __init__(self, dims):
        self.check_input(dims)

        self.gap = dims[0] // 10

        self.finder_size = 8
        self.dims = [dim + (2 * self.gap) for dim in dims]

        self.img = Image.new('RGB', self.dims, color='white')
        self.pix = self.img.load()

        self.insert_finders()
        self.insert_timing()

        self.img.save('image.png')

    def check_input(self, dims):
        checks = [
            (dims[0] != dims[1], 'Dimensions must be equivilant.'),
            (dims[0] > 177, 'Dimensions cannot be larger than 177.'),
            (dims[0] < 11, 'Dimensions cannot be smaller than 11.')
        ]
        checks = [c for c in checks if c[0]]
        if len(checks) >= 1:
            assert False, checks[0][1]

    def insert_finders(self):
        size = self.finder_size
        pos = [
            (self.gap, self.gap),
            (self.dims[0] - size - self.gap, self.gap),
            (self.gap, self.dims[1] - size - self.gap)
        ]
        for x, y in pos:
            self.square(x, y, size)
            self.square(x + 1, y + 1, size - 2, (255, 255, 255))
            self.square(x + 2, y + 2, size - 4)

    def square(self, x, y, size, color=(0, 0, 0), step=1, conditional=False):
        for i in range(y, y + size, step):
            for j in range(x, x + size, step):
                if conditional:
                    print(i, j)
                self.pix[i, j] = color

    def insert_timing(self):
        pos = self.finder_size + self.gap - 1
        self.inner_square(pos)

    def inner_square(self, pos):
        size = self.dims[0] - (2 * self.finder_size) - (2 * self.gap)
        self.square(pos, pos, size, step=2)
        self.square(pos + 1, pos + 1, size, color=(255, 255, 255))

    def forbidden_areas():
        pass



if __name__ == "__main__":
    QR((21, 21))
