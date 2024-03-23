def calculate_average(numbers):
    '''handling null values is a very good way of writing clean code'''
    if numbers is None:
        raise ValueError("Input cannot be None")

    total = sum(numbers)
    return total / len(numbers)

# Example usage:
try:
    data = [10, 20, 30, 40, 50]
    avg = calculate_average(data)
    print(f"The average is: {avg}")
except ValueError as e:
    print(e)

# -------------------------------------------
def multiply(a, b):
    return a * b

# Pure function usage
result = multiply(5, 3)
print(result)  # Output: 15

# No side effects
# The multiply function only takes inputs and produces an output without modifying any external state or variables.
