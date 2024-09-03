from decimal import Decimal
from time import perf_counter
from math import sin

n: int = 0
approximation: Decimal = 0
previous: Decimal = 3.14
finalAccuracy: int = 0
totalComputationTime: float = 0
flag: bool = False

try: x: float = float(input("Enter a value for 'x': "))
except ValueError: x = "" # Setting 'n' to a non-integer ensures that the below check fails and the execution flow is transferred to the else statement at the bottom.

try:
    flag = x % 1 != 0 and isinstance(x, float)
except TypeError:
    flag = False

if flag:
    while True:

        iterationStartTime: float = perf_counter()

        approximation += Decimal(sin(float(previous) * x) / (n + x)) * Decimal(pow(-1, n))
        if n != 0: approximation += Decimal(sin(float(previous) * x) / (x - n)) * Decimal(pow(-1, n))

        iterationEndTime: float = perf_counter()

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

        deviation: Decimal = approximation - Decimal(previous)
        if deviation == 0 and previous != 3.14: 
            print("Negligible deviation (terminating the program)\n")
            break
        elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

        if finalAccuracy >= 2: previous = approximation # this stops the extremely incorrect approximations from the first few steps from ruining all succeeding steps.
        n += 1

else:
    print("\nx must be a non-integral rational number less than 2^52 - 1.\n")

if flag: print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {n + 1} iterations.\n")