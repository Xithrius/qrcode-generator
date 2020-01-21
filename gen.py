"""
> QR_Generator
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
"""


from PIL import Image


class QR:

    def __init__(self, dimensions):
        self.check_input(dimensions)

        self.dimensions = dimensions
        self.forbidden = []

        _bin = self.to_binary('Hello World')


    def check_input(self, dims):
        checks = [
            (dims[0] != dims[1], 'Dimensions must be equivilant.'),
            (dims[0] > 177, 'Dimensions cannot be larger than 177.'),
            (dims[0] < 21, 'Dimensions cannot be smaller than 21.'),
            (dims[0] - 21 != 0, 'Dimensions must be a multiple of 4 added to 21.'),
            ((dims[0] - 21) % 4 == 1, 'Dimensions must be a multiple of 4 added to 21.')
        ]
        checks = [c for c in checks if c[0]]
        if len(checks) >= 1:
            assert False, checks[0][1]

    def to_binary(self, _input):
        out = bin(int.from_bytes(_input.encode(), 'big'))[2:]
        out = [out[i:i + 8] for i in range(0, len(out), 8)]
        out = [i + '0' * (8 - len(i)) for i in out]
        print(out)

    def square(self, pos):
        pass


if __name__ == "__main__":
    QR((21, 21))

"""
        else:
            x = (any((dims[0] - 21 == 0, (dims[0] - 21) % 4 == 1)), 'Dimensions must be a multiple of 4 added to 21.')
            print(x)
            print(dims[0] - 21 == 0)
            print((dims[0] - 21) % 4 == 1)
            # 'Dimensions must be a multiple of 4 added to 21.'
"""