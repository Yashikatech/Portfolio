# palindrome_checker.py

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def main():
    # Take input from the user
    text = input("Enter a word or phrase: ").lower().replace(" ", "")

    if is_palindrome(text):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

if __name__ == "__main__":
    main()
