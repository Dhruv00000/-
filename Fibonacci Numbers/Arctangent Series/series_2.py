from decimal import Decimal
from time import perf_counter
from math import atan

n: int = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
alternateTerms: list = [1, 2]
iterationStartTime: float = 0
iterationEndTime: float = 0

def fibonacci_odd(num: int) -> int:

    if num == 1: return 1
    if num == 2: return 2

    result: int = 3 * alternateTerms[1] - alternateTerms[0]

    alternateTerms.pop(0)
    alternateTerms.append(result)

    return result

while True:

    iterationStartTime = perf_counter()
    approximation += 2 * Decimal(atan(1 / fibonacci_odd(n)))
    iterationEndTime = perf_counter()

    print(f"\nIteration {n + 1}")
    print(f"Approximation = {approximation}")

    for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
        if char != str(approximation)[i]:
            if i < 2: print("No accurate decimal places")
            else:
                print(f"{i - 2} correct decimal place(s)")
                finalAccuracy = i - 2
            break

    print(f"Iteration duration: {iterationEndTime - iterationStartTime}  seconds")
    totalComputationTime += iterationEndTime - iterationStartTime

    deviation: Decimal = approximation - previous
    if deviation == 0:
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    n += 1

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {n + 1} iterations.\n")