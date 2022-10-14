# author: JHR 10/14/22

# defining variables
word = "flibbertigibbet"
firstname = "jack"
sentence = "I wish, I wish, I was a fish."

# storing t index as variable
letter_t = word.find("t")

# printing the letter after t
print (word[letter_t + 1])

# converting to uppercase and printing 
print (firstname.upper())

# printing sentence with comma as delimiter
print (sentence.split(sep=",", maxsplit=-1))