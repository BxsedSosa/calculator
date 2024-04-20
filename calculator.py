# Ask the user for the 1st number
# Ask the user for the 2nd number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal
import json

with open("messages.json", "r") as file:
    MESSAGE = json.load(file)


def prompt(message):
    print(f"==> {message}")


def is_valid_number(num):
    try:
        int(num)
    except ValueError:
        return True

    return False


while True:
    prompt(MESSAGE["welcome"])

    prompt(MESSAGE["questions"]["first_num"])
    number1 = input()

    while is_valid_number(number1):
        prompt(MESSAGE["edge_case"]["not_num"])
        number1 = input()

    prompt(MESSAGE["questions"]["second_num"])
    number2 = input()

    while is_valid_number(number2):
        prompt(MESSAGE["edge_case"]["not_num"])
        number2 = input()

    prompt(MESSAGE["questions"]["operator"])

    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGE["edge_case"]["not_op"])
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

    prompt(MESSAGE["result"])

    prompt(MESSAGE["try_again"])
    resume = input()
    if resume != "1":
        break
