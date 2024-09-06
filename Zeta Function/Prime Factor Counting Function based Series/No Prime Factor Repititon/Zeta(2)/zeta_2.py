from decimal import Decimal
from time import perf_counter
from time import sleep

iterationCounter: int = 1
n: int = 2
approximationSquaredInverted: float = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0

def epsilonModified(n):
    PrimeFactorCount: int = 0

    if n % 2 == 0:
        n = n // 2
        PrimeFactorCount += 1

    for i in range(3, n + 1, 2):
        if n % i== 0:
            n = n // i
            PrimeFactorCount += 1
        if n % i == 0:
            PrimeFactorCount = 0
    
    if n % 2 == 0:
        PrimeFactorCount = 0

    return PrimeFactorCount

while True:

    if epsilonModified(n) % 2 != 0:

        iterationStartTime: float = perf_counter()
        approximationSquaredInverted += 2 / (9 * pow(n, 2))
        approximation = Decimal(pow(approximationSquaredInverted, -1/2))
        iterationEndTime: float = perf_counter()

        print(f"\nIteration {iterationCounter}")
        print(f"Approximation = {approximationSquaredInverted / 20}")

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
        iterationCounter += 1
    
    n += 1

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {iterationCounter} iterations.\n")