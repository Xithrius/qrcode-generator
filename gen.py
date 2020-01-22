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
        self.forbidden = []
        self.safe = dims[0] // 10
        self.finder_size = 7
        self.missing_bin = ['11101100', '00010001']

        self.img = Image.new('RGB', self.dims, color='white')
        self.pix = self.img.load()

        self.insert_items()
        self.I = self.get_bin(I)
        self.bin_path()
        self.insert_bin()

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

    def get_bin(self, I):
        I = bin(int.from_bytes(I.encode(), 'big'))[2:]
        I = [I[i:i + 8] for i in range(0, len(I), 8)]
        return [i + '0' * (8 - len(i)) for i in I]

    def insert_bin(self):
        pass

    def bin_path(self):
        br = self.s - self.safe - 1
        pos = [br, br]
        for b in self.I:
            self.zig_zag(pos, b)
        # self.pix[pos, pos] = (0, 255, 0)

    def zig_zag(self, pos, b):
        for i in range(0, 8, 2):
            x, y = pos
            if (x, y) not in self.forbidden:
                self.pix[x, y] = (0, 0, 0) if b[i] == '1' else (255, 255, 255)
            else:
                pass

            if (x - 1, y) not in self.forbidden:
                self.pix[x - 1, y] = (0, 0, 0) if b[i + 1] == '1' else (255, 255, 255)
            else:
                pass

            pos[1] -= 1

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

    def insert_items(self):
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
        self.square(pos, pos, inner)
        self.square(pos, pos, inner, step=2)
        self.square(pos + 2, pos + 2, inner, (255, 255, 255), 2, False)

        # Insert Alignment pattern(s)
        pos += inner - 1
        for i in range(3):
            self.square(pos + i, pos + i, 5 - (i * 2), (255, 255, 255) if i == 1 else None)
        
        # Create dark module
        x = self.finder_size + self.safe + 1
        y = self.s - self.safe - self.finder_size - 1
        self.pix[x, y] = (0, 0, 0)
        self.forbidden.append((x, y))

        # Show forbidden spots
        for pos in self.forbidden:
            x, y = pos
            self.pix[x, y] = (255, 0, 0)


if __name__ == "__main__":
    QR('Hello World')