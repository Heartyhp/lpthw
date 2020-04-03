

numbers = []
print("Numbers you want to enter from 0 to upper limit")
max_element = int(input("++>"))
print("Enter step size")
step = int(input("==>"))
def insert_numbers(max_element, step):
    i = 0
    while i < max_element :
         numbers.append(i)
         print(f"At the top i is {i}")

         i = i + step
         print("numbers now", numbers)
         print(f"at the bottom i is {i}")

    print("The numbers")
    for num in numbers :
        print(num)

def delete_numbers(max_element):
    for i in range(max_element-1):
        numbers.pop()
        

insert_numbers(max_element, step)
for i in numbers:
    print(f"the value is {i}")
delete_numbers(max_element)
for i in numbers :
    print(f"the value is {i}")

print("List is ", numbers)
