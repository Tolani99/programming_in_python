"""
A program to demonstrate the use
of if statements
"""

BILL_TOTAL= 210

DISCOUNT1 = 10
DISCOUNT2 = 20

if BILL_TOTAL > 100 and BILL_TOTAL < 200:
    print("Bill is greater than 100!")
    BILL_TOTAL = BILL_TOTAL - DISCOUNT1
else:
    print("Bill is less than 100!")

print("Total bill: " + str(BILL_TOTAL))
