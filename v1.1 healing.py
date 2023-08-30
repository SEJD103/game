from random import randint, choice




# Super class for all living things

class LivingThing():
    def __init__ (self):
        self.name = "some name"
        self.health = 1
        self.inv_healpotion = 0
    def tire(self):
        self.health = self.health - 2
    def hurt(self):
        self.health = self.health - randint (0,self.health)
    def regen(self):
        self.health = self.health + 1


# This is the Player's class. Maybe I can let player choose different classes?
class Player (LivingThing):
    def __init__ (self,name):
        self.name = name
        self.health = 15
        self.status = "regular"
        self.inv_healpotion = 1
        self.gold = 0

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

# this will tell the player the commands they can use
    def help(self,monster):
        print ('Your choices are:')
        for key in Commands.keys():
            print(key)

# this will show player health, monster health and Player status
    def stats(self,monster):
        print("you are", self.name)
        print("with health of", self.health)
        print("your status is", self.status)
        print(monster.name , "health is", monster.health)

# this will let player regenerate, and find the monster
    def explore(self,monster):
        self.regen()
        print("your health is now", self.health)
        if randint (0,2) == 2:
            print("you found a healing potion")
            self.inv_healpotion += 1
        if randint(0,1) == 1:
            print(monster.name, "confronts you")
            print("what do you want to do?")
            self.status = "confronted"

# this function will let you hit the monster, and the monster hit you back
    def fight(self,monster):
        if self.status == "confronted":
            self.hurt()
            monster.hurt()
# here I added a gamerule that if player is facing a dragon, they will take extra damage
            if monster.name == "Dragon":
                print("your health is", self.health)
                self.health -= 2
                print ("the flames burn your flesh and you take some extra damage")
            else:
                print(monster.name, "attacks you")
            if self.health <= 0:
                print("you were killed by the", monster.name)
            elif monster.health > 0:
                print("your health is now", self.health)
                print("the", monster.name, "is still alive, keep going!")
                self.status = "confronted"
            else:
                print("victory! You defeated the", monster.name)
                self.status = "regular"
                self.gold += 1
        else:
            print("you are safe. There are no monsters near")


    def run(self,monster):
        if randint (0, self.health) < randint(0, monster.health):
            print("a monster has appeared")
            self.status = "confronted"
            self.fight (monster)
        else:
            self.tire()
            monster.regen()
            print ("your health suffered from you running")
            print ("your health is now", self.health)

# This is the monster class
class Monster (LivingThing):
    def __init__ (self,name,health):
        self.name = name
        self.health = health






name = input("what is your name? >> ")

hero = Player(name)






Commands = {
'help' :Player.help,
'stats' : Player.stats,
'explore' : Player.explore,
'run' :Player.run,
'fight' : Player.fight,
'heal' : Player.heal,
'inventory' : Player.inventory
}


goblin=Monster("Goblin",20)
dragon=Monster("Dragon",10)
monsters = []
monsters.append(goblin)
monsters.append(dragon)
monster = choice(monsters)




print('(type help to get a list of commands) ')
print(hero.name, "enters a dark cave, searching for adventure. You will soon face the", monster.name)




while hero.health > 0 and monster.health > 0:
    line = input("What do you want to do? >> ")
    if line in Commands.keys():
        Commands[line] (hero,monster)
    else:
        print (hero.name, "does not understand this suggestion.")






print("Game Over")