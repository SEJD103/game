from random import randint, choice

# Super class for all living things
class LivingThing():
    def __init__ (self):
        self.name = "some name"
        self.health = 1
    def tire(self):
        self.health = self.health - 2
    def hurt(self):
        self.health = self.health - randint (0,self.health)
    def regen(self):
        self.health = self.health + 1

# this is an attempt at having a room system in place.
class Room():
    def __init__ (self,name,number):
        self.roomnum = number
        self.roomname = name

#this is an attempt at an item class
class item():
    def __init__ (name, dmg, value, uses):
        name = ""
        dmg = 0
        value = "0 gold"
        uses = "infinite"

# This is the monster class
class Monster (LivingThing):
    def __init__ (self,name,health):
        self.name = name
        self.health = health 

def credits():
    print("game over")

#this will decide which boss the player will eventually fight
goblin=Monster("Goblin",20)
dragon=Monster("Dragon",10)
kraken=Monster("Kraken",15)
monsters = []
monsters.append(goblin)
monsters.append(dragon)
monsters.append(kraken)
monster = choice(monsters)

# this will make the rooms different every time the game is played
random_terrain = ["forest", "dark caves", "waterfall", "time ravaged village", "rock slab", "dense bushes", "clearing","glittering glade",
"amethyst cliffs","sandy shores","abandoned mines","rocky mountain","field","flower garden","buried chest","BattleDex's house",
"TRVSG's house","Coda's house","mysterious well","graveyard",monster.name + "'s hideout","toadstool garden","friendly elf traders",
"shrine to foreign gods","hollow tree","sandy beach"]

terrain = []
a = 25
roomnum = 2
while a > 0:
    room1 = (random_terrain[randint(0,a)])
    random_terrain.remove (room1)
    a -= 1
    terrain.append(room1)
name = terrain[2]
current_room=Room("",2)

# This is the Player's class. Maybe I can let player choose different classes?
class Player (LivingThing):
    def __init__ (self,name):
        self.name = name
        self.health = 15
        self.status = "regular"
        self.gold = 0
        self.inv_healpotion = 1
        self.roomnum = 2
        self.roomname = terrain[self.roomnum]

# this function will print all the availible commands
    def help(self,monster):
        print ('Your choices are:')
        for key in Commands.keys():
            print(key)

# I added a healing potion, and ways to find them while exploring
    def heal(self,monster):                                                    
            if self.inv_healpotion > 0:
                self.health = self.health + 3
                self.inv_healpotion = self.inv_healpotion - 1
                print (self.inv_healpotion, "potion/s left, health = ", self.health)
            else: print("no healing potions in inventory")

# I added an inventory function, so a player can see how many healing potions, gold pieces and magical items they have
    def inventory(self, monster):
        print ("you have",self.gold, "gold")
        print ("you have",self.inv_healpotion, "healing potions")

# this function will show the player various stats i.e. player name, monster health etc.
    def stats(self,monster):
        print("you are", self.name)
        print("with health of", self.health)
        print("your status is", self.status)
        print(monster.name , "health is", monster.health)

    def explore(self,monster):
# I added a bit of code to stop the player being able to explore when confronted
        if self.status == "confronted":
            print("you cannot explore this area right now, you are in combat!") 
        else:
            rand = randint (0,4)
            
            if rand == 0 or rand == 1:
                print("you explore the ", terrain[current_room.roomnum],"and find a cool looking potion")
                self.inv_healpotion += 1
                print("+ 1 healing potion")
            elif rand == 2:
                print("you explore the ", terrain[current_room.roomnum],"and a cute rabbit pops out of the shadows")
                print("wow, what a cute bunny!")
                answer = input("do you want to hurt the bunny? y/n >> ")
                if answer == "y":
                    print("you should learn not to attack innocent creatures. the bunny spins on its heel, kicking you in the jugular with its razor sharp back left foot claws,"+
                          " killing you instantly")
                    self.health = 0
                else:
                    self.health += 5
                    print("Good job. Animal cruelty is bad. +5 health")
                    print("your health is now", self.health)
            elif rand == 3 or rand == 4:
                print("you explore the", terrain[current_room.roomnum],"but you find nothing of use")


            
# this function allows you to fight the monster if the monster has confronted you.
    def fight(self,monster):
        if self.status == "confronted":
            self.hurt()
            monster.hurt()
            print(monster.name, "attacks you")
            if self.health <= 0:
                print("you were killed by the", monster.name)
            elif monster.health > 0:
                print("you survived the", monster.name)
                print("your health is now", self.health)
                # I removed a line here so that once the monster has confronted you, your status will not change until you kill the monster
            else:
                print("victory! You defeated the", monster.name)
        else:
            print("you are safe. There are no monsters near")

