from decimal import Decimal
from time import perf_counter

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.

k: int = 1
approximationExponentiated: float = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
overflowed: bool = False
totalComputationTime: float = 0

def factorial(n: int):
    return factorial(n - 1) * n if n != 0 else 1

try: n: int = int(input("Enter a value for 'n': "))
except ValueError: n = "a" # Setting 'n' to a non-integer ensures that the below check fails and the execution flow is transferred to the else statement at the bottom.

def Bernoulli(num: int):
    if num == 0: return 1

    result: float = sum(
        (Bernoulli(l) * factorial(num))
        / (factorial(l) * factorial(num - l) * (num - l + 1))
        for l in range(num)
    )
    return 1 - result

flag: bool = isinstance(n, int) and n != 0 and n > 0
if flag:
    while True:
        try:
            iterationStartTime: float = perf_counter()
            approximationExponentiated += pow(-1, n + 1) * (2 * factorial(2*n)) / (pow(k, 2*n) * pow(2, 2*n) * Bernoulli(2*n))
        except (OverflowError, RecursionError) as e:
            print("\nThe entered value is too large to handle.\n")
            overflowed = True
            break

        approximation = Decimal(pow(approximationExponentiated, 1 / (2*n)))
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

else:
    print("\nn must be a positive integer.\n")

if not overflowed and flag: print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k} iterations.\n")