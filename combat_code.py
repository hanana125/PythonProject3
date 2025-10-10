#create combat code with magic option between human and octopus
import random

#Dictionary to keep player and octopus stats

'''gameDict = {
    "Octopus" : {
        "Name" : "Octopus",
        "HP" : 1000000000,
        "Damage" : 5000,
    },
    "Player" : {
        "Name" : userName,
        "HP" : 100,
        "Damage" : 50,
    }
}

#combat loop
def combatCode():
    for i in range(5, 0, -1):
        print(i)
    else:
        raise Exception("Your light fades out.")

class Characters:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def damageDone(self):
        for i in range(10):
            time.sleep(1)
            self.health -= random.randint(1, 6)
            print(f"warrior new health: {warrior.health}")

    def healDone(self):
        warrior.health += 30
        if warrior.health > 100:
            warrior.health = 100

warrior = Characters(100, 20, 30)'''

#Character class
class Character:
    def __init__(self, name, health, damage_range):
        self.name = name
        self.health = health
        self.damage_range = damage_range

    def is_alive(self):
        return self.health > 0

    def take_damage(self, dmg):
        self.health -= dmg
        if self.health < 0:
            self.health = 0

    def attack(self):
        return random.randint(*self.damage_range)

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

#Create player and octopus stats
player = Character("Warrior", 100, (10, 20))
octopus = Character("Giant Octopus", 120, (15, 25))

#Magic attack stats
magic_spells = {
    "fireball": (20, 35),
    "ice spike": (15, 30),
    "lightning": (10, 40)
}

def magic_attack():
    spell_choice = input("Choose a magic spell: ")
    for spell in magic_spells:
        print(f"- {spell.title()}")

    if spell_choice in magic_spells:
        return random.randint(*magic_spells[spell_choice])
    else:
        print("Invalid spell! You fumble and do no damage.")
        return 0

#Combat loop
def combat_loop():
    print("The battle begins...")

    while player.is_alive() and octopus.is_alive():
        print(f"\nYour HP: {player.health} | Octopus HP: {octopus.health}")
        choice = input("Choose your action: [attack, magic, heal] ")

        if choice == "attack":
            damage = player.attack()
            octopus.take_damage(damage)
            print(f"You slash the Octopus for {damage} damage!")
        elif choice == "magic":
            damage = magic_attack()
            octopus.take_damage(damage)
            print(f"You cast a spell dealing {damage} damage!")
        elif choice == "heal":
            player.heal(25)
            print("You heal yourself for 25 HP.")
        else:
            print("Invalid choice! You lose your turn.")

        # Octopus's turn
        if octopus.is_alive():
            octoDamage = octopus.attack()
            player.take_damage(octoDamage)
            print(f"The Octopus lashes out and deals {octoDamage} damage!")

    #End of the battle
    if player.is_alive():
        print("You defeated the Giant Octopus! ")
    else:
        print("Your light fades out..." )

#Run code
combat_loop()
