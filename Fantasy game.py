# imports:
import random
from time import time
import math
import threading
import os
import readchar
from copy import deepcopy

SHOP_VARIABLES_DEFAULT = {
  "multiple_arrow_index": None,
  "multiple_arrow_amount": None, 
  "multiple_shuriken_index": None,
  "multiple_shuriken_amount": None,
  "weapon_options": None,
  "weapon_prices": None, 
  "armor_options": None,
  "armor_prices": None,
  "attachment_prices": None,
  "spell_prices": None,
  "spell_data": None,
  "already_taken_indices": None,
  "shop_refresh_needed": True
}

#Villages
Snecor = {
"Name": "Snecor",
"Bordering": ["The Wall", "Kibron"],
"shop_data": SHOP_VARIABLES_DEFAULT,
}
Aspel = {
"Name": "Aspel",
"Bordering": ["Otren"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Shaton = {
"Name": "Shaton",
"Bordering": ["Deshica", "Root"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Jaflen = {
"Name": "Jaflen",
"Bordering": ["Ethad", "Otren"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
TheFrostyMountains = {
"Name": "The Frosty Mountains",
"Bordering": ["Wolf Forest", "Oskesh"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
WolfForest = {
"Name": "Wolf Forest",
"Bordering": ["The Wall", "The Frosty Mountains"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
TheWall = {
"Name": "The Wall",
"Bordering": ["Wolf Forest", "Snecor"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Deshica = {
"Name": "Deshica",
"Bordering": ["Kibron", "Ethad", "Shaton"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
villages = [Snecor, Aspel, Shaton, Jaflen, TheFrostyMountains, WolfForest, TheWall, Deshica]
#Cities:
Otren = {
"Name": "Otren",
"Bordering": ["Aspel", "Jaflen", "Guclia"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Esmar = {
"Name": "Esmar",
"Bordering": ["Kibron"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Guclia = {
"Name": "Guclia",
"Bordering": ["Otren"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Ethad = {
"Name": "Ethad",
"Bordering": ["Kibron", "Jaflen"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Kibron = {
"Name": "Kibron",
"Bordering": ["Esmar", "Snecor", "Ethad", "Deshica"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Root = {
"Name": "Root",
"Bordering": ["Branch", "Shaton"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Leaf = {
"Name": "Leaf",
"Bordering": ["Branch"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Branch = {
"Name": "Branch",
"Bordering": ["Root", "Leaf"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Ogron = {
"Name": "Ogron",
"Bordering": ["Oskesh"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
Oskesh = {
"Name": "Oskesh",
"Bordering": ["Ogron", "The Frosty Mountains"],
"shop_data": SHOP_VARIABLES_DEFAULT
}
cities = [Otren, Esmar, Guclia, Ethad, Kibron, Root, Leaf, Branch, Ogron, Oskesh]
# realms:
Adrea = {
"Race": "Elves",
"Cities": [Branch, Root],
"Villages": [Leaf]
}
Ucror = {
"Race": "Dwarves",
"Cities": [Guclia, Otren],
"Villages": [Aspel, Jaflen]
}
Errevar = {
"Race": "Humans",
"Cities": [Esmar, Kibron, Ethad],
"Villages": [Shaton, Snecor, Deshica, TheWall]
}
TheJungle = {
"Race": "Orcs",
"Cities": [Ogron, Oskesh],
"Villages": [WolfForest, TheFrostyMountains]
}

# Armors:
BasicClothes = {
"Name": "BasicClothes",
"WeaponSlots": ["BootLeft", "BootRight", "AxeFrogLeft"],
"Slowness": 0,
"Protection": 0,
"Magic": 1,
"Plural": True
}
KnightArmor = {
"Name": "KnightArmor",
"WeaponSlots": ["ScabbardSlotLeft", "ShieldSlotBack"],
"Slowness": 5,
"Protection": 10,
"Magic": 1,
"Price": 150,
"Plural": False
}
BarbarianRags = {
"Name": "BarbarianRags",
"WeaponSlots": ["ScabbardSlotLeft", "ScabbardSlotRight", "BootLeft", "BootRight", "AxeFrogLeft", "AxeFrogRight", "AxeLoopBack"],
"Slowness": 1,
"Protection": 2,
"Magic": 2,
"Price": 75,
"Plural": True
}
NinjaGi = {
"Name": "NinjaGi",
"WeaponSlots": ["ScabbardSlotBackLeft", "ScabbardSlotBackRight", "BootLeft", "BootRight", "ShurikenSlotLeft", "ShurikenSlotRight"],
"Slowness": -2,
"Protection": 1,
"Magic": 2,
"Price": 200,
"Plural": False
}
MageArmor = {
"Name": "MageArmor",
"WeaponSlots": ["PotionSlotRight", "PotionSlotLeft", "StaffSlotBack"],
"Slowness": 4,
"Protection": 8,
"Magic": 5,
"Price": 200,
"Plural": False
}
WizardRobes = {
"Name": "WizardRobes",
"WeaponSlots": ["PotionSlotRight", "PotionSlotLeft", "StaffSlotBack"],
"Slowness": 2,
"Protection": 1,
"Magic": 6,
"Price": 65,
"Plural": True
}
BattleMageArmor = {
"Name": "BattleMageArmor",
"WeaponSlots": ["ScabbardSlotLeft", "PotionSlotRight", "BowSlotBack", "QuiverSlotBack", "ShieldSlotBack", "BootLeft", "BootRight"],
"Slowness": 4,
"Protection": 9,
"Magic": 4,
"Price": 150,
"Plural": False
}
ArcherCoat = {
"Name": "ArcherCoat",
"WeaponSlots": ["BootLeft", "BootRight", "BowSlotBack", "QuiverSlotBack"],
"Slowness": 0,
"Protection": 1,
"Magic": 1,
"Price": 50,
"Plural": False
}
Chainmail = {
"Name": "Chainmail",
"WeaponSlots": ["ScabbardSlotLeft", "ShieldSlotBack"],
"Slowness": 2,
"Protection": 5,
"Magic": 1,
"Price": 100,
"Plural": False
}
PlateArmor = {
"Name": "PlateArmor",
"WeaponSlots": ["ScabbardSlotLeft", "ShieldSlotBack"],
"Slowness": 6,
"Protection": 12,
"Magic": 1,
"Price": 250,
"Plural": False
}
Gambeson = {
"Name": "Gambeson",
"WeaponSlots": ["ScabbardSlotLeft", "ShieldSlotBack"],
"Slowness": 2,
"Protection": 2,
"Magic": 1,
"Price": 75,
"Plural": False
}
ShadowSteelArmor = {
"Name": "ShadowSteelArmor",
"WeaponSlots": ["ScabbardSlotLeft", "ScabbardSlotRight", "BowSlotBack", "QuiverSlotBack"],
"Slowness": 1,
"Protection": 7,
"Magic": 4,
"Price": None,
"Plural": False
}
RuggedHideArmor = {
"Name": "RuggedHideArmor",
"WeaponSlots": ["BootLeft", "BootRight"],
"Slowness": 1,
"Protection": 2,
"Magic": 1,
"Price": None,
"Plural": False
}
#Items:
Gold = 5000 # 100, currently changed for debug purposes
Items = {
"MainHand": {"Item": [], "Amount": 0},
"SecondHand": {"Item": [], "Amount": 0},
"BootLeft": {"Item": None, "Amount": 0},
"BootRight": {"Item": None, "Amount": 0},
"ScabbardSlotLeft": {"Item": None, "Amount": 0},
"ScabbardSlotRight": {"Item": None, "Amount": 0},
"ScabbardSlotBackLeft": {"Item": None, "Amount": 0},
"ScabbardSlotBackRight": {"Item": None, "Amount": 0},
"BowSlotBack": {"Item": None, "Amount": 0},
"QuiverSlotBack": {"Item": None, "Amount": 0},
"ShieldSlotBack": {"Item": None, "Amount": 0},
"ShurikenSlotLeft": {"Item": None, "Amount": 0},
"ShurikenSlotRight": {"Item": None, "Amount": 0},
"AxeLoopBack": {"Item": None, "Amount": 0},
"PotionSlotLeft": {"Item": None, "Amount": 0},
"PotionSlotRight": {"Item": None, "Amount": 0},
"StaffSlotBack": {"Item": None, "Amount": 0},
"Staff": {"Spells": None, "Amount": 0},
"AxeFrogRight": {"Item": None, "Amount": 0},
"AxeFrogLeft": {"Item": None, "Amount": 0},
"Armor": BasicClothes.copy()
}

# uncomment if you want to start off as a wizard
#Items = {'MainHand': {'Item': [], 'Amount': 0}, 'SecondHand': {'Item': [], 'Amount': 0}, 'BootLeft': {'Item': None, 'Amount': 0}, 'BootRight': {'Item': None, 'Amount': 0}, 'ScabbardSlotLeft': {'Item': None, 'Amount': 0}, 'ScabbardSlotRight': {'Item': None, 'Amount': 0}, 'ScabbardSlotBackLeft': {'Item': None, 'Amount': 0}, 'ScabbardSlotBackRight': {'Item': None, 'Amount': 0}, 'BowSlotBack': {'Item': None, 'Amount': 0}, 'QuiverSlotBack': {'Item': None, 'Amount': 0}, 'ShieldSlotBack': {'Item': None, 'Amount': 0}, 'ShurikenSlotLeft': {'Item': None, 'Amount': 0}, 'ShurikenSlotRight': {'Item': None, 'Amount': 0}, 'AxeLoopBack': {'Item': None, 'Amount': 0}, 'PotionSlotLeft': {'Item': None, 'Amount': 0}, 'PotionSlotRight': {'Item': {'Name': 'Health Potion', 'Projectile': False, 'Stacking': 3, 'DamagePerInstance': -5, 'Slots': ['PotionSlotRight', 'PotionSlotLeft'], 'Speed': 1, 'TimeLeft': 1, 'Price': 125, 'Packet': False, 'Potion': True}, 'Amount': 2}, 'StaffSlotBack': {'Item': {'Name': 'Staff', 'Damage': 1, 'Slots': ['StaffSlotBack'], 'Speed': 1, 'Weapon': True, 'Projectile': False, 'Stacking': 1, 'Price': 150, 'Packet': False, 'Potion': False}, 'Amount': 1}, 'Staff': [{'Type': {'Name': 'Fireball', 'Damage': 1, 'Slots': ['Staff'], 'Speed': 2, 'Weapon': False, 'Projectile': True, 'Requires': [{'Name': 'Staff', 'Damage': 1, 'Slots': ['StaffSlotBack'], 'Speed': 1, 'Weapon': True, 'Projectile': False, 'Stacking': 1, 'Price': 150, 'Packet': False, 'Potion': False}], 'Stacking': 36, 'Price': 100, 'Packet': False, 'Potion': False}, 'Amount': 0}, {'Type': {'Name': 'Lightning bolt', 'Damage': 2, 'Slots': ['Staff'], 'Speed': 1, 'Weapon': False, 'Projectile': True, 'Requires': [{'Name': 'Staff', 'Damage': 1, 'Slots': ['StaffSlotBack'], 'Speed': 1, 'Weapon': True, 'Projectile': False, 'Stacking': 1, 'Price': 150, 'Packet': False, 'Potion': False}], 'Stacking': 3, 'Price': 150, 'Packet': False, 'Potion': False}, 'Amount': 0}], 'AxeFrogRight': {'Item': None, 'Amount': 0}, 'AxeFrogLeft': {'Item': None, 'Amount': 0}, 'Armor': {'Name': 'WizardRobes', 'WeaponSlots': ['PotionSlotRight', 'PotionSlotLeft', 'StaffSlotBack'], 'Slowness': 2, 'Protection': 1, 'Magic': 6, 'Price': 65, 'Plural': True}} # debug, remove when finished

Health = 25
Location = Deshica
realm = Errevar
#Weapons:
Dagger = {
"Name": "Dagger",
"Damage": 3,
"Slots": ["BootLeft", "BootRight"],
"Speed": 3,
"Weapon": True,
"Projectile": True,
"Requires": [],
"Stacking": 1,
"Price": 100,
"Packet": False,
"Potion": False
}
KnightSword = {
"Name": "KnightSword",
"Damage": 5,
"Slots": ["ScabbardSlotLeft"],
"Speed": 2,
"Weapon": True,
"Projectile": False,
"Stacking": 1,
"Price": 100,
"Packet": False,
"Potion": False
}
Shortsword = {
"Name": "Shortsword",
"Damage": 4,
"Slots": ["ScabbardSlotLeft", "ScabbardSlotRight"],
"Speed": 3,
"Weapon": True,
"Projectile": False,
"Stacking": 1,
"Price": 150,
"Packet": False,
"Potion": False
}
Ninjato = {
"Name": "Ninjato",
"Damage": 4,
"Slots": ["ScabbardSlotBackLeft", "ScabbardSlotBackRight", "ScabbardSlotLeft", "ScabbardSlotRight"],
"Speed": 4,
"Weapon": True,
"Projectile": False,
"Stacking": 1,
"Price": 150,
"Packet": False,
"Potion": False
}
Bow = {
"Name": "Bow",
"Damage": 1,
"Slots": ["BowSlotBack"],
"Speed": 1,
"Weapon": True,
"Projectile": False,
"Stacking": 1,
"Price": 125,
"Packet": False,
"Potion": False
}
Arrow = {
"Name": "Arrow",
"Damage": 2,
"Slots": ["QuiverSlotBack"],
"Speed": 1,
"Weapon": False,
"Projectile": True,
"Requires": [Bow],
"Stacking": 24,
"Price": 3,
"Packet": False,
"Potion": False
}
Shuriken = {
"Name": "Shuriken",
"Damage": 2,
"Slots": ["ShurikenSlotLeft", "ShurikenSlotRight"],
"Speed": 3,
"Weapon": False,
"Projectile": True,
"Requires": [],
"Stacking": 3,
"Price": 100,
"Packet": False,
"Potion": False
}
BattleAxe = {
"Name": "BattleAxe",
"Damage": 10,
"Slots": ["AxeLoopBack"],
"Speed": 1,
"Weapon": True,
"Projectile": False,
"Stacking": 1,
"Price": 200,
"Packet": False,
"Potion": False
}
Hatchet = {
"Name": "Hatchet",
"Damage": 3,
"Slots": ["AxeFrogRight", "AxeFrogLeft"],
"Speed": 1,
"Weapon": True,
"Projectile": True,
"Requires": [],
"Stacking": 1,
"Price": 100,
"Packet": False,
"Potion": False
}
SpikedClub = {
"Name": "SpikedClub",
"Damage": 9,
"Slots": ["AxeLoopBack"],
"Speed": 1,
"Weapon": True,
"Projectile": False,
"Stacking": 1,
"Price": 125,
"Packet": False,
"Potion": False
}
Staff = {
"Name": "Staff",
"Damage": 1,
"Slots": ["StaffSlotBack"],
"Speed": 1,
"Weapon": True,
"Projectile": False,
"Stacking": 1,
"Price": 150,
"Packet": False,
"Potion": False
}
Fireball = {
"Name": "Fireball",
"Damage": 1, # the number is multiplied by Items["Armor"]["Magic"]
"Slots": ["Staff"],
"Speed": 2,
"Weapon": False,
"Projectile": True,
"Requires": [Staff],
"Stacking": 36,
"Price": 100,
"Packet": False,
"Potion": False
}
Lightningbolt = {
"Name": "Lightning bolt",
"Damage": 2, # the number is multiplied by Items["Armor"]["Magic"]
"Slots": ["Staff"],
"Speed": 1,
"Weapon": False,
"Projectile": True,
"Requires": [Staff],
"Stacking": 3,
"Price": 150,
"Packet": False,
"Potion": False
}
# Potions:
HealthPotion = {
"Name": "Health Potion",
"Projectile": False,
"Stacking": 3,
"DamagePerInstance": -5,
"Slots": ["PotionSlotRight", "PotionSlotLeft"],
"Speed": 1,
"TimeLeft": 1,
"Price": 125,
"Packet": False,
"Potion": True
}
DamagePotion = {
"Name": "Damage Potion",
"Projectile": True,
"Requires": [],
"Stacking": 3,
"DamagePerInstance": 1, # 5*round(Items["Armor"]["Magic"]/2)
"Slots": ["PotionSlotRight", "PotionSlotLeft"],
"Speed": 1,
"TimeLeft": 1,
"Price": 125,
"Packet": False,
"Potion": True
}
PoisonPotion = {
"Name": "Poison Potion",
"Projectile": True,
"Stacking": 3,
"Requires": [],
"DamagePerInstance": 1,
"Slots": ["PotionSlotRight", "PotionSlotLeft"],
"Speed": 1,
"TimeLeft": 7,
"Price": 150,
"Packet": False,
"Potion": True
}
RegenerationPotion = {
"Name": "Regeneration Potion",
"Projectile": False,
"Stacking": 3,
"DamagePerInstance": 1, # -1*round(Items["Armor"]["Magic"]/2)
"Slots": ["PotionSlotRight", "PotionSlotLeft"],
"Speed": 1,
"TimeLeft": 7,
"Price": 150,
"Packet": False,
"Potion": True
}
# Attachments
Scabbard = {
"Name": "Scabbard",
"Unlocks": ["ScabbardSlotLeft", "ScabbardSlotRight"],
"Price": 30
}
ScabbardBack = {
"Name": "Back Scabbard",
"Unlocks": ["ScabbardSlotBackLeft", "ScabbardSlotBackRight"],
"Price": 35
}
Quiver = {
"Name": "Quiver",
"Unlocks": ["QuiverSlotBack"],
"Price": 40
}
AxeLoop = {
"Name": "AxeLoop",
"Unlocks": ["AxeLoopBack"],
"Price": 21
}
AxeFrog = {
"Name": "AxeFrog",
"Unlocks": ["AxeFrogLeft", "AxeFrogRight"],
"Price": 45
}
# these decide where you can buy stuff
VILLAGE_WEAPONS = [Dagger, Bow, Arrow, Hatchet, KnightSword, PoisonPotion]
VILLAGE_ARMORS = [ArcherCoat, BarbarianRags, KnightArmor, Chainmail]
CITY_WEAPONS = [Ninjato, Bow, Arrow, Shuriken, BattleAxe, Staff, Shortsword, KnightSword, HealthPotion, DamagePotion, PoisonPotion, RegenerationPotion]
CITY_ARMORS = [NinjaGi, MageArmor, WizardRobes, BattleMageArmor, KnightArmor, PlateArmor]
# defines which ones are attachments
attachments = [Scabbard, ScabbardBack, Quiver, AxeLoop, AxeFrog] # the items in the list are not altered, but the list is shuffled, so it's technically not a constant
# keeps track of what spells the player can infuse their staff with
learned_spells = []
SPELLS = [Fireball, Lightningbolt]
# The things that only need the armor to attach
AUTO_ATTACHMENTS = ["BootLeft", "BootRight", "StaffSlotBack", "ShurikenSlotLeft", "ShurikenSlotRight", "BowSlotBack", "PotionSlotRight", "PotionSlotLeft"]
# functions
def multiple(item, possible, minimum, maximum):
    if possible[0][0] == item:
        which = 0
    elif possible[0][1] == item:
        which = 1
    else:
        which = 2
    ending = ""
    if which < 2: 
        amount = random.randint(minimum, maximum) # this segment can also be used for potensially other stuff like fireballs and possibly shurikens if i decide to.
        Type = item
        if amount != 1:
            ending = "s"
        possible[0][which] = {"Name": ""+str(amount)+" "+Type["Name"]+ending+"", "Type": Type, "Price": Type["Price"]*amount, "Packet": True}
    else:
        amount = 1
    return which, amount, possible
def negative_check(number):
    if number < 1:
        number = random.randint(3, 5)
    return number
def n(string):
    if string[0].lower() in "aeiouy":
        start = "an"
    else:
        start = "a"
    return start
def available(theList, number, length):
    if str(number) in theList:
        print("-"*length+"", end="")
        if number % 2 == 0:
            print("")
        return False
    return True
# The shop function
def shop(IN_A_CITY, Gold, Items, JUST_ARRIVED, shop_data):
    arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken = shop_data["multiple_arrow_index"], shop_data["multiple_arrow_amount"], shop_data["multiple_shuriken_index"], shop_data["multiple_shuriken_amount"], shop_data["weapon_options"], shop_data["weapon_prices"], shop_data["armor_options"], shop_data["armor_prices"], shop_data["attachment_prices"], shop_data["already_taken_indices"]
    if JUST_ARRIVED:
        if IN_A_CITY:
            possible = [CITY_WEAPONS.copy(), CITY_ARMORS.copy()]
            random.shuffle(possible[0])
            random.shuffle(possible[1])
        else:
            possible = [VILLAGE_WEAPONS.copy(), VILLAGE_ARMORS.copy()]
            random.shuffle(possible[0])
            random.shuffle(possible[1])
        arrowWhich, arrowAmount, possible = multiple(Arrow, possible, 3, 24)
        shurikenWhich, shurikenAmount, possible = multiple(Shuriken, possible, 3, 3)
        random.shuffle(attachments) # and then it randomizes the attachments outside, because villages and cities have the same attachments
        sold_weapons = [possible[0][0], possible[0][1]]
        weapon_prices = [negative_check(sold_weapons[0]["Price"]-random.randint(-20, 20)), negative_check(sold_weapons[1]["Price"]-random.randint(-20, 20))]
        sold_armors = [possible[1][0], possible[1][1]]
        armor_prices = [sold_armors[0]["Price"]-random.randint(-20, 20), sold_armors[1]["Price"]-random.randint(-20, 20)]
        attachment_prices = [attachments[0]["Price"]-random.randint(-20, 20), attachments[1]["Price"]-random.randint(-20, 20)]
        already_taken = []
    print("The current items sold are:") # shows the shop menu
    print("Weapons:") # displays the weapons
    if available(already_taken, 1, len(sold_weapons[0]["Name"])+len(str(weapon_prices[0]))+13):
        print(sold_weapons[0]["Name"]+" for "+str(weapon_prices[0])+" gold(1)", end="")
    print(" and ", end="")
    if available(already_taken, 2, len(sold_weapons[1]["Name"])+len(str(weapon_prices[1]))+14):
        print(""+sold_weapons[1]["Name"]+" for "+str(weapon_prices[1])+" gold(2).")
    print("Armors:") # displays the armors
    if available(already_taken, 3, len(sold_armors[0]["Name"])+len(str(armor_prices[0]))+13):
        print(sold_armors[0]["Name"]+" for "+str(armor_prices[0])+" gold(3)", end="")
    print(" and ", end="")
    if available(already_taken, 4, len(sold_armors[1]["Name"])+len(str(armor_prices[1]))+14):
        print(""+sold_armors[1]["Name"]+" for "+str(armor_prices[1])+" gold(4).")
    print("Attachments:") # displays the attachments
    if available(already_taken, 5, len(attachments[0]["Name"])+len(str(attachment_prices[0]))+13):
        print(attachments[0]["Name"]+" for "+str(attachment_prices[0])+" gold(5)", end="")
    print(" and ", end="")
    if available(already_taken, 6, len(attachments[1]["Name"])+len(str(attachment_prices[1]))+14):
        print(""+attachments[1]["Name"]+" for "+str(attachment_prices[1])+" gold(6).")
    print("You may also exit the shop (7)") # displays the exit the shop option
    done = False
    while not done:
        willWork = False
        willWork2 = False
        beenHere = False
        while True:
            purchase = "None"
            first = True
            while len(purchase) != 1 or not purchase in "1234567" or purchase in already_taken: # gets input and makes sure it is correct
                if not first:
                    print("What you wrote was not accepted. Try something else.")
                purchase = input()
                first = False
            number = purchase
            some = False
            if purchase == "1" or purchase == "2":
                price = weapon_prices[int(purchase)-1] # buying weapons and checking if they're too expensive
                if price > Gold:
                    print("Sorry! Too exspensive!")
                else:
                    if sold_weapons[int(purchase)-1]["Packet"]:
                        sold_weapons[int(purchase)-1] = sold_weapons[int(purchase)-1]["Type"]
                        some = True
                    for i in range(len(sold_weapons[int(purchase)-1]["Slots"])):
                        if sold_weapons[int(purchase)-1]["Slots"][i] in AUTO_ATTACHMENTS and sold_weapons[int(purchase)-1]["Slots"][i] in Items["Armor"]["WeaponSlots"] and Items[sold_weapons[int(purchase)-1]["Slots"][i]]["Item"] == None:
                           Items[sold_weapons[int(purchase)-1]["Slots"][i]]["Item"] = [] 
                        if Items[sold_weapons[int(purchase)-1]["Slots"][i]]["Item"] == None:
                            beenHere = True
                        elif Items[sold_weapons[int(purchase)-1]["Slots"][i]]["Item"] == []:
                            willWork = True
                            break
                        elif Items[sold_weapons[int(purchase)-1]["Slots"][i]]["Amount"] < Items[sold_weapons[int(purchase)-1]["Slots"][i]]["Item"]["Stacking"] and Items[sold_weapons[int(purchase)-1]["Slots"][i]]["Item"] == sold_weapons[int(purchase)-1]:
                            willWork = True
                            break
                    if not willWork:
                        if beenHere:
                            print("You don't have the propper attachment for that!")
                        else:
                            print("You don't have enough space for that!")
                    else:
                        purchase = sold_weapons[int(purchase)-1]
                        break
            elif purchase == "3" or purchase == "4":
                price = armor_prices[int(purchase)-3] # buying armors and checking if they're too expensive
                if price > Gold:
                    print("Sorry! Too exspensive!")
                else:
                    purchase = sold_armors[int(purchase)-3]
                    if purchase["Plural"]:
                        some = True
                    break
            elif purchase == "5" or purchase == "6":
                price = attachment_prices[int(purchase)-5]# buying attachments and checking if they're too expensive
                if price > Gold:
                    print("Sorry! Too exspensive!")
                else:
                    beenHere2 = False
                    for i in range(len(attachments[int(purchase)-5]["Unlocks"])):
                        if Items[attachments[int(purchase)-5]["Unlocks"][i]]["Item"] == None:
                            beenHere2 = True
                            if attachments[int(purchase)-5]["Unlocks"][i] in Items["Armor"]["WeaponSlots"]:                        
                                willWork2 = True
                                break
                        if willWork2:
                            break
                    if not willWork2:
                        if not beenHere2 and attachments[int(purchase)-5] == Quiver or attachments[int(purchase)-5] == AxeLoop or ("ScabbardSlotLeft" in Items["Armor"]["WeaponSlots"] and "ScabbardSlotRight" not in Items["Armor"]["WeaponSlots"]) or ("AxeFrogLeft" in Items["Armor"]["WeaponSlots"] and "AxeFrogRight" not in Items["Armor"]["WeaponSlots"]):
                            print("You've already unlocked that slot")
                        elif beenHere2:
                            print("Your armor can't support that attachment!")
                        else:
                            print("You've already unlocked those slots")
                    else:
                        purchase = attachments[int(purchase)-5]
                        break
            else:
                shop_data = { # TODO: oh no, it's here as well. Stop all the dictionary to variable and back again nonsense. 
                  "multiple_arrow_index": arrowWhich,
                  "multiple_arrow_amount": arrowAmount, 
                  "multiple_shuriken_index": shurikenWhich,
                  "multiple_shuriken_amount": shurikenAmount,
                  "weapon_options": sold_weapons,
                  "weapon_prices": weapon_prices, 
                  "armor_options": sold_armors,
                  "armor_prices": armor_prices,
                  "attachment_prices": attachment_prices,
                  "spell_prices": shop_data["spell_prices"],
                  "spell_data": shop_data["spell_prices"],
                  "already_taken_indices": already_taken,
                  "shop_refresh_needed": False
                }
                return Gold, Items, shop_data # otherwise, it exits the shop function as a whole
            number = purchase
        already_taken.append(number)
        if not some:
            starting = n(purchase["Name"])
            ending = ""
        else:
            starting = "some"
            ending = "s"
        print("You bought "+starting+" "+purchase["Name"]+ending+" for "+str(price)+" gold.") # notifies you of your purchase
        Gold -= price
        print("You now have "+str(Gold)+" gold left")
        if purchase in attachments: # checks if the purchase is an attachment
            Items[purchase["Unlocks"][i]]["Item"] = [] # we can use "i" because it jumped straight from finding out if it was possible to here, so now we do it since it's possible.
        elif purchase in sold_weapons: # checks if the purchase is a weapon
            Items[purchase["Slots"][i]]["Item"] = purchase # same principle as earlier, so we can use "i"
            if purchase == Arrow:
                Items[purchase["Slots"][i]]["Amount"] += arrowAmount
                if Items[purchase["Slots"][i]]["Amount"] > purchase["Stacking"]:
                    Items[purchase["Slots"][i]]["Amount"] = purchase["Stacking"]
            elif purchase == Shuriken:
                Items[purchase["Slots"][i]]["Amount"] += shurikenAmount
                if Items[purchase["Slots"][i]]["Amount"] > purchase["Stacking"]:
                    Items[purchase["Slots"][i]]["Amount"] = purchase["Stacking"]
            elif purchase["Potion"]:
                Items[purchase["Slots"][i]]["Amount"] += 1
                if Items[purchase["Slots"][i]]["Amount"] > purchase["Stacking"]:
                    Items[purchase["Slots"][i]]["Amount"] = purchase["Stacking"]
            else:
                Items[purchase["Slots"][i]]["Amount"] = 1
                if purchase == Staff:
                    Items["Staff"]["Spells"] = [{'Type': {'Name': 'Fireball', 'Damage': 1, 'Slots': ['Staff'], 'Speed': 2, 'Weapon': False, 'Projectile': True, 'Requires': [{'Name': 'Staff', 'Damage': 1, 'Slots': ['StaffSlotBack'], 'Speed': 1, 'Weapon': True, 'Projectile': False, 'Stacking': 1, 'Price': 150, 'Packet': False, 'Potion': False}], 'Stacking': 36, 'Price': 100, 'Packet': False, 'Potion': False}, 'Amount': 0}, {'Type': {'Name': 'Lightning bolt', 'Damage': 2, 'Slots': ['Staff'], 'Speed': 1, 'Weapon': False, 'Projectile': True, 'Requires': [{'Name': 'Staff', 'Damage': 1, 'Slots': ['StaffSlotBack'], 'Speed': 1, 'Weapon': True, 'Projectile': False, 'Stacking': 1, 'Price': 150, 'Packet': False, 'Potion': False}], 'Stacking': 3, 'Price': 150, 'Packet': False, 'Potion': False}, 'Amount': 0}]
        else: # checks if the purchase is armor 
            Items["Armor"] = purchase
            for item_name in Items:
                if not item_name in ["Armor", "MainHand", "SecondHand", "Staff"]:
                    if not item_name in Items["Armor"]["WeaponSlots"]:
                        Items[item_name]["Item"] = None
                        Items[item_name]["Amount"] = 0
                elif item_name == "Staff":
                    if Items["StaffSlotBack"]["Amount"] == 0:
                        Items["Staff"]["Spells"] = None
        more = "None"
        while more.lower() != "no" and more.lower() != "yes":
            print("Anything else? (write \"no\" to exit the shop, or write \"yes\" to make another purchase)")
            more = input()
        if more.lower() == "no":
            done = True
        else:
            done = False
            print("And that is ...?")
    shop_data = { # TODO: fix this. This is bad programming, there shouldn't be all these variables when we already have a dictionary. In addition, the keys should only be defined once, in the beginning of the program. 
      "multiple_arrow_index": arrowWhich,
      "multiple_arrow_amount": arrowAmount, 
      "multiple_shuriken_index": shurikenWhich,
      "multiple_shuriken_amount": shurikenAmount,
      "weapon_options": sold_weapons,
      "weapon_prices": weapon_prices, 
      "armor_options": sold_armors,
      "armor_prices": armor_prices,
      "attachment_prices": attachment_prices,
      "spell_prices": shop_data["spell_prices"],
      "spell_data": shop_data["spell_data"],
      "already_taken_indices": already_taken,
      "shop_refresh_needed": False
    }
    return Gold, Items, shop_data
def options(Gold, Items, learned_spells):
    villageSwaps, citySwaps = 0, 0
    if (time()-START_TIME) // 180 > citySwaps:
        citySwaps = (time()-START_TIME) // 180
        for city in cities:
            city["shop_data"]["shop_refresh_needed"] = True
            city["shop_data"]["armor_prices"] = [None, None] # this part doesn't need to be done on the village side since villages don't have academies.
    if (time()-START_TIME) // 300 > villageSwaps:
        villageSwaps = (time()-START_TIME) // 300
        for village in villages:
            village["shop_data"]["shop_refresh_needed"] = True
    action = None
    generate = location["shop_data"]["shop_refresh_needed"]
    
    while action != "1":
        action = None
        while action != "1" and action != "2" and action != "3" and (action != "4" or location in villages):
            if location in villages:
                print("You can: leave for another settlement(1), shop for items(2), or fight monsters on the egde of the village (3)")
            else:
                print("You can: leave for another settlement(1), shop for items(2), fight monsters on the egde of the city (3) or learn magic at the academy (4)")
            action = input()
        if action == "1":
            print("Where do you want to go?")
            for i in range(len(location["Bordering"])):
                print(str(i+1)+": "+location["Bordering"][i])
            print(str(i+2)+": stay here")
            destination = "None"
            while True:
                if destination in "123456789" and len(destination) == 1:
                    if int(destination) < i+3:
                        break
                destination = input()
            if destination != str(i+2):
                destination = location["Bordering"][int(destination)-1]
                print("Heading to "+destination)
            else:
                print("Ok then ...")
                action = None
        elif action == "2":
            Gold, Items, location["shop_data"] = shop(location not in villages, Gold, Items, generate, location["shop_data"])
            generate = False
        elif action == "3":
            combat() # TODO: working here, continue
        elif action == "4":
            print(location["shop_data"]) # debug
            Gold, Items, location["shop_data"]["spell_prices"], location["shop_data"]["spell_data"], learned_spells = academy(Gold, Items, location["shop_data"]["spell_prices"], location["shop_data"]["spell_data"], learned_spells) # debug
        else:
            print("Please enter a valid number")
    return Gold, Items, destination, learned_spells
def settlement(NAME):
    for city in cities:
        if city["Name"] == NAME:
            return city
    for village in villages:
        if village["Name"] == NAME:
            return village
def academy(Gold, Items, spell_prices, spell_data, learned_spells):
    """
    This function allows the player to acquire new spells by infusing them into their staff using gold.
    :param Gold: int - The player's current amount of gold.
    :param Items: list - The player's current inventory of items.
    :param spell_prices: dict - A dictionary mapping spell names to their prices.
    :param spell_data: dict - A dictionary mapping spell names to their respective dictionaries. 
    :param learned_spells: list - List of spells the player has already learned.
    :return: tuple - Updated values of Gold, Items, spell_prices, spell_data, and learned_spells.
    """

    organize(Items) # debug

    if Items["Staff"]["Spells"] is None:
        print("You need a staff to learn spells!")
        return Gold, Items, spell_prices, spell_data, learned_spells

    if spell_prices is None:
        spell_prices = {
            Fireball["Name"]: Fireball["Price"] + random.randint(-10, 10),
            Lightningbolt["Name"]: Lightningbolt["Price"] + random.randint(-10, 10)
        }

    if spell_data is None:
        spell_data = {Fireball["Name"]: Fireball, Lightningbolt["Name"]: Lightningbolt}

    # Learning spells
    print("Welcome to the academy! You can learn new spells and infuse them into your staff.")
    academyChoice = "None"
    while academyChoice != "3":
        academyChoice = "None"
        done = False
        while academyChoice not in ["1", "2", "3"]:
            print("You find yourself in the main hall of the academy. Before you are two doors, labeled with what's inside their rooms, and behind you is the way out.")
            print("Do you wish to learn spells (1), infuse spells that you've already learned (2) or exit the academy (3)?") 
            academyChoice = input()

        if academyChoice == "1":
            print("The following spells are available for learning:")

            while not done:
                available_spells = []
                for spell, data in spell_data.items():
                    if data not in learned_spells:
                        available_spells.append(spell)
                if not available_spells:
                    print("You have already learned all the available spells, so you return to the main hall.")
                    break

                count = 0
                for spell in available_spells:
                    count += 1
                    print(f"{spell}: 50 gold ({count})")
                print("Whenever you wish to get back to the main hall, type \"e\".")

                spell_choice_index = "None"
                while True:
                    if intConvertable(spell_choice_index):
                        if len(available_spells) >= int(spell_choice_index):
                            break
                    spell_choice_index = input("Which spell would you like to learn? ")
                    if spell_choice_index.lower() == "e":
                        done = True
                        break
                if not done:
                    SPELL_CHOICE_NAME = available_spells[int(spell_choice_index) - 1]
                    if int(spell_choice_index) - 1 in range(len(available_spells)) and Gold >= 50:

                        Gold -= 50
                        learned_spells.append(spell_data[SPELL_CHOICE_NAME])
                        
                        for spell in Items["Staff"]["Spells"]:
                            if spell["Type"]["Name"] == SPELL_CHOICE_NAME:
                                previous = spell["Amount"]
                                spell["Amount"] += min(Items['Armor']['Magic'], spell["Type"]["Stacking"] - spell["Amount"])
                        
                        print(f"Successfully learned {SPELL_CHOICE_NAME} for 50 gold. Your staff has been infused with {min(Items['Armor']['Magic'], spell['Type']['Stacking'] - previous)} {SPELL_CHOICE_NAME}{'s' if min(Items['Armor']['Magic'], spell['Type']['Stacking'] - previous) != 1 else ''}. You now have {Gold} gold remaining.")

                    elif Gold < 50:
                        print("You don't have enough gold to learn that spell.")
                    else:
                        print("Invalid spell choice.")
        elif academyChoice == "2":
            while not done:
                count = 0

                for spell, price in spell_prices.items():
                    count += 1
                    print(f"{spell}: {price} gold ({count})")
                print("Whenever you want to return to the main hall, type \"e\".")

                spellChoice = "Invalid"
                while True:
                    if intConvertable(spellChoice):
                        if len(spell_prices.keys()) >= int(spellChoice):
                            break
                    spellChoice = input("Which spell would you like to infuse into your staff? ")
                    if spellChoice.lower() in ["e"]:
                        done = True
                        break

                if not done:
                    spellChoiceName = list(spell_prices.keys())[int(spellChoice) - 1]
                    if int(spellChoice) - 1 in range(len(spell_prices)) and Gold >= spell_prices[spellChoiceName]:

                        if spell_data[spellChoiceName] not in learned_spells:
                            print("You haven't learned that spell yet, so you can't infuse it.")
                            continue

                        infusionAmount = -1
                        for index, spell in enumerate(SPELLS):
                            if spell["Name"] == spellChoiceName:
                                maxPotential = min(Gold // spell_prices[spellChoiceName], spell["Stacking"] - Items["Staff"]["Spells"][spellChoiceName]["Amount"])
                        while infusionAmount < 0 or infusionAmount > maxPotential:
                            infusionRequest = input(f"How many {spellChoiceName}s do you want to infuse? (max {maxPotential}) ")
                            if intConvertable(infusionRequest):
                                infusionAmount = int(infusionRequest)
                                if infusionAmount > maxPotential:
                                    print("Invalid response")
                            else:
                                print("Invalid response")
                        
                        for spell in Items["Staff"]["Spells"]:
                            if spell["Type"]["Name"] == spellChoiceName:
                                spell["Amount"] += infusionAmount
                        Gold -= spell_prices[spellChoiceName] * infusionAmount        
                        print(f"Successfully infused {infusionAmount} {spellChoiceName}{'s' if infusionAmount != 1 else ''} into your staff for {spell_prices[spellChoiceName] * infusionAmount} gold. You now have {Gold} gold remaining.")

                    elif Gold < spell_prices[spellChoiceName]:
                        print("You don't have enough gold to infuse that spell.")
                    else:
                        print("Invalid spell choice.")

    return Gold, Items, spell_prices, spell_data, learned_spells

# <debug, but likely permanent>
def organize(dictionary):
    """
    Displays the key-value pairs of the dictionary
    :param dictionary: dict - the dictionary you wish to see organized
    """
    if type(dictionary) != dict:
        print("Hey, thats not a dictionary!")
    else:
        longest = 0
        for i in range(len(list(dictionary.keys()))):
            if len(str(list(dictionary.keys())[i])) > longest:
                longest = len(str(list(dictionary.keys())[i]))
        for i in range(len(list(dictionary.keys()))):
            if len(list(dictionary.keys())[i]+":"+" "*(longest+1-len(list(dictionary.keys())[i]))+str(dictionary[list(dictionary.keys())[i]])) > 156:
                print("")
            print(list(dictionary.keys())[i]+":"+" "*(longest+1-len(list(dictionary.keys())[i]))+str(dictionary[list(dictionary.keys())[i]]))
            if len(list(dictionary.keys())[i]+":"+" "*(longest+1-len(list(dictionary.keys())[i]))+str(dictionary[list(dictionary.keys())[i]])) > 156:
                print("")
# </debug>
def intConvertable(string_to_check):
    """
    Checks if the string can be converted to an integer without an error.
    :param string_to_check: str - The input string to be checked for convertibility.
    :return: bool - True if the input string can be converted to an integer, False otherwise.
    """
    try:
        int(string_to_check)
        return True
    except ValueError:
        return False

def clear():
    """
    Clears the terminal screen.
    For Windows, uses the 'cls' command.
    For macOS and Linux, uses the 'clear' command.
    Requires: import os
    """
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux (here, os.name is 'posix')
    else:
        os.system('clear')


def generate_random_enemy(level):
    if level == 1:
        enemy = random.choice([{
            "Race": "Goblin",
            "Armor": RuggedHideArmor,
            "Items": {"MainHand": {"Item": Dagger, "Amount": 1}},
            "Hp": 3
        }, {
            "Race": "Wolf",
            "Armor": None,
            "Items": None,
            "Hp": 4
        }])
    elif level == 2:
        enemy = random.choice([{
            "Race": "Goblin",
            "Armor": RuggedHideArmor,
            "Items": {"MainHand": {"Item": Shortsword, "Amount": 1}},
            "Hp": 3
        }, {
            "Race": "Dark Elf",
            "Armor": RuggedHideArmor,
            "Items": {"MainHand": {"Item": Shortsword, "Amount": 1}},
            "Hp": 4
        }])
    elif level == 3:
        enemy = random.choice([{
            "Race": "Goblin",
            "Armor": ArcherCoat,
            "Items": {"MainHand": {"Item": Bow, "Amount": 1}, "SecondHand": {"Item": Arrow, "Amount": 1}, "Quiver": {"Item": Arrow, "Amount": random.randint(11, 23)}},
            "Hp": 3
        }, {
            "Race": "Dark Elf",
            "Armor": ShadowSteelArmor,
            "Items": {"MainHand": {"Item": Shortsword, "Amount": 1}},
            "Hp": 4
        }])
    elif level == 4:
        enemy = random.choice([{
            "Race": "Orc",
            "Armor": RuggedHideArmor,
            "Items": {"MainHand": {"Item": SpikedClub, "Amount": 1}},
            "Hp": 5
        }, {
            "Race": "Giant Spider",
            "Armor": None,
            "Items": None,
            "Hp": 10
        }])
    elif level == 5:
        enemy = random.choice([{
            "Race": "Orc",
            "Armor": RuggedHideArmor,
            "Items": {"MainHand": {"Item": BattleAxe, "Amount": 1}},
            "Hp": 5
        }, {
            "Race": "Giant Spider",
            "Armor": None,
            "Items": None,
            "Hp": 10
        }])
    
    return enemy

def get_key():  # This function runs in a separate thread and continuously reads user input.
  global key
  global previous_valid
  global game_over
  global pending_actions
  while not game_over:  # It runs until the game is over.
    allowed = ["a", "s", "d", "w", "t", "e", "1", "2", "3", "4", "5", "6", "7", "8", " ", "j", "k", "b", "c", "p"]
    while key not in allowed and not game_over:  # It waits for a valid user input.
      key = readchar.readchar().lower()  # It reads a single character input from the user and converts it to lowercase.
    if key != previous_valid:  # If the new input is different from the previous valid input:
      previous_valid = key  # Update the previous valid input.
      pending_actions.append(previous_valid)  # Add the new valid input to the pending actions list.
      if key == "p": # debug
        quit()
    key = "None"  # Reset the key variable after processing the input.

def display_map(grid, player_coordinates, fov=120.0):
    """
    prints a given map onto the screen where the player is placed at the bottom and can only see within a certain fov
    :param grid: list of list of str - The map to be displayed
    :param player_coordinates: list of int - The coordinates of the player
    :param fov: float, optional - angle in degrees that the player can see. Default is 120.0.
    """
    # Define the grid size
    GRID_SIZE = len(grid) # NOTE: map must be square
    
    # Define the field of view (FOV) angle in radians
    FOV_ANGLE = math.tau * (fov / 360)  # Convert 120 degrees to radians

    # Create the grid
    #grid = [[" _" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Place the 'Y' at the center of the bottom row
    #grid[BOTTOM_Y][CENTER_X] = " Y" # this will already be done

    visible_grid = deepcopy(grid)

    # Replace characters outside the FOV with black boxes
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            # Calculate the angle between the center and the current position
            DELTA_Y = y - player_coordinates[0]
            DELTA_X = x - player_coordinates[1]
            try:
              ANGLE = math.atan(DELTA_Y/DELTA_X)
            except ZeroDivisionError:
              ANGLE = math.tau/4 # this equals 90 degrees
            # Check if the position is outside the FOV
            if DELTA_Y > 0 or not math.tau/4-abs(ANGLE) < FOV_ANGLE/2:
                visible_grid[y][x] = ("█" if x != 0 and grid[y][x-1][1] == "█" else " ") + "█"  # Replace with a black box character

    # Print the grid
    grid_str = "\n".join(["".join(row) for row in visible_grid])
    clear()
    print(grid_str)

def generate_map():
    GRID_SIZE = 9
    
    CENTER_X = GRID_SIZE // 2
    BOTTOM_Y = GRID_SIZE - 1

    grid = [[' _' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    grid[BOTTOM_Y][CENTER_X] = " Y"

    ENEMY_X = random.randint(0, GRID_SIZE-1)
    ENEMY_Y = random.randint(0, GRID_SIZE // 2)

    grid[ENEMY_Y][ENEMY_X] = " E"

    COORDINATES = (BOTTOM_Y, CENTER_X)
    ENEMY_COORDINATES = (ENEMY_Y, ENEMY_X)

    return grid, COORDINATES, ENEMY_COORDINATES

def move(grid, entity_coordinates, entity_char, delta_y, delta_x):
    if entity_coordinates[0]+delta_y < 0 or entity_coordinates[0]+delta_y >= len(grid): # assumes all columns are equal length
        delta_y = 0
    if entity_coordinates[1]+delta_x < 0 or entity_coordinates[1]+delta_x >= len(grid[0]): # assumes all rows are equal length
        delta_x = 0
    if grid[entity_coordinates[0]+delta_y][entity_coordinates[1]+delta_x] != " _":
        return grid, entity_coordinates
    grid[entity_coordinates[0]][entity_coordinates[1]] = " _"
    entity_coordinates = [entity_coordinates[0]+delta_y, entity_coordinates[1]+delta_x]
    grid[entity_coordinates[0]][entity_coordinates[1]] = f" {entity_char}"
    return grid, entity_coordinates

def run_combat(grid, enemy):
    global key
    global previous_valid
    global game_over
    global pending_actions
    global coordinates
    
    display_map(grid, coordinates)
    
    while not game_over:
        # get target action
        previous_valid = ""
        TARGET_ACTION = "" if pending_actions == [] else pending_actions.pop(0)  # Get the next action from the pending actions list or set it to nothing.
        if TARGET_ACTION == "":
            pass
        elif TARGET_ACTION == "a":
            grid, coordinates = move(grid, coordinates, "Y", 0, -1)
        elif TARGET_ACTION == "s":
            grid, coordinates = move(grid, coordinates, "Y", 1, 0)
        elif TARGET_ACTION == "d":
            grid, coordinates = move(grid, coordinates, "Y", 0, 1)
        elif TARGET_ACTION == "w":
            grid, coordinates = move(grid, coordinates, "Y", -1, 0)
        elif TARGET_ACTION == "e":
            pass
        elif TARGET_ACTION == " ":
            pass
        elif TARGET_ACTION == "j":
            pass
        elif TARGET_ACTION == "k":
            pass
        elif TARGET_ACTION == "b":
            pass
        elif TARGET_ACTION == "t":
            pass
        elif TARGET_ACTION in "1234567890":
            pass
        elif TARGET_ACTION == "c":
            game_over = True
        else:
            raise Exception("Somethings wrong, I can feel it. TARGET_ACTION:", TARGET_ACTION, "previous_valid:", previous_valid, "pending_actions:", pending_actions)  # This exception is raised if an unexpected condition occurs.
        display_map(grid, coordinates)
        # TODO: logic for combat here ## WORKING HERE
        
def combat():
    global key
    global previous_valid
    global game_over
    global pending_actions
    global coordinates
    global enemy_coordintates
    # <debug>
    enemy = generate_random_enemy(2)
    grid, coordinates, enemy_coordintates = generate_map()
    # </debug>
    key = "None"
    previous_valid = ""
    pending_actions = []
    game_over = False

    t1 = threading.Thread(target=get_key)
    t2 = threading.Thread(target=run_combat, args=(grid, enemy))
    input("Press enter to start") # bc why not, but likely temporary
    t1.start()
    t2.start()
    while not game_over:
        pass
    return game_over

# Test the function
#random_enemy = generate_random_enemy(3)
#print(random_enemy)

# Starting the program
START_TIME = time()
location = Deshica
print("You start at the small village of "+location["Name"])
print("You have "+str(Gold)+" gold")
while True:
    Gold, Items, destination, learned_spells = options(Gold, Items, learned_spells)
    destination = settlement(destination)
    location = destination
    print("You are now at "+location["Name"])
    
# to do:
# make the fighting monsters part
# combat
# custom settlements for the wall, wolf forest, the frosty mountains, Oskesh and Ogron
