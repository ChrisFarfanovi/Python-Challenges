from challenge import Challenge


def chris_f(challenge: Challenge):
    # Unpack the data
    key: str = challenge.data[0]
    key_origin: str = challenge.data[-1]
    message: str = challenge.data[1:]
    shift = ord(key) - ord(key_origin)
    if shift <= 0:
        shift += 26

    def undo_shift(letter: str, shift: int) -> str:
        """Takes a letter and shifts it by the given amount"""
        return chr(ord(letter) - shift + (26 if ord(letter) - shift <= 64 else 0))

    deciphered = ""
    for letter in message:
        deciphered = deciphered + undo_shift(letter, shift)

    return deciphered


if __name__ == "__main__":
    test = Challenge()
    solution = chris_f(test)
    result = test.check_solution(solution)
    print(f"{test.data} | {solution} | {result}")
