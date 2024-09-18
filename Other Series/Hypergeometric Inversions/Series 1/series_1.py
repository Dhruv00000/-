from decimal import Decimal
from time import perf_counter

k: int = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0

def d1(n: int) -> int:
    PrimeFactorCount: int = 1

    for potentialFactor in range(3, n + 1):
        if n % potentialFactor == 0 and (potentialFactor - 1) % 4 == 0:
            PrimeFactorCount += 1
            while n % potentialFactor == 0: n /= potentialFactor

    return PrimeFactorCount

def d3(n: int) -> int:
    PrimeFactorCount: int = 0

    for potentialFactor in range(3, n + 1):
        if n % potentialFactor == 0 and (potentialFactor - 3) % 4 == 0:
            PrimeFactorCount += 1
            while n % potentialFactor == 0: n /= potentialFactor

    return PrimeFactorCount

def r2(n: int) -> int:
    return 4 * abs(d1(n) - d3(n))

def risingFactorial(x: int, n: int) -> float:
    result: int = 1

    if n == 0: return 1

    for i in range(n):
        result *= x + i
    return result

def hypergeometric(a, b, c, z):


# while True:

#     iterationStartTime = perf_counter()
#     approximation += 8 * Decimal(1 / ((4*k + 1) * (4*k + 3)))
#     iterationEndTime = perf_counter()

#     print(f"\nIteration {k + 1}")
#     print(f"Approximation = {approximation}")

#     for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
#         try:
#             if char != str(approximation)[i]:
#                 if i < 2: print("No accurate decimal places")
#                 else:
#                     print(f"{i - 2} correct decimal place(s)")
#                     finalAccuracy = i - 2
#                 break
#         except IndexError: print("No incorrect decimal places.")

#     print(f"Iteration duration: {iterationEndTime - iterationStartTime}  seconds")
#     totalComputationTime += iterationEndTime - iterationStartTime

#     deviation: Decimal = approximation - previous
#     if deviation == 0: 
#         print("Negligible deviation (terminating the program)\n")
#         break
#     elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

#     previous = approximation
#     k += 1

# print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k + 1} iterations.\n")