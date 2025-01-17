from time import perf_counter

k: int = 1
approximationExponentiated: float = 0
approximation: str = ""
finalAccuracy: int = 0
terminated: bool = False
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0

def factorial(n: int) -> int:
    return factorial(n - 1) * n if n != 0 else 1

def Bernoulli(num: int) -> float:
    if num == 0: return 1

    result: float = sum(
        (Bernoulli(l) * factorial(num))
        / (factorial(l) * factorial(num - l) * (num - l + 1))
        for l in range(num)
    )
    return 1 - result

while True:
    try:
        iterationStartTime = perf_counter()
        approximation += str(int(10 * ((pow(10, k - 1)(((2 * pow(-1, k) * factorial(2*k - 2)) / (pow(2, 2*k - 2) * Bernoulli(2*k - 2) * (1 - pow(2, 1 - k)) * (1 - pow(3, 1 - k)) * (1 - pow(5, 1 - k)) * (1 - pow(7, 1 - k)))) ** (2*k - 2))) % 1)))
    except (OverflowError, RecursionError) as e:
        print("\nThe entered value is too large to handle.\n")
        terminated = True
        break

    approximation = Decimal(pow(approximationExponentiated, 1 / (2*n)))
    iterationEndTime = perf_counter()

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
    elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1

if not terminated: print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k} iterations.\n")