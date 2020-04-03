ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not  ten things in that list. Lets fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "NIght", "Song" , "Frisbee", " Corn", "Banana", "Girl", "Boy"]

while len(stuff)!=10 :
      next_one = more_stuff.pop()
      print("Adding next_one", next_one)
      stuff.append(next_one)
      print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Lets do some things with stuff")

print(stuff[1])
print(stuff[-1]) # Its fancy
print(stuff.pop())
print(' '.join(stuff)) #Whats so cool!
print('#'.join(stuff[3:5])) #super steller
