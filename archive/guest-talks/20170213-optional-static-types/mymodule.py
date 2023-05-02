mystery = 3


class MyClass(dict):
    def __add__(self, other: int) -> int:
        return 1 + other
