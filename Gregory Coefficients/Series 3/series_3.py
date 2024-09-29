from decimal import Decimal
from time import perf_counter

n: int = 0
approximationIntermediate: float = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
Coeffecients: list[float] = []
iterationStartTime: float = 0
iterationEndTime: float = 0

def GregoryCoeffecient(num: int) -> float:
    if num == 1 : return 1/2

    result: float = 0 - sum(Coeffecients[k + 1] / (num - k + 1) for k in range(1, num))
    if result + (1 / (num + 1)) not in Coeffecients: Coeffecients += result + (1/ (num + 1))
    return result + (1 / (num + 1))

while True:

    iterationStartTime = perf_counter()
    approximationIntermediate += pow(-1, n) * (GregoryCoeffecient(3*n + 3) + GregoryCoeffecient(3*n + 4))
    approximation = pow(3, 1/2) / (1/2 - approximationIntermediate)
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