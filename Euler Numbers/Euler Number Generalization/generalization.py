from decimal import Decimal
from time import perf_counter

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.

n: int = 0
approximationExponentiated: float = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
overflowed: bool = False

def factorial(n: int):
    return factorial(n - 1) * n if n != 0 else 1

try: k: int = int(input("Enter a value for 'k': "))
except ValueError: k = "a" # Setting 'n' to a non-integer ensures that the below check fails and the execution flow is transferred to the else statement at the bottom.

def Euler_2k(num: int):

    if num == 0: return 1
    result: int = 0

    for k in range(1, 2*num + 1):
        innerLoopSum: float = sum(
            (pow(-1, l) * pow(k - l, 2 * num) * factorial(2 * k))
            / (factorial(l) * factorial(2 * k - l))
            for l in range(2 * k + 1)
        )
        result += pow(-1, k) * pow(2, -k) * innerLoopSum

    return result

if isinstance(k, int) and k >= 0:
    startingTime: float = perf_counter()

    while True:
        try:
            iterationStartTime: float = perf_counter()
            approximationExponentiated += (pow(-1, n-k) * factorial(2*k) * pow(2, 2*k + 2)) / (pow(2*n + 1, 2*k + 1) * Euler_2k(k))
        except (OverflowError, RecursionError) as e:
            print("\nThe entered value is too large to handle.\n")
            overflowed = True
            break

        approximation = Decimal(pow(approximationExponentiated, 1 / (2*k + 1)))
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

        deviation: Decimal = approximation - previous
        if deviation == 0: 
            print("Negligible deviation (terminating the program)\n")
            break
        elif deviation != approximation: print(f"Deviation from previous iteration: {approximation - previous}") # this if-statement prevents a deviation from being shown during the first iteration.

        previous = approximation
        n += 1

else:
    print("\nn must be a whole number.\n")

if not overflowed:
    terminationTime: float = perf_counter()

    print(f"\n\nCalculated {finalAccuracy} correct decimal places in {terminationTime - startingTime} seconds and {k + 1} iterations.\n")