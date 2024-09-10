from decimal import Decimal
from time import perf_counter
from time import sleep

def double_factorial(n: int) -> int:
    return double_factorial(n - 2) * n if n not in [0, 1] else 1

k: int = 0
approximationInverted: float = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0

while True:

    iterationStartTime = perf_counter()
    approximationInverted += pow((double_factorial(2*k + 1) / ((2*k + 1) * double_factorial(2*k))), 3) * (4*k + 1) * pow(-1, k) / 2
    approximation = 1 / Decimal(approximationInverted)
    iterationEndTime = perf_counter()

    print(f"\nIteration {k + 1}")
    print(f"Approximation = {2 / approximation}")

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
    k += 1

    sleep(5)

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k + 1} iterations.\n")