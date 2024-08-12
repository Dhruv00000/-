from decimal import Decimal

def factorial(n: int):
    return factorial(n - 1) * n if n != 0 else 1

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.

k: int = 0
approximation: float = 0
previous: float = 0

while True:

    approximation += 2 * Decimal(factorial(k) * factorial(2*k) * (25*k - 3)) / (factorial(3*k) * pow(2, k))

    print(f"\nIteration {k + 1}")
    print(f"Approximation = {approximation}")

    for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
        if char != str(approximation)[i]:
            if i < 2: print("No accurate decimal places")
            else: print(f"{i - 2} accurate decimal place(s)")
            break

    deviation: float = approximation - previous

    if deviation == 0: 
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {approximation - previous}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1