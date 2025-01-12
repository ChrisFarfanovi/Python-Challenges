from challenge import Challenge  # Importing Challenge Class
from datetime import datetime, timedelta  # For timing
from community_solutions import *  # importing function from community to test
from my_solution import my_solver

solver_list = {
    "My Solver": my_solver,
    "Example": name,
}  # List of solvers to test


def print_stress_test(tally: dict[str, int], time_taken: timedelta, solver_name: str):
    """Prints the test results including:
    :passed% (num failed)
    :seconds total
    :ms/test"""
    pass_rate = tally["PASSED"] / num_of_tests * 100
    failed = tally["FAILED"]
    total_secs = time_taken.total_seconds()
    time_per_test = total_secs / num_of_tests * 1000
    print(
        f"""\n{pass_rate}% Passed ({failed} failed)
{total_secs:.2f}s total
{time_per_test:.2f}ms/test.
"""
    )


def do_stress_test(num_of_tests: int, solver_name: str):
    tally: dict = {"PASSED": 0, "FAILED": 0}  # Scoreboard for tests
    solver_function = solver_list[solver_name]  # Get the solver from the solver_list
    start_time: datetime = datetime.now()  # Start the timer
    for x in range(num_of_tests):  # Repeat until done specified num of tests
        print(f"Running test {x+1}", end="\r")  # Print which test is running
        test = Challenge()  # Create challenge object
        solution = solver_function(test)  # Get solution by running solver
        if test.check_solution(solution):  # Update tally if solution was correct
            tally["PASSED"] += 1
        else:
            tally["FAILED"] += 1
    time_taken: timedelta = datetime.now() - start_time  # Stop the timer
    print_stress_test(tally, time_taken, solver_name)  # Print results


if __name__ == "__main__":
    num_of_tests: int = 5000  # Number of challenges to perform
    for solver_name in solver_list:  # For each available solver
        print(f"=== {solver_name} ===")
        do_stress_test(num_of_tests, solver_name)  # Test the solver
