# Take input for the sequence of numbers
numbers_input = input("Enter a sequence of numbers separated by commas: ")
# Convert the input string into a list of integers
numbers = [int(num.strip()) for num in numbers_input.split(",")]

# Take input for the target number
target = int(input("Enter the target number: "))

# Create a dictionary to store the complement of each number and its index
num_to_index = {}

# Iterate through the list of numbers
for index, num in enumerate(numbers):
    # Calculate the complement needed to reach the target
    complement = target - num
    
    # Check if the complement exists in the dictionary
    if complement in num_to_index:
        # If found, return the indices of the complement and current number
        print([num_to_index[complement], index])
        break
    
    # Otherwise, add the current number and its index to the dictionary
    num_to_index[num] = index
else:
    # If no solution is found, return an empty list or raise an exception
    print("FAILED")