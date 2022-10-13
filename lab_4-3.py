# author: JHR 10/12/22

# defining input variables
first_letter = input ("What is the first letter in your first name? (Please use Capitals)")
last_letter = input ("What is the last letter in your first name?")

# comparing variables using conditionals
if first_letter < last_letter:
    print ("Your first letter comes before your last.")
elif first_letter > last_letter:
    print ("Your last letter comes before your first.")
else:
    print ("Your first letter and last letter are the same.")

