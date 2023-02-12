# lab3.3_normalise.py
# Description: reads in a string
#              strips any leading or trailing spaces
#              converts all letters to lower case
#              outputs the lengths of original string and the normalised one

row_string = input("Please enter a string:")
normalised_string = row_string.strip().lower()

length_of_raw_string = len(row_string)
length_of_normalised = len(normalised_string)

print(f"That String normalised is:{normalised_string}")
print(f"we reduced the input string from {length_of_raw_string} to {length_of_normalised} characters")
