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



if __name__ == "__main__":
    calc1 = Calc1
    print(f"{calc1.answer1}")

