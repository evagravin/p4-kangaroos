class Foil:
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4

    def __repr__(self):
        return f"{self.num1},{self.num2},{self.num3},{self.num4}"