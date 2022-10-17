# author: JHR 10/17/22

#defining variables with inputs
person1 = input ("What is your name?")
person2 = input ("And what is your name?")

#adding variables via interpolation 
sentence = "Hello, {0}. My name is {1}." .format(person1,person2)

#printing whole sentence
print (sentence)
