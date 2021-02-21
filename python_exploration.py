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

# TODO: Fill in payments array
payments = []


def print_out_payment_history_header():
    """Print out the header for a customer payment history report."""
    # TODO
    pass


def print_out_customer_payment_history(cust_index):
    """
    Print out the payment history for the customer at the specified index in the
    customers array.

    :param cust_index: The index of the customer
    """
    # TODO
    pass


def account_standing(acct_index):
    """
    Return the account standing for the account at the specified index in the
    payments array.

    :param acct_index: The index of the account in the payments array

    :return: The standing of the account
    """
    # TODO
    pass


def num_of_zero_payments(acct_index):
    """
    Return the number of zero (0) payments that exist for the account at the
    specified index in the payments array.

    :param acct_index: The index of the account in the payments array

    :return: The number of zero (0) payments that exist for the account
    """
    # TODO
    pass

def main():
    # Print out report header
    print_out_payment_history_header()

    # Print the payment history for each customer in the customers array.
    for cust_index in range(0, len(customers)):
        print_out_customer_payment_history(cust_index)

if __name__ == "__main__":
    main()
