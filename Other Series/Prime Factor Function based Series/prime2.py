from decimal import Decimal
from time import perf_counter

def epsilonAlt(n):
    PrimeFactorCount: int = 0

    # if n % 2 == 0: PrimeFactorCount += 1
    while n % 2 == 0: n = n // 2

    for i in range(3, n + 1, 2):
        if n % i == 0 and ((i - 1) % 4 == 0): PrimeFactorCount += 1
        while n % i== 0: n = n // i

    return PrimeFactorCount

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.

k: int = 1
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0

while True:

    iterationStartTime: float = perf_counter()
    approximation += pow(-1, epsilonAlt(k)) / k
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

    deviation: Decimal = approximation - previous
    if deviation == 0: 
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {approximation - previous}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k} iterations.\n")