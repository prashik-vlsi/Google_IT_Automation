def calculate_average(total, count):
    if count == 0:
        raise ValueError("Count must not be zero")
    return total / count

try:
    print("Average:", calculate_average(100, 0))
except ValueError as error:
    print("Error:", error)
