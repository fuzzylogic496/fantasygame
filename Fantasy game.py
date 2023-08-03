# imports:
import random
# Defining them so errors don't appear in the program
Otren = None
Aspel = None
Shaton = None
Jaflen = None
Esmar = None
Guclia = None
Ethad = None
Deshica = None
Kibron = None
Root = None
Leaf = None
Branch = None
TheWall = None
Ogron = None
TheFrostyMountains = None
WolfForest = None
Oskesh = None
#arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken = None, None, None, None, None, None, None, None, None, None, None
#shopVariables = [arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken]
#Villages
Snecor = {
"Name": "Snecor",
"Bordering": ["The Wall", "Kibron"]
}
Aspel = {
"Name": "Aspel",
"Bordering": ["Otren"]
}
Shaton = {
"Name": "Shaton",
"Bordering": ["Deshica", "Root"]
}
Jaflen = {
"Name": "Jaflen",
"Bordering": ["Ethad", "Otren"]
}
TheFrostyMountains = {
"Name": "The Frosty Mountains",
"Bordering": ["Wolf-Forest", "Oskesh"]
}
WolfForest = {
"Name": "Wolf-Forest",
"Bordering": ["TheWall", "The Frosty Mountains"]
}
TheWall = {
"Name": "The Wall",
"Bordering": ["Wolf-Forest", "Snecor"]
}
Deshica = {
"Name": "Deshica",
"Bordering": ["Kibron", "Ethad", "Shaton"]
}
villages = [Snecor, Aspel, Shaton, Jaflen, TheFrostyMountains, WolfForest, TheWall, Deshica]
#Cities:
Otren = {
"Name": "Otren",
"Bordering": ["Aspel", "Jaflen", "Guclia"]
}
Esmar = {
"Name": "Esmar",
"Bordering": ["Kibron"]
}
Guclia = {
"Name": "Guclia",
"Bordering": ["Otren"]
}
Ethad = {
"Name": "Ethad",
"Bordering": ["Kibron", "Jaflen"]
}

