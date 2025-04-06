# Define the mapping of Roman numerals to their integer values
roman_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

# Take input for the Roman numeral
roman = input("Enter a Roman numeral: ").strip().upper()

# Validate the input
valid_roman = "IVXLCDM"
if not all(char in valid_roman for char in roman):
    print("Invalid Roman numeral. Please enter a valid Roman numeral.")
    exit()

# Initialize variables to store the result and previous value
total = 0
prev_value = 0

# Iterate through the Roman numeral from right to left
for char in reversed(roman):
    # Get the integer value of the current Roman numeral character
    current_value = roman_map[char]
    
    # If the current value is less than the previous value, subtract it
    if current_value < prev_value:
        total -= current_value
    else:
        # Otherwise, add it to the total
        total += current_value
    
    # Update the previous value for the next iteration
    prev_value = current_value

# Print the result
print(f"The numerical value of the Roman numeral {roman} is {total}.")