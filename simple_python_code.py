# Simple and professional example of a Python script for GitHub portfolio

def calculate_factorial(number):
    """Calculate factorial of a number with debug information"""
    if number == 0 or number == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, number+1):
            factorial *= i
        return factorial

def main():
    number = int(input("Enter a number: "))
    result = calculate_factorial(number)
    print(f"The factorial of {number} is {result}.")

if __name__ == "__main__":
    main()
