class Calc1:

    def __init__(self, temp1):
        self._temp1 = temp1
        self._answer1 = (self.temp1 - 32) * 5/9

    @property
    def temp1(self):
        return self._temp1

    @property
    def answer1(self):
        return self._answer1

class Calc2:
    def __init__(self, weight2):
        self._weight2 = weight2
        self._answer2 = (self.weight2 * 454)
    @property
    def weight2(self):
        return self._weight2

    @property
    def answer2(self):
        return self._answer2

class Calc3:
    def __init__(self, distance3):
        self._distance3 = distance3
        self._answer3 = (self.distance3 / 1.094)
    @property
    def distance3(self):
        return self._distance3

    @property
    def answer3(self):
        return self._answer3




if __name__ == "__main__":
    calc1 = Calc1
    print(f"{calc1.answer1}")
    calc2 = Calc2
    print(f"{calc2.answer2}")
    calc3 = Calc3
    print(f"{calc3.answer3}")




