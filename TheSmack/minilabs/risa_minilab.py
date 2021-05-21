import math

class Calculations:

    # Initializing
    def __init__(self, num):
        self._num = num

    # Degrees Calculation (Celsius to Fahrenheit)
    @property
    def cel2far(self):
        return round((self._num - 32) * 5 / 9, 2)

    # Weight Calculation (Pounds to Grams)
    @property
    def lbs2g(self):
        return round((self._num * 454), 2)

    # Length Calculation (Yards to Meters)
    @property
    def y2m(self):
        return round((self._num / 1.094), 2)

    # Weight Calculation (Grams to Ounces)
    @property
    def g2oz(self):
        return round((self._num / 28.35), 2)

    # Weight Calculation (Kilograms to Pounds)
    @property
    def kg2lbs(self):
        return round((self._num * 2.205), 2)

    # Fibonacci Series
    @property
    def fibonacci(self):
        # Initializing a list for the first two fibonacci numbers
        list = [0, 1]
        # Producing the nth number (self._num) in the fibonacci sequence
        for r in range(2, self._num + 1):
            list.append(list[r - 2] + list[r - 1])
        # Returning the nth number in the fibonacci sequence
        return list[self._num]

    @property
    def newton(self):

        # Initializing variables for newton, math.sqrt is a function that runs through the math package
        x = math.sqrt(self._num)
        # Local variable, How many decimal points to calculate the square root to
        limit = .0001
        # To count the number of times the process would be repeated until a correct outcome is reached (iterations)
        number = 0
        # Loop continues until accuracy reaches limit
        while True:
            number += limit
            # Keeps calculating answer until the accurate square root is found
            answer = 0.5 * (x + (self._num / x))
            # Testing if the answer-x is less than limit
            if abs(answer - x) < limit:
                break
                # Updates answer
            x = answer
        # Returns the final answer
        return answer

    @property
    def num(self):
        return self._num

# Tester
if __name__ == "__main__":
    calculations = Calculations(6)
    print(f"{calculations.cel2far}")
    print(f"{calculations.lbs2g}")
    print(f"{calculations.y2m}")
    print(f"{calculations.g2oz}")
    print(f"{calculations.kg2lbs}")
    print(f"{calculations.fibonacci}")
    print(f"{calculations.newton}")

