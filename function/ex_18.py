from sys import argv 
#print function is take 2 values of argv
def print_two(*argv):
    arg1, arg2,arg3 = argv
    print(f"Printing arg1: {arg1}, Printing arg2 : {arg2}, printing arg3 : {arg3}")

def print_2(*argv):
    arg1, arg2 = argv
    print(f"Printing arg1: {arg1}, Printing arg2 : {arg2}")

def print_ok(h1,h2):
    arg1 = h1
    arg2 = h2
    print(f"Printing arg1: {h1}, Printing arg2 : {h2}")

#print fuction object
print_two("hardik", "pagal","hay")
print_2("hardik", "pagal")
print_ok("hardik", "shi me pagal hai")

