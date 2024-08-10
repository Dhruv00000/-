from math import pi, log10, floor, factorial

def double_factorial(n: int):
    return double_factorial(n - 2) * n if n not in [0, 1] else 1
# def factorial(n: int):
#     return factorial(n - 1) * n if n != 0 else 1

k: int = 0
approximation: float = 0
previous: float = 0

while True:

    try: approximation += 2 * (factorial(k) / double_factorial(2*k + 1))
    except RecursionError: break # maximum recursion depth = 999. But that does not matter because this series converges much before this depth is hit.

    print(f"\nIternation {k}")
    print(f"Approximation = {approximation}")

    accuracy: int = floor(abs(log10(abs(approximation - pi)))) - 1
    accuracy = max(accuracy, 0) # limits the 'accuracy' variable to be 0 at negative values.
    if k == 7: accuracy = 1 # writing a different expression for this case (which doesnt work with the above expression) would have required too much effort.
    print(f"{accuracy} accurate decimal place(s)")

    deviation: float = approximation - previous

    if deviation == 0: print("Negligible deviation")
    else: print(f"Deviation from previous iteration: {approximation - previous}")

    previous = approximation
    k += 1