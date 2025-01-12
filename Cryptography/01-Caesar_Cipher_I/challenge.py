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
        self.data: list = [word1, word2, word3, shift]
        """The `data` property contains the data you need to complete the challenge.
        (In this instance, these are just instructions.)"""

    def check_solution(self, solution) -> bool:
        """The `check_solution` method is used to make sure your solution is correct.
        (You can often check the type-hinting if you are getting any type errors.)"""
        word1: str = self.data[0]
        word2: str = self.data[1]
        word3: str = self.data[2]
        shift: int = self.data[3]
        phrase = word1.upper() + word2.upper() + word3.upper()

        def do_shift(letter: str, shift: int) -> str:
            return chr(ord(letter) + shift - (26 if ord(letter) >= (91 - shift) else 0))

        encrypted_phrase = ""
        for letter in phrase:
            encrypted_phrase = encrypted_phrase + do_shift(letter, shift)

        key = do_shift(encrypted_phrase[-1], shift)

        return True if solution == key + encrypted_phrase else False


if __name__ == "__main__":
    test = Challenge()
    print(test.data)
