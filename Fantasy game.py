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
arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken = None, None, None, None, None, None, None, None, None, None, None
variables = [arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken]

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
"Damage": 1, # 1*Items["Armor"]["Magic"]
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
"Damage": 1, # 2*Items["Armor"]["Magic"]
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
# these are the two skills
Skills = [Lightningbolt, Fireball]
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
def shop(city, Gold, Items, new, variables):
    arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken = variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10]
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
                variables = [arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken]
                return Gold, Items, variables # otherwise, it exits the shop function as a whole
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
                    Items["Staff"]["Spells"] = []
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
    variables = [arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken]
    return Gold, Items, variables
def options(Gold, Items):
    arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken = None, None, None, None, None, None, None, None, None, None, None
    variables = [arrowWhich, arrowAmount, shurikenWhich, shurikenAmount, possible, sold_weapons, weapon_prices, sold_armors, armor_prices, attachment_prices, already_taken]
    action = None
    first = True
    while action != "1":
        action = None
        while action != "1" and action != "2" and action != "3" and (action != "4" or location in villages):
            if location in villages:
                print("You can: leave for another settlement(1), shop for items(2), or fight monsters on the egde of the village (3)")
            else:
                print("You can: leave for another settlement(1), shop for items(2), fight monsters on the egde of the city (3) or learn magic at the acadamy (4)")
            action = input()
        if action == "1":
            print("Where do you want to go?")
            for i in range(len(location["Bordering"])):
                print(str(i+1)+": "+location["Bordering"][i])
            print(str(i+2)+": stay here")
            destination = "None"
            while True:
                if destination in "123456789" and len(destination) == 1: # make the acadamy part
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
            Gold, Items, variables = shop(location not in villages, Gold, Items, first, variables)
            first = False
        elif action == "3":
            pass
        elif action == "4":
            pass
        else:
            pass
    return Gold, Items, destination
def settlement(name):
    for i in range(len(cities)):
        if cities[i]["Name"] == name:
            return cities[i]
    for i in range(len(villages)):
        if villages[i]["Name"] == name:
            return villages[i]
def acadamy(Gold, Items):
    """
    This function allows the player to acquire new spells by spending gold. The available spells and their prices are determined by the location of the acadamy.
    :param Gold: int - The player's current amount of gold.
    :param Items: list - The player's current inventory of items.
    :return: tuple - Updated values of Gold and Items.
    """
    # List of available spells and their prices
    spells = {Fireball["Name"]: Fireball["Price"]+random.randint(-10, 10), Lightningbolt["Name"]: Lightningbolt["Price"]+random.randint(-10, 10)}
    print("Welcome to the acadamy! The following spells are available for purchase:")
    count = 0
    for spell, price in spells.items():
        count += 1
        print(f"{spell}: {price} gold ({count})")
    # Ask player which spell they want to purchase
    spell_choice = "Invalid"
    while True:
        if tallifiser(spell_choice):
            if len(spells.keys()) >= int(spell_choice):
                break
        spell_choice = input("Which spell would you like to purchase? ") # FIX THIS PART, NEED TO CONVERT 1 OR 2 INTO THE SPELL NEEDED
    # Check if spell is available and player has enough gold
    if spell_choice in range(1, len(spells)) and Gold >= spells[spell_choice]:
        Gold -= spells[spells.keys()[spell_choice-1]]
        Items["Staff"]["Spells"].append(spells[spells.keys()[spell_choice]])
        Items["Staff"]["Amount"] += 1
        print(f"Successfully purchased {spell_choice} for {spells[spell_choice]} gold.")
    else:
        print("Invalid spell choice or not enough gold.")
    return Gold, Items

#/* Debug, but likely permanent
def organize(dictionary):
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
    return
#*/ Debug
def tallifiser(tall):
    """
    denne funksjonen returnerer "True" om den kan bli int uten error
    :param tall: str - tallet som kanskje ikke er et tall
    :return: bool - om tall kan bli gjort om til int uten error.
    """
    for i in range(len(tall)):
        if not tall[i] in "1234567890":
            return False
    return tall != ""

# Starting the program
location = Deshica
print("You start at the small village of "+location["Name"])
print("You have "+str(Gold)+" gold")
Gold, Items, destination = options(Gold, Items)
while True:
    destination = settlement(destination)
    location = destination
    print("You are now at "+location["Name"])
    Gold, Items, destination = options(Gold, Items)

# to do:
# make the acadamy part
# make the fighting monters part
# combat
