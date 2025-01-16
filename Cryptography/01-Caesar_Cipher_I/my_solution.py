from challenge import Challenge  # Importing the Challenge class


def my_solver(challenge: Challenge):  # Defining your solver
    data = challenge.data  # Storing our challenge data

    word1 = data[0]
    word2 = data[1]
    word3 = data[2]
    shift = data[3]
    phrase = word1.upper() + word2.upper() + word3.upper()

    def shift_letter(letter, shift):
        shifted = chr(ord(letter) + shift)
        if ord(shifted) > 90:
            shifted = chr(ord(shifted) - 26)
        return shifted

    encrypted = ""
    for letter in phrase:
        encrypted = encrypted + shift_letter(letter, shift)
    # take last letter of encrypted
    last_letter = encrypted[-1]
    key = shift_letter(last_letter, shift)

    return key + encrypted  # Don't forget to return your solution!


if __name__ == "__main__":
    my_challenge = Challenge()  # Creating an instance of the Challenge class
    raw_data = my_challenge.data  # Storing our challenge data
    solution = my_solver(my_challenge)  # Running your solver and store what returns
    result = my_challenge.check_solution(solution)  # Checking the solution
    print(f"{raw_data} | {solution} | {result}")  # Print the final outcome
