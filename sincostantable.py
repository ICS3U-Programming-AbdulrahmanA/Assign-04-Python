#!/usr/bin/env python3
# Created By: Abdul
# Date: 12/3/2025
# Program to ask the user for month and year and display days in month

# import math module for trigonometric functions
import math


def main():
    # welcome message for the user
    print("Welcome to the degree table generator!")
    # ask until the user provides a valid choice: sin, cos, or tan
    while True:
        user_input = input(
            "Please enter either sin, cos, or tan to see the degree table: "
        )
        # check for a valid option
        if user_input == "sin" or user_input == "cos" or user_input == "tan":
            break
        else:
            # invalid input, ask again
            print("Invalid input, try again.")

    # if the user chose sine, compute and print sin for 0..360 degrees
    if user_input == "sin":
        for degree in range(0, 361, 1):
            # does the actual sin function on the degree
            sin_value = math.sin(degree)
            # print degree and sine value rounded to 5 decimal places
            print(f"{degree} = {round(sin_value, 5)}")
    # if the user chose cosine, compute and print cos for 0..360 degrees
    elif user_input == "cos":
        for degree in range(0, 361, 1):
            # does the actual cos function on the degree
            cos_value = math.cos(degree)
            print(f"{degree} = {round(cos_value, 5)}")
    # otherwise the user chose tangent, compute and print tan for 0..360 degrees
    else:
        for degree in range(0, 361, 1):
            # does the actual tan function on the degree
            tan_value = math.tan(degree)
            print(f"{degree} = {round(tan_value, 5)}")


if __name__ == "__main__":
    # run the main function when the script is executed directly
    main()
