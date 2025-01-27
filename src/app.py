import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def parse_arguments():
    parser = argparse.ArgumentParser(description="Mathematical Calculator")
    
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"],
                        help="The mathematical operation to perform.")
    parser.add_argument("a", type=float, help="The first number.")
    parser.add_argument("b", type=float, help="The second number.")
    return parser.parse_args()

def main():
    args = parse_arguments()
    operation = args.operation
    a = args.a
    b = args.b

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            raise ValueError("Unsupported operation.")

        print(f"The result of {operation}({a}, {b}) is: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()