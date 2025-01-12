import random


class Challenge:
    def __init__(self):
        self.data: int = random.randint(a=500, b=1_000_000_000)
        """The `data` property contains the data you need to complete the challenge.
        (In this instance, these are just instructions.)"""

    def check_solution(self, solution) -> bool:
        """The `check_solution` method is used to make sure your solution is correct.
        (You can often check the type-hinting if you are getting any type errors.)"""
        factor: int = 2
        number: int = self.data
        while number > (factor - 1) ** 2:
            while number % factor == 0:
                number = int(number / factor)
            factor += 1
        factor = (factor - 1) if number == 1 else number
        return True if factor == solution else False
