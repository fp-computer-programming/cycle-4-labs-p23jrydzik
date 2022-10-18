# author: JHR 10/18/22

# creating input variables
animal_name = input("What is your animals name?")
dish_name = input("What is your animal bringing?")

# taking first letters from each input
first_letter_1 = animal_name[0]
first_letter_2 = dish_name[0]

# reversing dish and taking first level
reverse = dish_name[::-1]
last_letter_2 = reverse[0]

# boolean for if they are all equal
if first_letter_1 == first_letter_2 == last_letter_2:
    print ("true")
else:
    print ("false")