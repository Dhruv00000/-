from decimal import Decimal
from time import perf_counter

def sum_of_divisors(num: int):
    divisorSum: int = sum(
        divisorCandidate
        for divisorCandidate in range(1, num)
        if num % divisorCandidate == 0
    )
    return divisorSum + num

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.
e: float = 2.7182818284590452

k: int = 1
approximationIntermediate: float = 0
approximation: Decimal = 0
previous: Decimal = 3.14
finalAccuracy: int = 0
totalComputationTime: float = 0

while True:

    iterationStartTime: float = perf_counter()
    approximationIntermediate += sum_of_divisors(k) * pow(e, (-2 * float(previous) * k))
    approximation = 1 / Decimal(1/3 - 8 * approximationIntermediate)
    iterationEndTime: float = perf_counter()

    print(f"\nIteration {k}")
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

    deviation: Decimal = approximation - Decimal(previous)
    if deviation == 0: 
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k} iterations.\n")