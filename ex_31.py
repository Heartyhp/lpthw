print(""" you enter a dark room with doors.
      DO you go through door #1 or door#2 or door 3 or door4 ?""")

door = input("-->")

if  door == "1" :
    print("There's a giant Bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take cake/ \n 2. Scream at bear.")

    bear = input(">>")
  

    if bear == "1":
       print("The bear eats your face off ! Good job")
    elif bear == "2":
       print("The bear eats your legs off ! Good job")

    else: 
      print(f"Well , doing {Bear} is probably better .")
      print("Bear RUns away")

elif door == "2" :
     print("you stare at the endless abyss at Cthulu's Ratina.")
     print("1. Blue barries.  \n 2. Yellow jacket cloathespins. \n 3.Understanding revolvers yelling melodies.")
     
     insanity = input("<-->")
     if insanity == "1" or insanity == "2":
       print("Your body survives powered by a mind of jello")
       print("good JOb")

     else :
         print("The insainity rots your eyes into a pool of musk")
         print("Good Job !")
elif door == "3":
      
      print("""You are seeing towards Hill press 1 if you want to climb hill \n or select 2. if you want to do sucide \n """)
      choice = input("===>")
      if choice == "1" :
         print("Hurreh you are on the top of Hill")
      elif choice == "2":
           print("You are died") 
      else:
          print("you think too much")
else :
     print("You strumble around and fall on a Knife and die. Good job!")    