Kibron = {
"Name": "Kibron",
"Bordering": ["Esmar", "Snecor", "Ethad", "Deshica"]
}
Root = {
"Name": "Root",
"Bordering": ["Branch", "Shaton"]
}
Leaf = {
"Name": "Leaf",
"Bordering": ["Branch"]
}
Branch = {
"Name": "Branch",
"Bordering": ["Root", "Leaf"]
}
Ogron = {
"Name": "Ogron",
"Bordering": ["Oskesh"]
}
Oskesh = {
"Name": "Oskesh",
"Bordering": ["Ogron", "The Frosty Mountains"]
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
"Price": 100,
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
"Protection": 8,
"Magic": 5,
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
#Items:
Gold = 1000000000 # 100, currently changed for debug purposes
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
Items = {'MainHand': {'Item': [], 'Amount': 0}, 'SecondHand': {'Item': [], 'Amount': 0}, 'BootLeft': {'Item': None, 'Amount': 0}, 'BootRight': {'Item': None, 'Amount': 0}, 'ScabbardSlotLeft': {'Item': None, 'Amount': 0}, 'ScabbardSlotRight': {'Item': None, 'Amount': 0}, 'ScabbardSlotBackLeft': {'Item': None, 'Amount': 0}, 'ScabbardSlotBackRight': {'Item': None, 'Amount': 0}, 'BowSlotBack': {'Item': None, 'Amount': 0}, 'QuiverSlotBack': {'Item': None, 'Amount': 0}, 'ShieldSlotBack': {'Item': None, 'Amount': 0}, 'ShurikenSlotLeft': {'Item': None, 'Amount': 0}, 'ShurikenSlotRight': {'Item': None, 'Amount': 0}, 'AxeLoopBack': {'Item': None, 'Amount': 0}, 'PotionSlotLeft': {'Item': None, 'Amount': 0}, 'PotionSlotRight': {'Item': {'Name': 'Health Potion', 'Projectile': False, 'Stacking': 3, 'DamagePerInstance': -5, 'Slots': ['PotionSlotRight', 'PotionSlotLeft'], 'Speed': 1, 'TimeLeft': 1, 'Price': 125, 'Packet': False, 'Potion': True}, 'Amount': 2}, 'StaffSlotBack': {'Item': {'Name': 'Staff', 'Damage': 1, 'Slots': ['StaffSlotBack'], 'Speed': 1, 'Weapon': True, 'Projectile': False, 'Stacking': 1, 'Price': 150, 'Packet': False, 'Potion': False}, 'Amount': 1}, 'Staff': {'Spells': [{'Type': {'Name': 'Fireball', 'Damage': 1, 'Slots': ['Staff'], 'Speed': 2, 'Weapon': False, 'Projectile': True, 'Requires': [{'Name': 'Staff', 'Damage': 1, 'Slots': ['StaffSlotBack'], 'Speed': 1, 'Weapon': True, 'Projectile': False, 'Stacking': 1, 'Price': 150, 'Packet': False, 'Potion': False}], 'Stacking': 36, 'Price': 100, 'Packet': False, 'Potion': False}, 'Amount': 0}, {'Type': {'Name': 'Lightning bolt', 'Damage': 2, 'Slots': ['Staff'], 'Speed': 1, 'Weapon': False, 'Projectile': True, 'Requires': [{'Name': 'Staff', 'Damage': 1, 'Slots': ['StaffSlotBack'], 'Speed': 1, 'Weapon': True, 'Projectile': False, 'Stacking': 1, 'Price': 150, 'Packet': False, 'Potion': False}], 'Stacking': 3, 'Price': 150, 'Packet': False, 'Potion': False}, 'Amount': 0}], 'Amount': 0}, 'AxeFrogRight': {'Item': None, 'Amount': 0}, 'AxeFrogLeft': {'Item': None, 'Amount': 0}, 'Armor': {'Name': 'WizardRobes', 'WeaponSlots': ['PotionSlotRight', 'PotionSlotLeft', 'StaffSlotBack'], 'Slowness': 2, 'Protection': 1, 'Magic': 6, 'Price': 65, 'Plural': True}} # debug, remove when finished
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
VillageWeapons = [Dagger, Bow, Arrow, Hatchet, KnightSword, PoisonPotion]
VillageArmors = [ArcherCoat, BarbarianRags, KnightArmor]
CityWeapons = [Ninjato, Bow, Arrow, Shuriken, BattleAxe, Staff, Shortsword, KnightSword, HealthPotion, DamagePotion, PoisonPotion, RegenerationPotion]
CityArmors = [NinjaGi, MageArmor, WizardRobes, BattleMageArmor, KnightArmor]
# defines which ones are attachments
Attachments = [Scabbard, ScabbardBack, Quiver, AxeLoop, AxeFrog]
# defines which ones are armors
Armors = [BasicClothes, KnightArmor, BarbarianRags, NinjaGi, MageArmor, WizardRobes, BattleMageArmor, ArcherCoat]
# keeps track of what spells the player can infuse their staff with
learnedSpells = []
spells = [Fireball, Lightningbolt]
# The things that only need the armor to attach
AutoAttachments = ["BootLeft", "BootRight", "StaffSlotBack", "ShurikenSlotLeft", "ShurikenSlotRight", "BowSlotBack", "PotionSlotRight", "PotionSlotLeft"]
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
    if string[0] in "aeiouyAEIOUY":
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
def shop(city, Gold, Items, new, shopVariables):
    arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken = shopVariables[0], shopVariables[1], shopVariables[2], shopVariables[3], shopVariables[4], shopVariables[5], shopVariables[6], shopVariables[7], shopVariables[8], shopVariables[9], shopVariables[10]
    if new:
        if city:
            random.shuffle(CityWeapons)
            random.shuffle(CityArmors)
            possible = [CityWeapons.copy(), CityArmors.copy()] # randomizes the two lists, so we get different options each time
        else:
            random.shuffle(VillageWeapons)
            random.shuffle(VillageArmors)
            possible = [VillageWeapons.copy(), VillageArmors.copy()] # the same as the last, but for the villages
        arrowWhich, arrowAmount, possible = multiple(Arrow, possible, 3, 24)
        shurikenWhich, shurikenAmount, possible = multiple(Shuriken, possible, 3, 3)
        random.shuffle(Attachments) # and then it randomizes the attachments outside, because villages and cities have the same attachments
        sold_weapons = [possible[0][0], possible[0][1]]
        weapon_prices = [negative_check(sold_weapons[0]["Price"]-random.randint(-20, 20)), negative_check(sold_weapons[1]["Price"]-random.randint(-20, 20))]
        sold_armors = [possible[1][0], possible[1][1]]
        armor_prices = [sold_armors[0]["Price"]-random.randint(-20, 20), sold_armors[1]["Price"]-random.randint(-20, 20)]
        attachment_prices = [Attachments[0]["Price"]-random.randint(-20, 20), Attachments[1]["Price"]-random.randint(-20, 20)]
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
    if available(already_taken, 5, len(Attachments[0]["Name"])+len(str(attachment_prices[0]))+13):
        print(Attachments[0]["Name"]+" for "+str(attachment_prices[0])+" gold(5)", end="")
    print(" and ", end="")
    if available(already_taken, 6, len(Attachments[1]["Name"])+len(str(attachment_prices[1]))+14):
        print(""+Attachments[1]["Name"]+" for "+str(attachment_prices[1])+" gold(6).")
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
                        if sold_weapons[int(purchase)-1]["Slots"][i] in AutoAttachments and sold_weapons[int(purchase)-1]["Slots"][i] in Items["Armor"]["WeaponSlots"] and Items[sold_weapons[int(purchase)-1]["Slots"][i]]["Item"] == None:
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
                    for i in range(len(Attachments[int(purchase)-5]["Unlocks"])):
                        if Items[Attachments[int(purchase)-5]["Unlocks"][i]]["Item"] == None:
                            beenHere2 = True
                            if Attachments[int(purchase)-5]["Unlocks"][i] in Items["Armor"]["WeaponSlots"]:                        
                                willWork2 = True
                                break
                        if willWork2:
                            break
                    if not willWork2:
                        if not beenHere2 and Attachments[int(purchase)-5] == Quiver or Attachments[int(purchase)-5] == AxeLoop or ("ScabbardSlotLeft" in Items["Armor"]["WeaponSlots"] and "ScabbardSlotRight" not in Items["Armor"]["WeaponSlots"]) or ("AxeFrogLeft" in Items["Armor"]["WeaponSlots"] and "AxeFrogRight" not in Items["Armor"]["WeaponSlots"]):
                            print("You've already unlocked that slot")
                        elif beenHere2:
                            print("Your armor can't support that attachment!")
                        else:
                            print("You've already unlocked those slots")
                    else:
                        purchase = Attachments[int(purchase)-5]
                        break
            else:
                shopVariables = [arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken]
                return Gold, Items, shopVariables # otherwise, it exits the shop function as a whole
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
        if purchase in Attachments: # checks if the purchase is an attachment
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
            Fireball["Damage"] = 1*Items["Armor"]["Magic"]
            Lightningbolt["Damage"] = 2*Items["Armor"]["Magic"]
            DamagePotion["DamagePerInstance"] = 5*round(Items["Armor"]["Magic"]/2)
            RegenerationPotion["DamagePerInstance"] = -1*round(Items["Armor"]["Magic"]/2)
            for i in range(len(list(Items.keys()))):
                if not list(Items.keys())[i] in ["Armor", "MainHand", "SecondHand", "Staff"]:
                    if not list(Items.keys())[i] in Items["Armor"]["WeaponSlots"]:
                        Items[list(Items.keys())[i]]["Item"] = None
                        Items[list(Items.keys())[i]]["Amount"] = 0
                elif list(Items.keys())[i] == "Staff":
                    if Items["StaffSlotBack"]["Amount"] == 0:
                        Items[list(Items.keys())[i]]["Spells"] = None
                        Items[list(Items.keys())[i]]["Amount"] = 0 
        more = "None"
        while more.lower() != "no" and more.lower() != "yes":
            print("Anything else? (write \"no\" to exit the shop, or write \"yes\" to make another purchase)")
            more = input()
        if more.lower() == "no":
            done = True
        else:
            done = False
            print("And that is ...?")
    shopVariables = [arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken]
    return Gold, Items, shopVariables
def options(Gold, Items, learnedSpells):
    arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken = None, None, None, None, None, None, None, None, None, None, None
    shopVariables = [arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken]
    spellPrices, spellData = None, None
    academyVariables = [spellPrices, spellData]
    action = None
    first = True
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
                if destination in "123456789" and len(destination) == 1: # make the academy part
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
            Gold, Items, shopVariables = shop(location not in villages, Gold, Items, first, shopVariables)
            first = False
        elif action == "3":
            pass
        elif action == "4":
            Gold, Items, academyVariables, learnedSpells = academy(Gold, Items, academyVariables, learnedSpells) # debug
        else:
            pass
    return Gold, Items, destination, learnedSpells
def settlement(name):
    for i in cities:
        if i["Name"] == name:
            return i
    for i in villages:
        if i["Name"] == name:
            return i
def academy(Gold, Items, academyVariables, learnedSpells): # TODO: remove the "Amount" and "Spells" part of the staff, and turn the staff into just the spells part. The amount part is useless.
    spellPrices, spellData = academyVariables[0], academyVariables[1]
    """
    This function allows the player to acquire new spells by infusing them into their staff using gold.
    :param Gold: int - The player's current amount of gold.
    :param Items: list - The player's current inventory of items.
    :param academyVariables: list - Additional variables for the academy.
    :param learnedSpells: list - List of spells the player has already learned.
    :return: tuple - Updated values of Gold, Items, academyVariables, and learnedSpells.
    """
    if Items["Staff"]["Spells"] is None:
        print("You need a staff to learn spells!")
        return Gold, Items, academyVariables, learnedSpells

    if spellPrices is None:
        spellPrices = {
            Fireball["Name"]: Fireball["Price"] + random.randint(-10, 10),
            Lightningbolt["Name"]: Lightningbolt["Price"] + random.randint(-10, 10)
        }  # TODO: make the prices stay the same when at the same place

    if spellData is None:
        spellData = {Fireball["Name"]: Fireball, Lightningbolt["Name"]: Lightningbolt}

    academyVariables = [spellPrices, spellData]

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
                for spell, data in spellData.items():
                    if data not in learnedSpells:
                        available_spells.append(spell)
                if not available_spells:
                    print("You have already learned all available spells.")
                    break

                count = 0
                for spell in available_spells:
                    count += 1
                    print(f"{spell}: 50 gold ({count})")
                print("Whenever you wish to get back to the main hall, type \"e\".")

                spellChoice = "Invalid"
                while True:
                    if intConvertable(spellChoice):
                        if len(available_spells) >= int(spellChoice):
                            break
                    spellChoice = input("Which spell would you like to learn? ")
                    if spellChoice.lower() == "e":
                        done = True
                        break
                if not done:
                    spellChoiceName = available_spells[int(spellChoice) - 1]
                    if int(spellChoice) - 1 in range(len(available_spells)) and Gold >= 50:

                        Gold -= 50
                        learnedSpells.append(spellData[spellChoiceName])

                        for i in Items["Staff"]["Spells"]:
                            if i["Type"]["Name"] == spellChoiceName:
                                i["Amount"] += min(Items['Armor']['Magic'], i["Type"]["Stacking"] - i["Amount"])
                        
                        print(f"Successfully learned {spellChoiceName} for 50 gold. Your staff has been infused with {min(Items['Armor']['Magic'], i['Type']['Stacking'] - i['Amount'])} {spellChoiceName}{'s' if Items['Armor']['Magic'] > 1 else ''}. You now have {Gold} gold remaining.") # TODO: this one seems to display the wrong number. Fix.

                    elif Gold < 50:
                        print("You don't have enough gold to learn that spell.")
                    else:
                        print("Invalid spell choice.")
        elif academyChoice == "2":
            while not done:
                count = 0

                for spell, price in spellPrices.items():
                    count += 1
                    print(f"{spell}: {price} gold ({count})")
                print("Whenever you want to return to the main hall, type \"e\".")

                spellChoice = "Invalid"
                while True:
                    if intConvertable(spellChoice):
                        if len(spellPrices.keys()) >= int(spellChoice):
                            break
                    spellChoice = input("Which spell would you like to infuse into your staff? ")
                    if spellChoice.lower() in ["e"]:
                        done = True
                        break

                if not done:
                    spellChoiceName = list(spellPrices.keys())[int(spellChoice) - 1]
                    if int(spellChoice) - 1 in range(len(spellPrices)) and Gold >= spellPrices[spellChoiceName]:

                        if spellData[spellChoiceName] not in learnedSpells:
                            print("You haven't learned that spell yet, so you can't infuse it.")
                            continue

                        infusionAmount = -1
                        while infusionAmount < 0 or infusionAmount > min(Gold // spellPrices[spellChoiceName], i["Stacking"] - Items["Staff"]["Spells"][index]["Amount"]):
                            for index, i in enumerate(spells):
                                if i["Name"] == spellChoiceName:
                                    maxPotential = min(Gold // spellPrices[spellChoiceName], i["Stacking"] - Items["Staff"]["Spells"][index]["Amount"])
                            infusionRequest = input(f"How many of {spellChoiceName} do you want to infuse? (max {maxPotential})")
                            infusionAmount = -1 if not intConvertable(infusionRequest) else int(infusionRequest)
                            if not intConvertable(infusionRequest):
                                print("Invalid response")

                                done = True # TODO: these are only supposed to happen if you have chosen a correct amount.
                                break 
                            
                        if not done:
                            
                            spellFound = False
                            for i in Items["Staff"]["Spells"]:
                                if i["Type"]["Name"] == spellChoiceName:
                                    if i["Amount"]+infusionAmount > i["Type"]["Stacking"]:
                                        infusionAmount = i["Type"]["Stacking"] - i["Amount"]
                                        print(f"You can only have a max of {i['Type']['Stacking']} of them infused.")
                                    i["Amount"] += min(infusionAmount, i['Type']['Stacking']-i["Amount"])
                                    spellFound = True
                            #if not spellFound: # TODO: I believe this part can be entirely removed. Just commented out, and will see if I get any errors.
                            #    Items["Staff"]["Spells"].append({"Type": spellData[spellChoiceName], "Amount": infusionAmount})
                            #    Items["Staff"]["Amount"] += 1
                            Gold -= spellPrices[spellChoiceName] * min(infusionAmount, i['Type']['Stacking']-i["Amount"])

                            print(f"Successfully infused {min(infusionAmount, i['Type']['Stacking']-i['Amount'])} of {spellChoiceName} into your staff for {spellPrices[spellChoiceName] * min(infusionAmount, i['Type']['Stacking']-i['Amount'])} gold. You now have {Gold} gold remaining.")
                    elif Gold < spellPrices[spellChoiceName]:
                        print("You don't have enough gold to infuse that spell.")
                    else:
                        print("Invalid spell choice.")

    return Gold, Items, academyVariables, learnedSpells

#/* Debug, but likely permanent
def organize(dictionary):
    """
    tidys up dictionaries so that you can clearly see the keys and the corresponding values
    :param dictionary: dict - the dictionary you with to see organized
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
#*/ Debug
def intConvertable(stringToCheck):
    """
    This function checks if a given string can be converted to an integer without an error.
    :param stringToCheck: str - The input string to be checked for convertibility.
    :return: bool - True if the input string can be converted to an integer, False otherwise.
    """
    for i in stringToCheck:
        if not i in "1234567890":
            return False
    return stringToCheck != ""

# Starting the program
location = Deshica
print("You start at the small village of "+location["Name"])
print("You have "+str(Gold)+" gold")
Gold, Items, destination, learnedSpells = options(Gold, Items, learnedSpells)
while True:
    destination = settlement(destination)
    location = destination
    print("You are now at "+location["Name"])
    Gold, Items, destination = options(Gold, Items, learnedSpells)

# to do:
# make the academy part
# make the fighting monsters part
# combat
# have prices and stock in shop and academy be determined by irl time since last visit, instead of going back and fourth
