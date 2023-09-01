
from random import choice, randint
import numpy as np



#                               1  2  3  4  5  
#                               6  7  8  9  10
#                               11 12 13 14 15
#                               16 17 18 19 20
#                               21 22 23 24 25

class Room():
    def __init__ (self):
        self.num = roomnum
        self.name = roomname



roomnum = 7



def north():
    global roomnum
    if roomnum == 1:
        print ("there is an unimaginable barrier in your way, preventing you from moving north")
    elif roomnum == 2:
        print ("there is an unimaginable barrier in your way, preventing you from moving north")
    elif roomnum == 3:
        print ("there is an unimaginable barrier in your way, preventing you from moving north")
    elif roomnum == 4:
        print ("there is an unimaginable barrier in your way, preventing you from moving north")
    elif roomnum == 5:
        print ("there is an unimaginable barrier in your way, preventing you from moving north")
    else:
        
         roomnum -= 5
         print("you have travelled to the north, where a", roomname , "appears")

   









a = 24


terrain = ["forest", "dark Caves", "waterfall", "time ravaged village", "rock slab", "dense bushes", "clearing","glittering glade",
"amethyst cliffs","sandy shores","abandoned mines","rocky mountain","field","flower garden","buried chest","BattleDex's house",
"TRVSG's house","Coda's house","mysterious well","graveyard","Troll's hideout","Dragon's lair","friendly elf traders",
"shrine to foreign gods","hollow tree"]


room1 = (terrain[randint(0,a)])
print (room1)
terrain.remove (room1)
a -= 1

room2 = (terrain[randint(0,a)])
print(room2)
terrain.remove(room2)
a -= 1

room3 = (terrain[randint(0,a)])
print(room3)
terrain.remove(room3)
a -= 1

room4 = (terrain[randint(0,a)])
print(room4)
terrain.remove(room4)
a -= 1

room5 = (terrain[randint(0,a)])
print(room5)
terrain.remove(room5)
a -= 1

room6 = (terrain[randint(0,a)])
print(room6)
terrain.remove(room6)
a -= 1

room7 = (terrain[randint(0,a)])
print(room7)
terrain.remove(room7)
a -= 1

room8 = (terrain[randint(0,a)])
print(room8)
terrain.remove(room8)
a -= 1

room9 = (terrain[randint(0,a)])
print(room9)
terrain.remove(room9)
a -= 1

room10 = (terrain[randint(0,a)])
print(room10)
terrain.remove(room10)
a -= 1

room11 = (terrain[randint(0,a)])
print(room11)
terrain.remove(room11)
a -= 1

room12 = (terrain[randint(0,a)])
print(room12)
terrain.remove(room12)
a -= 1

room13 = (terrain[randint(0,a)])
print(room13)
terrain.remove(room13)
a -= 1

room14 = (terrain[randint(0,a)])
print(room14)
terrain.remove(room14)
a -= 1

room15 = (terrain[randint(0,a)])
print(room15)
terrain.remove(room15)
a -= 1

room16 = (terrain[randint(0,a)])
print(room16)
terrain.remove(room16)
a -= 1

room17 = (terrain[randint(0,a)])
print(room17)
terrain.remove(room17)
a -= 1

room18 = (terrain[randint(0,a)])
print(room18)
terrain.remove(room18)
a -= 1

room19 = (terrain[randint(0,a)])
print(room19)
terrain.remove(room19)
a -= 1

room20 = (terrain[randint(0,a)])
print(room20)
terrain.remove(room20)
a -= 1

room21 = (terrain[randint(0,a)])
print(room21)
terrain.remove(room21)
a -= 1

room22 = (terrain[randint(0,a)])
print(room22)
terrain.remove(room22)
a -= 1

room23 = (terrain[randint(0,a)])
print(room23)
terrain.remove(room23)
a -= 1

room24 = (terrain[randint(0,a)])
print(room24)
terrain.remove(room24)
a -= 1

room25 = (terrain[randint(0,a)])
print(room25)
terrain.remove(room25)
a -= 1
 
print(terrain)


roomname = room3


north()





