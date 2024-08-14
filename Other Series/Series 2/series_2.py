from decimal import Decimal

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.

k: int = 1
approximationSquared: float = 0
approximation: Decimal = 0
previous: Decimal = 0

while True:

    approximationSquared += 6 / pow(k, 2)
    approximation = Decimal(pow(approximationSquared, 1/2))

    print(f"\nIteration {k}")
    print(f"Approximation = {approximation}")

    for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
        try:
            if char != str(approximation)[i]:
                if i < 2: print("No accurate decimal places")
                else: print(f"{i - 2} accurate decimal place(s)")
                break
        except IndexError: print("No incorrect decimal places.")

    deviation: Decimal = approximation - previous

    if deviation == 0: 
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {approximation - previous}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1