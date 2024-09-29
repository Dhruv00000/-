from decimal import Decimal
from time import perf_counter
from math import gamma
from time import sleep

k: int = 1
approximationIntermediate: Decimal = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
terminated: bool = False
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0


def factorial(n: int) -> int:
    return factorial(n - 1) * n if n != 0 else 1


def subscript(a: float, b: int):
    return gamma(a + b) / gamma(a)


try:
    parameter: int = int(input("Enter a value for lambda: "))
except ValueError:
    parameter = ""  # Setting 'n' to a non-integer ensures that the below check fails and the execution flow is transferred to the else statement at the bottom.

parameter = 50

# print(gamma(0))

flag: bool = isinstance(parameter, int) and parameter != 0 and parameter > 0
if flag:
    while True:
        try:
            iterationStartTime = perf_counter()
            approximationIntermediate += Decimal(
                (1 / (k + parameter) - 4 / (2 * k + 1)) / factorial(k)
            ) * Decimal(subscript(pow(2 * k + 1, 2) / (4 * (k + parameter) - k), k - 1))
        except (OverflowError, RecursionError) as e:
            print("\nThe entered value is too large to handle.\n")
            terminated = True
            break

        approximation = approximationIntermediate + 4
        iterationEndTime = perf_counter()

        print(f"\nIteration {k}")
        print(f"Approximation = {approximation}")

        for i, char in enumerate(
            "3.141592653589793238462643383279502884197169399375"
        ):  # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
            if char != str(approximation)[i]:
                if i < 2:
                    print("No accurate decimal places")
                else:
                    print(f"{i - 2} correct decimal place(s)")
                    finalAccuracy = i - 2
                break

        print(f"Iteration duration: {iterationEndTime - iterationStartTime}  seconds")
        totalComputationTime += iterationEndTime - iterationStartTime

        deviation: Decimal = Decimal(approximation - previous)
        if deviation == 0:
            print("Negligible deviation (terminating the program)\n")
            break
        elif deviation != approximation:
            print(
                f"Deviation from previous iteration: {deviation}"
            )  # this if-statement prevents a deviation from being shown during the first iteration.

        previous = approximation
        k += 1

        sleep(5)

else:
    print("\nn must be a positive integer.\n")

if not terminated and flag:
    print(
        f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k} iterations.\n"
    )
