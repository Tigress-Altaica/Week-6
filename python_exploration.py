"""CSIS 2450: Python Exploration Assignment: Python implementation of
Assignment 2: Part 2"""

# Module Name: python_exploration

# Author: Anneliese Braunegg
# Institution: Salt Lake Community College
# Course: CSIS 2450

# Date Created: Saturday, February 20, 2021
# Date Last Updated: Saturday, February 20, 2021


from enum import Enum


class AccountStanding(Enum):
    """
    Enum representing the standing of a customer payment account
    """
    GOOD = "GOOD"
    FAIR = "FAIR"
    POOR = "POOR"
    CLOSED = "CLOSED"


# Array of customers
CUSTOMERS = ["Amy Garrison","Braydon Beil","Bluebell Nguyen",
		   "Konrad Sears","Cheryl Salas","Rosanna Meyer",
		   "Karis Haley","Enzo Donaldson","Catrina Griffiths",
		   "Gregor Payne","Jermaine Jordan","Zakariya Goulding",
		   "Mehdi Vickers","Zarah Lozano","Mattie Watkins",
		   "Hudson Sheridan","Rahul Tate","Bruno Jefferson",
		   "Shaunie Mccallum","Mica Hendrix","Coco Houston",
		   "Kayla Stanton","Noel Cooper","Tommie Leonard",
		   "Naima Bray","Harley Neville","Sabah Rosas",
		   "Kade Mccartney","Bruce Valenzuela","Elif Ireland",
		   "Nansi Joseph","KeirBetts","Harvie Barnard",
		   "Kady Whitworth","Sadiyah Levine","Sakina Cresswell",
		   "Chantel Wu","Harriette Booth","Isla-Mae Edge",
		   "Daniela Shepherd","Cosmo Lam","Myron Archer",
		   "Caspian Bradford","Elyse Fletcher","Halima Devlin",
		   "Humzah Madden","Bevan Donnelly","Piotr Rice",
		   "Malikah Mejia","Mujtaba Bassett"]

# Array of account numbers (0th index of each sub-array) and payments (remaining
# indices in each sub-array), with main array indices corresponding to the indices
# of the CUSTOMERS array
PAYMENTS = [[1032,47,43,38,61,69,99,47,36,30,99,59,17],
		   [1043,93,48,18,57,52,14,55,87,22,52,56,77],
		   [1005,71,27,52,41,18,86,43,43,95,21,86,43],
		   [1030,13,12,27,81,29,86,31,86,10,54,71,81],
		   [1045,40,91,0,27,21,50,89,28,49,87,23,16],
		   [1040,25,15,63,88,68,60,77,25,63,73,13,10],
		   [1007,24,89,72,49,17,30,96,22,64,56,69,15],
		   [1008,45,42,54,27,65,22,75,51,42,43,97,97],
		   [1049,15,45,26,81,43,38,70,32,30,78,53,77],
		   [1035,21,47,15,28,54,61,15,85,60,95,39,62],
		   [1046,42,93,97,13,19,15,67,100,21,64,28,35],
		   [1029,90,42,61,75,96,25,12,65,66,39,20,52],
		   [1034,75,69,60,78,79,92,38,71,44,41,43,99],
		   [1027,60,59,89,22,86,55,83,67,70,24,70,39],
		   [1024,54,76,55,33,78,91,24,43,61,58,83,78],
		   [1001,94,56,48,30,32,0,0,52,41,46,37,60],
		   [1023,53,24,36,54,79,54,37,61,46,65,34,40],
		   [1022,21,41,49,74,44,91,82,100,12,26,12,23],
		   [1050,94,48,22,19,56,16,72,39,53,11,32,16],
		   [1033,82,21,97,69,50,86,16,55,93,72,70,47],
		   [1044,49,0,14,28,23,84,0,88,0,88,0,93],
		   [1026,26,22,34,63,99,99,50,36,75,64,86,33],
		   [1010,47,43,38,64,80,71,23,80,85,31,13,66],
		   [1003,36,97,15,25,41,77,44,54,72,20,12,85],
		   [1006,86,46,80,63,90,23,91,18,12,83,11,66],
		   [1047,80,73,48,28,11,49,76,14,85,67,65,51],
		   [1002,27,11,100,39,55,26,29,41,90,48,34,81],
		   [1021,94,94,50,16,37,48,56,90,96,25,93,70],
		   [1028,13,55,0,69,67,60,35,45,79,71,67,21],
		   [1042,80,69,29,47,70,22,42,83,26,54,95,70],
		   [1038,30,40,100,90,88,10,39,10,87,14,63,17],
		   [1004,30,84,56,28,13,92,51,52,61,91,68,53],
		   [1041,62,10,24,95,27,49,27,57,97,71,70,99],
		   [1000,10,69,43,91,93,24,74,52,20,76,27,86],
		   [1018,100,51,96,23,76,64,28,49,35,72,51,48],
		   [1019,22,82,37,26,39,81,81,94,50,80,78,88],
		   [1016,88,44,10,78,86,76,0,11,17,49,50,13],
		   [1012,57,67,47,41,43,100,66,23,29,18,55,75],
		   [1014,21,55,55,66,55,92,51,92,86,43,61,51],
		   [1036,42,19,97,27,68,24,69,85,80,43,87,58],
		   [1009,20,34,59,49,13,79,13,11,89,33,49,94],
		   [1013,36,30,50,77,93,30,97,100,68,41,93,21],
		   [1037,90,67,61,88,73,67,11,49,92,75,67,47],
		   [1017,32,73,82,30,55,39,48,79,87,31,99,41],
		   [1039,41,74,74,90,56,18,84,64,58,88,93,83],
		   [1025,32,91,0,0,0,19,87,74,83,64,26,44],
		   [1011,99,11,81,74,91,78,92,85,79,59,19,86],
		   [1020,35,84,81,73,30,90,95,30,68,51,12,83],
		   [1048,57,32,12,75,29,46,71,53,28,65,72,28],
		   [1015,16,86,61,44,63,80,48,25,15,30,45,36]]


