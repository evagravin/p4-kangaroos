class Foil:
    def __init__(self, num1, num2, num3, num4):
        self._num1 = num1
        self._num2 = num2
        self._num3 = num3
        self._num4 = num4
        self._term1 = self.num1 * self.num3
        self._term2 = self.num2 * self.num3
        self._term3 = self.num1 * self.num4
        self._term4 = self.num2 * self.num4

    @property
    def term1(self):
        return self._term1

    @property
    def term2(self):
        return self._term2

    @property
    def term3(self):
        return self._term3

    @property
    def term4(self):
        return self._term4

    @property
    def num1(self):
        return self._num1

    @property
    def num2(self):
        return self._num2

    @property
    def num3(self):
        return self._num3

    @property
    def num4(self):
        return self._num4


if __name__ == "__main__":
    foil = Foil(1,2,3,4)
    print(f"{foil.term1}{foil.term2}{foil.term3}{foil.term4}")