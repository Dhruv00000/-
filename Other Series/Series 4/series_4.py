from decimal import Decimal
from time import perf_counter
from math import tan

k: int = 2
approximationInverted: float = 0
approximation: Decimal = 0
piString: str = "3.141592653589793238462643383279502884197169399375"
finalAccuracy: int = 0
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0

try: precision: int = int(input("Enter the number of correct decimal places to use in the initial value of pi (defaults to 49 if a large value is entered.): "))
except ValueError: precision = ""

flag: bool = isinstance(precision, int) and precision > 0
if flag:

    previous: Decimal = Decimal(piString[: precision + 2])

    while True:

        iterationStartTime = perf_counter()
        approximationInverted += tan(previous / pow(2, k)) / pow(2, k)
        approximation = 1 / Decimal(approximationInverted)
        iterationEndTime = perf_counter()

        print(f"\nIteration {k - 1}")
        print(f"Approximation = {approximation}")

        for i, char in enumerate(piString):
            if char != str(approximation)[i]:

                if i < 2: print("No accurate decimal places")
                else:
                    print(f"{i - 2} correct decimal place(s)")
                    finalAccuracy = i - 2

                break

        print(f"Iteration duration: {iterationEndTime - iterationStartTime}  seconds")
        totalComputationTime += iterationEndTime - iterationStartTime

        deviation: Decimal = approximation - Decimal(previous)
        if deviation == 0 and previous != 3.14: 
                print("Negligible deviation (terminating the program)\n")
                break
        elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

        if finalAccuracy >= 2: previous = approximation # this stops the extremely incorrect approximations from the first few steps from ruining all succeeding steps.

        previous = approximation
        k += 1

else: print("\nPrecision must be a natural number.\n")

if flag: print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k - 1} iterations.\n")