from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take")

    choice = input(">>>")
    if "0" in choice or "1" in choice:
       how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50 :
       print("you are no greedy you win !")
       exit(0)
    else:
        print("you greedy bastard!")


def bear_room():
    print("There is a bear here. ")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
         choice = input(">>>")

         if choice == "take honey:":
            dead("the bear looks at you and slaps your face off.")
         elif choice == "taunt bear" and not bear_moved:
              print("The bear has moved from the door. \n You can go through it now") 
              bear_moved = True
         elif choice == "taunt bear" and bear_moved:
              dead("The bear get pissed of and chews your legs off.")
         elif choice == "open door" and bear_moved:
              gold_room()
         else:
             print("I got no idea what that means")


def ravan_room():
    print("Here you see the great evil Ravan.")
    print("He, it, whatever stares at you and you go insane")
    print("DO you flee for your life or eat your head ?")

    choice = input("> >> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
         dead("Well that was tasty!")
    else:
        ravan_room()


def dead(why):
    print(why, "Good job!")
    exit()


def start():
    print("You are in a dark room!")
    print("There is door to your right and left")
    print("Which one do you take ?")
    choice = input(">>>")
    
    if "right" in choice:
     ravan_room()
    elif "left" in choice:
         bear_room()
    else :
         dead("you starved and died ")


start()
