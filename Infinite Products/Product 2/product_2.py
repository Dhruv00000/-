from decimal import Decimal
from time import perf_counter

iterationCounter: int = 1
n: int = 2
approximationIntermediate: Decimal = Decimal(1)
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0

def isPrime(num) -> bool:
    return not any(num % i == 0 and num != i for i in range(3, num + 1, 2))

while True:

    if n % 6 in [1, 5] and isPrime(n):

        iterationStartTime = perf_counter()

        approximationIntermediate *= n
        if n % 6 == 1: approximationIntermediate /= n - 1
        else: approximationIntermediate /= n + 1
        approximation = 2 * Decimal(pow(3, 1/2)) * approximationIntermediate

        iterationEndTime = perf_counter()

        print(f"\nIteration {iterationCounter}")
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
        iterationCounter += 1
    
    n += 1

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {iterationCounter} iterations.\n")