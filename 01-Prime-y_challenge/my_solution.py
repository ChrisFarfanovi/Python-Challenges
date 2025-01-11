from challenge import Challenge  # Importing the Challenge class


def my_solver(challenge: Challenge):  # Defining your solver
    data = challenge.data  # Storing our challenge data
    # YOUR SOLVER GOES HERE
    return ...  # Don't forget to return your solution!


if __name__ == "__main__":
    my_challenge = Challenge()  # Creating an instance of the Challenge class
    raw_data = my_challenge.data  # Storing our challenge data
    solution = my_solver(my_challenge)  # Running your solver and store what returns
    result = my_challenge.check_solution(solution)  # Checking the solution
    print(f"{raw_data} | {solution} | {result}")  # Print the final outcome
