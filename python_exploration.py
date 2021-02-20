"""CSIS 2450: Python Exploration Assignment: Python implementation of
Assignment 2: Part 2"""

# Module Name: python_exploration

# Author: Anneliese Braunegg
# Institution: Salt Lake Community College
# Course: CSIS 2450

# Date Created: Saturday, February 20, 2021
# Date Last Updated: Saturday, February 20, 2021


# TODO: Fill in customers array
customers = []


def print_out_payment_history_header():
    # TODO
    pass


def print_out_customer_payment_history(cust_index):
    # TODO
    pass


def account_standing(acct_index):
    # TODO
    pass


def num_of_zero_payments(acct_index):
    # TODO
    pass


if __name__ == "__main__":
    # Print out report header
    print_out_payment_history_header()

    # Print the payment history for each customer in the customers array.
    for cust_index in range(0, len(customers)):
        print_out_customer_payment_history(cust_index)
