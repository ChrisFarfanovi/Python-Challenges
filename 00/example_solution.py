from challenge import Challenge  # Importing the Challenge class

my_challenge = Challenge()
# Creating an instance of the Challenge class

print(my_challenge.data)
# Accessing the `.data` attribute to get the instructions

solution = "o7"
result = my_challenge.check_solution(solution)
print(f"{solution} = {result}")
# Using the `check_solution()` method to check my solution and store the result.
# `False` *Buzzer noise* - Re-read the instructions.

solution = ["o7"]
print(f"{solution} = {my_challenge.check_solution(solution)}")
# Checking the revised solution - *Great Success*
