from challenge import Challenge


def chris_f(challenge: Challenge):
    # Unpack the data
    word1: str = challenge.data[0]
    word2: str = challenge.data[1]
    word3: str = challenge.data[2]
    shift: int = challenge.data[3]
    # Concat and Uppercase the words
    phrase = word1.upper() + word2.upper() + word3.upper()

    def do_shift(letter: str, shift: int) -> str:
        """Takes a letter and shifts it by the given amount"""
        return chr(ord(letter) + shift - (26 if ord(letter) >= (91 - shift) else 0))

    encrypted_phrase = ""
    for letter in phrase:
        encrypted_phrase = encrypted_phrase + do_shift(letter, shift)

    key = do_shift(encrypted_phrase[-1], shift)

    return key + encrypted_phrase


if __name__ == "__main__":
    test = Challenge()
    print(chris_f(test))
