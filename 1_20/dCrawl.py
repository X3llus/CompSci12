from queue import Queue
class character():
    def __init__(self):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.statQueue = ["18", "17", "15", "12", "10", "8"]

        self.race = ""
        self.role = ""
        self.weapon = {
        "warrior":""
        }

    def create(self):
        for i in self.statQueue:
            while True:
                nStat = input("What stat will be value {}\nstrength, dexterity, constitution, intelligence, wisdom, charisma. >")
                if nStat == "strength" and self.strength == 0:
                    self.strength = i
                    print ("Strength is {}".format(self.strength))
                    break
                elif nStat == "dexterity" and self.dexterity == 0:
                    self.dexterity = i
                    print ("Dexterity is {}".format(self.dexterity))
                    break
                elif nStat == "constitution" and self.constitution == 0:
                    self.constitution = i
                    print ("Constitution is {}".format(self.constitution))
                    break
                elif nStat == "intelligence" and self.intelligence == 0:
                    self.intelligence = i
                    print ("Intelligence is {}".format(self.intelligence))
                    break
                elif nStat == "wisdom" and self.wisdom == 0:
                    self.wisdom = i
                    print ("Wisdom is {}".format(self.wisdom))
                    break
                elif nStat == "charisma" and self.charisma == 0:
                    self.charisma = i
                    print ("Charisma is {}".format(self.charisma))
                    break
                else:
                    print("Stat not available.")

        while True:
            self.race = input("Are you a human, elf, or dwarf >")
            if self.race == "human":
                self.intelligence += 1
                self.charisma += 2
                break
            elif self.race == "elf":
                self.dexterity += 2
                self.wisdom += 1
                break
            elif self.race == "dwarf":
                self.constitution += 2
                self.strength += 1
                break
            else:
                print ("Not an option")

        while True:
            self.role = input("Are you a warrior, mage, ranger, templar, thief, bard, monk")


def main():
    player = character()
    player.create()


main()
