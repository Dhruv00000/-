# TODO: Implement more ramanujan-sato algorithms and move them into a separate folder if there are enough different series to justify doing so.
from decimal import Decimal

def factorial(n: int):
    return factorial(n - 1) * n if n != 0 else 1

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.

k: int = 0
approximationInverted: Decimal = 0
previous: Decimal = 0

while True:

    approximationInverted += Decimal((factorial(4*k) * (26390*k + 1103)) / (pow(factorial(k), 4) * pow(396, 4*k)))
    approximation: Decimal = Decimal(9801 / (2 * Decimal(pow(2, 1/2)) * (approximationInverted)))

    print(f"\nIteration {k + 1}")
    print(f"Approximation = {approximation}")

    for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
        if char != str(approximation)[i]:
            if i < 2: print("No accurate decimal places")
            else: print(f"{i - 2} accurate decimal place(s)")
            break

    deviation: Decimal = approximation - previous

    if deviation == 0: 
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {approximation - previous}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1