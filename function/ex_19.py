from sys import argv
def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"you have {cheese_count} cheese!")
    print(f"you have {box_of_crackers} boxes of crackers!")
    print("Man thats enough for a party")
    print("\n Get an Blnket")


print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)


print("OR , We can use variables from our script")
amount_of_cheese = 13
amount_of_crackers = 45
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combiine the two , variable and Math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

def run( *args ):
    arg1, arg2, arg3, arg4, arg5 = args
    if arg1 == "add":
       sum = arg5 + arg2 + arg3 + arg4
       print(f"sum is {sum}")
    elif arg1 == "mul":
         multi = arg2 * arg3 * arg4 * arg5
         print("multi value is", multi)

run("add", 1, 2, 3, 4)
run("add", 1.2, 2.1 , 0.6667, 9)
run("mul", 100, 5, 3, 6)
run("mul", 1.2, 5.1, 4, 5)


