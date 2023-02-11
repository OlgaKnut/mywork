# lab3.2_convert.py
# Description: takes in a float amount in euros and retuns that absolute amount in cents.
# Author: Olga Knutova

euro_amount = float(input("Please enter an amount: "))
cent_amount = int(euro_amount*100)
absolute_amount = abs(cent_amount)
print("That amount in cent is:{}" .format (absolute_amount))
