#f"some stuff here {avariable}"
#f"some other stuff {anothervar}"
#Declaring a variable and assign ing a value 10 to variavle
types_of_people = 10

#formatting  variable in string using f at the starting of string so that in {value} will sit in plaace of name of variable.
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
#formatting  variable in string using f at the starting of string so that in {value} will sit in plaace of name of variable.
y = f"Those who know {binary} and those who {do_not}."

#printing formatted strings


print(x)
print(y)


#printing formatted strings
print(f"I said : {x} ")

#printing formatted strings
print(f"I also said :{y}")

hillarious = False
joke_evaluation = "Isn't that joke so funny?!{}"

#printing formatted strings
print(joke_evaluation.format(hillarious))

w = " This is the left side of ..."
e= "a string with a right side."

print(w+e)
