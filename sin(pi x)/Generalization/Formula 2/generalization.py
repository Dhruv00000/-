from decimal import Decimal
from time import perf_counter
from math import sin

n: int = 0
approximationSquared: float = 0
approximation: Decimal = 0
piString: str = "3.141592653589793238462643383279502884197169399375"
previous: Decimal = 3.14
finalAccuracy: int = 0
totalComputationTime: float = 0
flag1: bool = False
iterationStartTime: float = 0
iterationEndTime: float = 0

try: x: float = float(input("Enter a value for 'x': "))
except ValueError: x = "" # Setting 'n' to a non-integer ensures that the below check fails and the execution flow is transferred to the else statement at the bottom.

try: precision: int = int(input("Enter the number of correct decimal places to use in the initial value of pi (defaults to 49 if a large value is entered.): "))
except ValueError: precision = ""

print() # Prints an empty line before errors are displayed (to make the output look cleaner).

try:
    flag1 = x % 1 != 0 and isinstance(x, float)
except TypeError:
    flag1 = False

flag2: bool = isinstance(precision, int) and precision > 0

if flag1 and flag2:

    previous: Decimal = Decimal(piString[: precision + 2])

    while True:

        iterationStartTime = perf_counter()

        approximationSquared += pow((sin(float(previous) * x) / (n + x)), 2)
        if n != 0: approximationSquared += pow((sin(float(previous) * x) / (x - n)), 2)
        approximation = Decimal(pow(approximationSquared, 1/2))

        iterationEndTime = perf_counter()

        print(f"\nIteration {n + 1}")
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
        n += 1

if not flag1: print("x must be a non-integral rational number less than 2^52 - 1.\n")
if not flag2: print("Precision must be a natural number less than 49.\n")

if flag1 and flag2: print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {n + 1} iterations.\n")