def print_out_payment_history_header():
    """
    Print out the header for a customer payment history report.
    """
    print("-------------------------------------------------------------")
    print("Customer Payment History")
    print("-------------------------------------------------------------")
    print("Name                  Account    01      02      03      04      05      06      07      08      09      10      11      12      Standing")
    print("-------------------------------------------------------------")


# TODO: Revise formatting of print statements so that the different customers'
#   printouts line up
def print_out_customer_payment_history(cust_index):
    """
    Print out the payment history for the customer at the specified index in the
    CUSTOMERS array.

    :param cust_index: The index of the customer
    """
    # Customer name
    print(":s  ", CUSTOMERS[cust_index], end="")

    # Account number
    print(":d     ", PAYMENTS[cust_index][0], end="")

    # Payments
    for i in range(1, len(PAYMENTS[0])):
        pay_amt = PAYMENTS[cust_index][pay_index]
        print(":f ", pay_amt, end="")

    # Account standing
    account_standing = account_standing(cust_index)
    print("  " + account_standing)


def account_standing(acct_index):
    """
    Return the account standing for the account at the specified index in the
    PAYMENTS array.

    :param acct_index: The index of the account in the PAYMENTS array

    :return: The standing of the account
    """
    num_of_zero_payments = num_of_zero_payments(acct_index)

    if num_of_zero_payments == 0:
        account_standing = AccountStanding.GOOD
    elif num_of_zero_payments == 1:
        account_standing = AccountStanding.FAIR
    elif num_of_zero_payments == 2:
        account_standing = AccountStanding.POOR
    else:
        account_standing = AccountStanding.CLOSED

    return account_standing


def num_of_zero_payments(acct_index):
    """
    Return the number of zero (0) payments that exist for the account at the
    specified index in the PAYMENTS array.

    :param acct_index: The index of the account in the PAYMENTS array

    :return: The number of zero (0) PAYMENTS that exist for the account
    """
    num_of_zero_payments = 0

    for i in range(1, len(PAYMENTS(acct_index))):
        if PAYMENTS[acct_index][i] == 0:
            num_of_zero_payments += 1

    return num_of_zero_payments


def main():
    # Print out report header
    print_out_payment_history_header()

    # Print the payment history for each customer in the CUSTOMERS array.
    for cust_index in range(0, len(CUSTOMERS)):
        print_out_customer_payment_history(cust_index)


if __name__ == "__main__":
    main()
