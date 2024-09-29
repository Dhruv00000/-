from decimal import Decimal
from time import perf_counter
from time import sleep

k: int = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0

while True:

    iterationStartTime = perf_counter()
    approximation += pow(-1, k) * (Decimal(256 / (10*k + 1)) + Decimal(1 / (10*k + 9)) - Decimal(32 / (4*k + 1)) - Decimal(1 / (4*k + 3)) - Decimal(64 / (10*k + 3)) - Decimal(4 / (10*k + 5)) - Decimal(4 / (10*k + 7))) / pow(2, 10*k + 6)
    iterationEndTime = perf_counter()

    print(f"\nIteration {k + 1}")
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

    deviation: Decimal = Decimal(approximation - previous)
    if deviation == 0:
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1

    # sleep(5)

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k + 1} iterations.\n")