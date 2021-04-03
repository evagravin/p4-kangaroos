class Sum:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
        self._term1 = self.num1 + self.num2


    @property
    def term1(self):
        return self._term1


    @property
    def num1(self):
        return self._num1

    @property
    def num2(self):
        return self._num2



if __name__ == "__main__":
    sum = Sum(1,2)
    print(f"{sum.term1}")