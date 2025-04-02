def add_numbers(a, b):
    sum = a + b  # ❌ Using 'sum' as a variable name (shadows built-in function)
    return sum


def divide(a, b):
    return a / b  # ❌ No handling for division by zero


def unused_function():  # ❌ Unused function
    print("This function is never called")


if __name__ == "__main__":
    print(add_numbers(5, "10"))  # ❌ Type error: adding int and string
    print(divide(10, 0))  # ❌ Division by zero error

