from sys import exit
from random import randint
from textwrap import dedent

class scene(object):

    def enter(self):
        print("This scence is not yet configured.")
        print("Subclass it and impliment enter().")
        exit(1)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
  
        while current_scene != last_scene:
           next_scene_name = current_scene.enter()
           current_scene = self.scene_map.next_scene(next_scene_name)


      # be sure to be print out the last scene
     current_scene.enter()

class Death(Scene):
     quips = [
         "you died. you kinda suck at this.",
         "your mom would be proud...if she were smarter.",
         "such a luser.",
         "i have a small puppy that's better at this.",
         "you're worse than your dad's jokes."
     ]
def enter (self):
    print(Death.quips[randint(0,len(self.quips)-1)])
    exit(1)
class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent("""The Gothons of planet percal #25 have invaded your ship and destroyed your entire crew.
                        You are the last surviving member and your last mission is to get the neutron destruct bomb from the weapons Armmory,
                        put it in the bridge,and blow the ship up after getting into an escape pod.
                        You're running down the central corridor to the weapons Armory when a gothon jumps out,
                	red scaly skin,dark grimy teeth,and evil clown costume flowing around his hate filled body.
			he's blocking the door to the Armory nd about to pull a weapon to blast you.
                        """))
        action=input("> ")
        
        if action == "shoot!":
           print(dedent("""
                         quick on the draw you yank out your blaster and fire it at the gothon..
			his clown costume is flowing and moving around his body, which throws off your aim.
			your laser hits his costume but misses him entirely.
 			this completely ruins his brand new costume his mother bought him,which makes him fly into an insane rage
                        and blast you repeatedly in the face until you are dead. then he eats you.
                       """))
		  return 'death'
        elif action == "dodge!":
            print(dedent("""
                  Luckey for you they made you learn Gothon insults in the academy. you tell the one Gothon joke ypu know:
                  zabb zabak zab zabak zabba ahhh jura joom barabar jhoom. The Gothon stops , tries not to laugh, than 
                  burst out laughing and can't move . while he is laughing you run up and shooot him square in the head 
                  putting him down, then jump through the Weapon Armory door. """))
   
           return 'laser_weapon_armory'

      else:
          print("DOES NOT COMPUTE!")
          return 'central_corridor'




C
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""you do a drive roll into the weapon armory, crouch and scan 
                     the room for more gothons that might bee hiding . It's dead 
                     quite, too quite. you stand up and run to the far side of the
                     room and find the neutron bomb in its Container. 
                     There is a keypad lock on the ox and you need the code to get 
                     the bomb out . If you get the code wrong 10 times then  the 
                     lock closes forever and you cant get the bomb . the code is a 3 digit.
                     """))
      code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
      guess = input("[keypad]>"
      guseses = 0

     while guess != code and guesses < 10:
         print("BZZZZEDDD!")
         guesses += 1
         guess = input("[keypad]> ")

    if guess == code:
        print(dedent("""
                          
 																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											

     
                           


   


     


