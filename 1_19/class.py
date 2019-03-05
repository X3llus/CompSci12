class character():
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma, race, role, alignment, background):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        self.race = race
        self.role = role
        self.alignment = alignment
        self.background = background

timmy = character(0, 15, 9000, -1, 1, -9000, "man-bear-pig", "water bottle", "chaotic good", "007")

def main():
    print (timmy.strength)

main()