# i changed the run command to automatically hurt you but you also escape automatically
    def run(self,monster):
        rand = randint(0,4) 
        if rand == 0:
            self.health -= randint(1,5)
            if rand == 1:
                self.health -= randint(1,5)
        elif rand == 2:
            self.health -= randint(5,10)
        elif rand == 3:
            self.health -= randint(5,10)
        elif rand == 4:
            self.health -= randint(11,14)
        self.status = "normal"
        print("the",monster.name,"attacks you as you run and hurts you. You now have",self.health,"health remaining")

# hopefully you can navigate around the map with these commands
    def north(self,monster):
        global current_room
        if current_room.roomnum == 0:
            print ("there is an unimaginable barrier in your way, preventing you from moving north")
        elif current_room.roomnum == 1:
            print ("there is an unimaginable barrier in your way, preventing you from moving north")
        elif current_room.roomnum == 2:
            print ("there is an unimaginable barrier in your way, preventing you from moving north")
        elif current_room.roomnum == 3:
            print ("there is an unimaginable barrier in your way, preventing you from moving north")
        elif current_room.roomnum == 4:
            print ("there is an unimaginable barrier in your way, preventing you from moving north")
        else:
            current_room.roomnum -= 5
            current_room.roomname = terrain[current_room.roomnum]
            print("you have travelled to the north, where you come to", current_room.roomname )

# this is the same thing as north, but instead of going in an "upwards" direction, you travel towards the right of the map
    def east(self,monster):

        if current_room.roomnum == 4:
            print ("there is an unimaginable barrier in your way, preventing you from moving east")
        elif current_room.roomnum == 9:
            print ("there is an unimaginable barrier in your way, preventing you from moving east")
        elif current_room.roomnum == 14:
            print ("there is an unimaginable barrier in your way, preventing you from moving east")
        elif current_room.roomnum == 19:
            print ("there is an unimaginable barrier in your way, preventing you from moving east")
        elif current_room.roomnum == 24:
            print ("there is an unimaginable barrier in your way, preventing you from moving east")
        else:
            current_room.roomnum += 1
            current_room.roomname = terrain[current_room.roomnum]
            print("you travel to the east, and you come across", current_room.roomname)

# this function takes the player towards the left of the map
    def south(self,monster):

        if current_room.roomnum == 20:
            print ("there is an unimaginable barrier in your way, preventing you from moving south")
        elif current_room.roomnum == 21:
            print ("there is an unimaginable barrier in your way, preventing you from moving south")
        elif current_room.roomnum == 22:
            print ("there is an unimaginable barrier in your way, preventing you from moving south")
        elif current_room.roomnum == 23:
            print ("there is an unimaginable barrier in your way, preventing you from moving south")
        elif current_room.roomnum == 24:
            print ("there is an unimaginable barrier in your way, preventing you from moving south")
        else:
            current_room.roomnum += 5
            current_room.roomname = terrain[current_room.roomnum]
            print("you travel south, not resting until", current_room.roomname," appears in the distance")
            
# this function will take you towards the bottom of the map
    def west(self,monster):

        if current_room.roomnum == 0:
            print ("there is an unimaginable barrier in your way, preventing you from moving west")
        elif current_room.roomnum == 5:
            print ("there is an unimaginable barrier in your way, preventing you from moving west")
        elif current_room.roomnum == 10:
            print ("there is an unimaginable barrier in your way, preventing you from moving west")
        elif current_room.roomnum == 15:
            print ("there is an unimaginable barrier in your way, preventing you from moving west")
        elif current_room.roomnum == 20:
            print ("there is an unimaginable barrier in your way, preventing you from moving north")
        else:
            current_room.roomnum -= 1
            current_room.roomname = terrain[current_room.roomnum ]
            print("you travel west, towards", current_room.roomname,"and reach it before night")

name = input("what is your name? >> ")
hero = Player(name)

# this is my list of commands
Commands = {
'help' :Player.help,
'heal' : Player.heal,
'inventory' : Player.inventory,
'stats' : Player.stats,
'explore' : Player.explore,
'run' :Player.run,
'fight' : Player.fight,
'north' : Player.north,
'east' : Player.east,
'south' : Player.south,
"west" : Player.west
}

print('(type help to get a list of commands) ')
print(hero.name, "enters a dark cave, searching for adventure. You will soon face the", monster.name)

while hero.health > 0 and monster.health > 0:
    line = input("What do you want to do? >> ")
    if line in Commands.keys():
        Commands[line] (hero,monster)
    else:
        print (hero.name, "does not understand this suggestion.")

credits()
