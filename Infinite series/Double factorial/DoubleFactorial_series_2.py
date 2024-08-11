from decimal import Decimal

def double_factorial(n: int):
    return double_factorial(n - 2) * n if n not in [0, 1] else 1
def factorial(n: int):
    return factorial(n - 1) * n if n != 0 else 1

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.

# def double_factorial_alt(n: int):

#     result: int = 1

#     for i in range(n, -1, -2):
#         if i in [0, 1]: return result
#         else: result *= i

k: int = 0
approximation: float = 0
previous: float = 0

while True:

    approximation += (3 * Decimal(pow(3, 1/2)) * factorial(k)) / (pow(2, k) * double_factorial(2*k + 1) * 2)

    print(f"\nIteration {k + 1}")
    print(f"Approximation = {approximation}")

    error: int = abs(approximation - pi)
    for i in range(46): # log10(error) kept giving me problems so I just wrote my own makeshift log10 algorithm.
        
        error *= 10

        if error >= 1:
            if i != 0: print (f"{i - 1} accurate decimal places")
            else: print("no accurate decimal places")
            break

    deviation: float = approximation - previous

    if deviation == 0: 
        print("Negligible deviation (terminating the program)\n")
        break
    else: print(f"Deviation from previous iteration: {approximation - previous}")

    previous = approximation
    k += 1