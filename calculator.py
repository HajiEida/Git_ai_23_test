print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return int(a * b)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")  # Proper error handling
        return a / b

    def power(self, a, b):
        if a == 0 and b < 0:
            raise ValueError("0 cannot be raised to a negative power")
        return a ** b
    

    def factorial(self, n):
            if n < 0:
                raise ValueError("not defined for negative numbers")
            if n == 0:
                return 1
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("not defined for negative numbers")
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b


class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def _round_result(self, result):
        if isinstance(result, float):
            return round(result, self.precision) #made a function so dont have to write in each function
        return result

    def add(self, a, b):
        result = super().add(a, b)
        return self._round_result(result)

    def subtract(self, a, b):
        result = super().subtract(a, b)
        return self._round_result(result)

    def multiply(self, a, b):
        result = super().multiply(a, b)
        return self._round_result(result)

    def divide(self, a, b):
        result = super().divide(a, b)
        return self._round_result(result)

    def power(self, a, b):
        result = super().power(a, b)
        return self._round_result(result)

    def factorial(self, n):
        result = super().factorial(n)
        return self._round_result(result)

    def fibonacci(self, n):
        result = super().fibonacci(n)
        return self._round_result(result)