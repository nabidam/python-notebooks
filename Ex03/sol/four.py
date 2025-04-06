# Take input for the ordered sequence of numbers
numbers_input = input("Enter an ordered sequence of numbers separated by commas: ").strip()
if not numbers_input:
    numbers = []
else:
    numbers = [int(num.strip()) for num in numbers_input.split(",")]

# Take input for the target number
target = int(input("Enter the target number: "))

# Use binary search to find the position or index
left, right = 0, len(numbers) - 1

while left <= right:
    mid = (left + right) // 2
    
    if numbers[mid] == target:
        # If the target is found, return its index
        print(f"The target number {target} is found at index {mid}.")
        print(mid)
        break
        
    elif numbers[mid] < target:
        # Move to the right half
        left = mid + 1
    else:
        # Move to the left half
        right = mid - 1

else:
    # If the loop ends, `left` is the insertion index
    print(f"The target number {target} would be placed at index {left}.")