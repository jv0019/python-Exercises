def divide_by_number():
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    finally:
        print("Execution completed.")

# Example usage
divide_by_number()