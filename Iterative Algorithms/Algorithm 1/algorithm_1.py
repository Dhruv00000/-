from decimal import Decimal
from time import perf_counter

k: int = 1
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0
previous_aValue: int = 1

def a_n(n: int) -> float:
    global previous_aValue

    previous_aValue *= (1 + 1 / (2*n - 1))
    return previous_aValue

for i in range(1, 11): print(a_n(i))

# while True:

#     iterationStartTime = perf_counter()
#     approximation = pow(a_n(k), 2) / k
#     iterationEndTime = perf_counter()

#     print(f"\nIteration {k}")
#     print(f"Approximation = {approximation}")

#     for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
#         if char != str(approximation)[i]:
#             if i < 2: print("No accurate decimal places")
#             else:
#                 print(f"{i - 2} correct decimal place(s)")
#                 finalAccuracy = i - 2
#             break

#     print(f"Iteration duration: {iterationEndTime - iterationStartTime}  seconds")
#     totalComputationTime += iterationEndTime - iterationStartTime

#     deviation: Decimal = approximation - previous
#     if deviation == 0: 
#         print("Negligible deviation (terminating the program)\n")
#         break
#     elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

#     previous = approximation
#     k += 1

# print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k} iterations.\n")