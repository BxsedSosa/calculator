# Ask the user for the 1st number
# Ask the user for the 2nd number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal


def prompt(message):
    print(f"==> {message}")


def is_valid_number(num):
    try:
        int(num)
    except ValueError:
        return True

    return False


prompt("Welcome to Calculator!")

prompt("What's the first number?")
number1 = input()

while is_valid_number(number1):
    prompt("This is not a number!")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while is_valid_number(number2):
    prompt("This is not a number!")
    number2 = input()

prompt(
    "What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide"
)
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:
    case "1":
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) // int(number2)
    case _:
        prompt("You didn't provide a number 1-4")

prompt(f"The result is: {output}")
