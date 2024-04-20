# Ask the user for the 1st number
# Ask the user for the 2nd number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal
import json

USER_LANG = ["en", "es", "ch", "jp"]

with open("text.json", "r") as file:
    MSG = json.load(file)


def prompt(key):
    return f"{MSG['arrow']} {key}"


def valid_language(text):
    selected_lang = input(f"{prompt(text)}\n")

    while selected_lang not in USER_LANG:
        selected_lang = input(f'{prompt(MSG["en"]["not-lang"])}\n')

    return selected_lang


def welcome_message(lang):
    print(prompt(MSG[lang]["welcome"]))


def invalid_number(num):
    try:
        int(num)
    except ValueError:
        return True

    return False


def number_selection(text):
    user_num = input(prompt(f"{text}\n"))

    while invalid_number(user_num):
        user_num = input(prompt(f'{MSG[language]["not-num"]}\n'))

    return user_num


def operation(text):
    operator = input(prompt(f"{text}\n"))
    operator_selection = ["1", "2", "3", "4"]

    while operator not in operator_selection:
        operator = input(prompt(f'{MSG[language]["not-selection"]}\n'))

    return operator


def result(num1, num2, op):
    match op:
        case "1":
            op = '+'
            result = float(num1) + float(num2)
        case "2":
            op = '-'
            result = float(num1) - float(num2)
        case "3":
            op = '*'
            result = float(num1) * float(num2)
        case "4":
            op = '/'
            if float(num2) == 0:
                print(prompt(MSG[language]["zero-division"]))
                exit(1)
            result = float(num1) / float(num2)
    print(prompt(f"The result is: {num1} {op} {num2} = {result}"))



def main():

    welcome_message(language)
    number1 = number_selection(MSG[language]["first-num"])
    number2 = number_selection(MSG[language]["second-num"])
    operator = operation(MSG[language]["operator"])
    result(number1, number2, operator)


language = valid_language(MSG["en"]["select-lang"])

while True:
    main()

    resume = input(prompt(f'{MSG[language]['try-again']}\n'))
    if resume != '1':
        break
