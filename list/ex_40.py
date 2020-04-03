"""#dict style

mystaff['Apple']

#module style

mystaff.apple()

print(mystuff.tangerine)

#Class style

thing = MyStuff()
thing.apple()
print(thing.tangerine)
"""

class Song(object):
      def __init__( self, lyrics):
          self.lyrics = lyrics
       
      def sing_a_song(self):
          for line in self.lyrics:
              print(line)

happy_bday = Song(["Happy BIrthday to you",
                    "I dont want to get sued" ,
                    " So I'll stop right there"])

break_up = Song(["Tune sath jo mera choda", "Deewana tera mar jayega"])

happy_bday.sing_a_song()

break_up.sing_a_song()




