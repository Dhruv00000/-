from decimal import Decimal
from time import perf_counter

n: int = 1
approximationExponentiated: float = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
previousHarmonic: int = 1
iterationStartTime: float = 0
iterationEndTime: float = 0

def nth_Harmonic() -> float:
    global previousHarmonic

    if n == 1: return 1

    result: int = previousHarmonic + 1 / n
    previousHarmonic = result

    return result

while True:

    iterationStartTime = perf_counter()
    approximationExponentiated += 72 * nth_Harmonic() / pow(n, 3)
    approximation = Decimal(pow(approximationExponentiated, 1/4))
    iterationEndTime = perf_counter()

    print(f"\nIteration {n}")
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

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {n} iterations.\n")