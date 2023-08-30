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
    def heal(self):
        self.health = self.health + 1

# This is the Player's class. Maybe I can let player choose different classes?
class Player (LivingThing):
    def __init__ (self,name):
        self.name = name
        self.health = 15
        self.status = "regular"

    def help(self,monster):
        print ('Your choices are:')
        for key in Commands.keys():
            print(key)
    def stats(self,monster):
        print("you are", self.name)
        print("with health of", self.health)
        print("your status is", self.status)
        print(monster.name , "health is", monster.health)
    def explore(self,monster):
        self.heal()
        print("your health is now", self.health)
        if randint(0,1) == 1:
            print(monster.name, "confronts you")
            print("what do you want to do?")
            self.status = "confronted"
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
                self.status = "normal"
            else:
                print("victory! You defeated the", monster.name)
        else:
            print("you are safe. There are no monsters near")

           
    def run(self,monster):
        if randint (0, self.health) < randint(0, monster.health):
            print("a monster has appeared")
            self.status = "confronted"
            self.fight (monster)
        else:
            self.tire()
            monster.heal()
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
'fight' : Player.fight
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