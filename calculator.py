# Ask the user for the 1st number
# Ask the user for the 2nd number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal
import json

with open("text.json", "r") as file:
    MESSAGE = json.load(file)


def prompt(key):
    message = messages(key)
    print(f"==> {message}")


def is_valid_number(num):
    try:
        int(num)
    except ValueError:
        return True

    return False


def messages(key):
    return MESSAGE[selected_lang][key]


while True:
    selected_lang = "en"

    prompt("lang")
    selected_lang = input()

    while selected_lang not in ["en", "es", "ch", "jp"]:
        selected_lang = "en"
        prompt("not-lang")
        selected_lang = input()

    prompt("welcome")
    prompt("first-num")
    number1 = input()

    while is_valid_number(number1):
        prompt("not-num")
        number1 = input()

    prompt("second-num")
    number2 = input()

    while is_valid_number(number2):
        prompt("not-num")
        number2 = input()

    prompt("operator")

    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("not-selection")
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            if float(number2) == 0:
                prompt("zero-division")
                exit(1)
            output = float(number1) // float(number2)

    print("==>", MESSAGE[selected_lang]["result"], output)

    prompt("try-again")
    resume = input()
    if resume != "1":
        break
