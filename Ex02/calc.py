
result = None  # Store the current result
operator = None  # Store the last operator entered

while True:
    user_input = input().strip()

    if user_input == "END":
        break
    elif user_input == "=":
        if result is not None:
            print(result)
    elif user_input in {"+", "-", "*", "/"}:
        operator = user_input
    else:
        try:
            number = int(user_input)
            if result is None:
                result = number
            elif operator:
                if operator == "+":
                    result += number
                elif operator == "-":
                    result -= number
                elif operator == "*":
                    result *= number
                elif operator == "/":
                    if number == 0:
                        print("Error: Division by zero")
                        result = None
                    else:
                        result //= number  # Integer division
                operator = None  # Reset operator after applying it
        except ValueError:
            print("Invalid input")
