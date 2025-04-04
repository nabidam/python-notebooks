# Take input for the number
number = input("Enter a number: ").strip()

# Check if the number is equal to its reverse
if number == number[::-1]:
    print(f"The number {number} is a palindrome.")
else:
    print(f"The number {number} is not a palindrome.")