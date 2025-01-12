from challenge import Challenge


def chris_f(challenge: Challenge) -> int:
    """Takes the `Challenge` object and returns and integer for testing"""
    factor: int = 2  # init at 2 (lowest prime)
    number: int = challenge.data  # init at our target number
    while number > (factor - 1) ** 2:  #
        while number % factor == 0:
            number = int(number / factor)
        factor += 1
    return (factor - 1) if number == 1 else number
