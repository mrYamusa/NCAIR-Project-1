import random

from dice import Dice

d = Dice()


class Weapons:
    def __init__(self):
        pass

    def pickWeapon(self):
        weapons = ["Holy water", "Cross of calvary", "Mantle", "Anointing oil", "Communion bread", "Offering basket"]
        input(f"In the chapel you have several options of Holy weapons\nRoll a dice to pick a weapon.\n{weapons}"
              "(Press enter to roll the dice for random weapon)")
        your_weap = random.choice(weapons)
        print(f"You picked {your_weap}")

        return your_weap

    # yourWeapon = pickWeapon()
