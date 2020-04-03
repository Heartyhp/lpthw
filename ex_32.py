the_count = [1,2,3,4,5]
fruits = ["apples", "oranges", "pears", "apricots"]
changes = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first tpe of for loop goes through a list

for number in the_count:
    print(f"This is count {number}")

#same as above

for fruit in fruits :
    print(f"fruits of type : {fruit}")

#also we can go through mixed list too
# Notice we have to use  {} since we dont know whats in it

for i in changes :
    print(f"I got {i}")

# We can also build lists , first start with an empty one

elements = []

# then use range function to do 0 to 5 counts

for i in range(0,6):
    print(f"adding element {i} to list")
    elements.append(i)

# now we can print out elements of a list 

for i in elements :
    print(f"Element is {i}")
