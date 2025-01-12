from random import choice, randint
import csv


class Challenge:
    def __init__(self):
        wordlist = []
        with open("Resources/nouns.csv") as file:
            lines = csv.reader(file)
            for line in lines:
                wordlist.append(line[0])
        word1: str = choice(wordlist)
        word2: str = choice(wordlist)
        word3: str = choice(wordlist)
        shift: int = randint(1, 25)
        self.__solution: str = word1.upper() + word2.upper() + word3.upper()

        def do_shift(letter: str, shift: int) -> str:
            """Takes a letter and shifts it by the given amount"""
            return chr(ord(letter) + shift - (26 if ord(letter) >= (91 - shift) else 0))

        encrypted_phrase = ""
        for letter in self.__solution:
            encrypted_phrase = encrypted_phrase + do_shift(letter, shift)

        key = do_shift(encrypted_phrase[-1], shift)
        self.data: str = key + encrypted_phrase
        """The `data` property contains the data you need to complete the challenge.
        (In this instance, these are just instructions.)"""

    def check_solution(self, solution: str) -> bool:
        """The `check_solution` method is used to make sure your solution is correct.
        (You can often check the type-hinting if you are getting any type errors.)"""
        return True if solution == self.__solution else False


if __name__ == "__main__":
    test = Challenge()
    print(test.data)
