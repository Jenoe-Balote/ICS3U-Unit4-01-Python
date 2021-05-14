#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program runs an add loop for positive integers

import string


def main():
    # this function uses a while loop
    loop_counter = 0
    total = 0

    # this function runs the "add loop" program
    # input
    print("Welcome!")
    num_integer = str(input("Enter a positive integer: "))

    # process and output
    try:
        num_integer = int(num_integer)
        while loop_counter <= num_integer:
            total = total + loop_counter
            loop_counter = loop_counter + 1
        print("The sum is {0}!".format(total))
    except Exception:
        print("{0} is invalid data.".format(num_integer))
    finally:
        print("Thanks for participating!")


if __name__ == "__main__":
    main()
