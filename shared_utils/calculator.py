"""Calculator module with basic math operations."""


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self, precision: int = 2):
        self.precision = precision

    def add(self, a: float, b: float) -> float:
        return round(a + b, self.precision)

    def subtract(self, a: float, b: float) -> float:
        return round(a - b, self.precision)

    def multiply(self, a: float, b: float) -> float:
        return round(a * b, self.precision)

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return round(a / b, self.precision)
