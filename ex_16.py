from sys import argv

script, filename = argv 

print(f'We are going to erase{filename}')
print('If you dont want then press ^c Ctlr + c, ')
print("if you dont want then hit RETURN")

input("----?----")

print("opening file.....")
target = open(filename)

print("Turncating the file. Good bye!")

target.truncate()

print("Now I'm going to ask you three lines")


line1 = input("Line---1")
line2 = input("line----2")
line3 = input("line----3")


print("I am going to write these lines into file.")

target.write(line1+"\n"+ line2 + "\n" + line3)
#target.write("\n")


#target.write(line2)
#target.write("\n")


#target.write(line3)
#target.write("End")

print("And finally we close it")

target.close()

