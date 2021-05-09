class Calculations:

    def __init__(self, num):
        self._num = num

    @property
    def cel2far(self):
        return round((self._num - 32) * 5 / 9, 2)

    @property
    def lbs2g(self):
        return round((self._num * 454), 2)

    @property
    def y2m(self):
        return round((self._num / 1.094), 2)

    @property
    def g2oz(self):
        return round((self._num / 28.35), 2)

    @property
    def kg2lbs(self):
        return round((self._num * 2.205), 2)

    # Fibonacci Series using Dynamic Programming
    @property
    def fibonacci(self):
        # Initializing a list for the first two fibonacci numbers
        b = [0, 1]
        # Producing the nth number (self._num) in the fibonacci sequence
        for r in range(2, self._num + 1):
            b.append(b[r - 1] + b[r - 2])
        # Returning the nth number in the fibonacci sequence
        return b[self._num]

    @property
    def newton(self):

        # initializing variables for newton
        x = self._num
        limit = .0001

        # To count the number of iterations
        count = 0

        # Loop continues until accuracy reaches limit
        while True:
            count += limit

            # Calculate more closed x
            answer = 0.5 * (x + (self._num / x))

            # Testing if the root-x is less than limit
            if abs(answer - x) < limit:
                break

                # Update root
            x = answer

        return answer

    @property
    def num(self):
        return self._num

if __name__ == "__main__":
    calculations = Calculations(4)
    print(f"{calculations.cel2far}")
    print(f"{calculations.lbs2g}")
    print(f"{calculations.y2m}")
    print(f"{calculations.g2oz}")
    print(f"{calculations.kg2lbs}")
    print(f"{calculations.fibonacci}")
    print(f"{calculations.newton}")

