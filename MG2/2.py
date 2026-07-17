import os
import random
import json
import time


SAVE="save3d.json"


player={
"x":5,
"y":5,

"hp":100,
"energy":100,

"food":50,
"water":50,

"wood":0,
"stone":0,
"iron":0,

"money":100,

"level":1,
"xp":0,

"day":1,

"weapon":"🪵 Stick",
"armor":"👕 Cloth",

"inventory":[],

"pet":"❌",

"base":False
}


SIZE=11


world={}



def clear():
    os.system("clear")



def wait():
    input("\n⏎ Enter...")



def tile():

    return random.choice(
    [
    "🌲",
    "🏠",
    "⛏️",
    "🌊",
    "🏜️",
    "🏪",
    "🧟",
    "⬜"
    ])



def create_world():

    for y in range(SIZE):

        for x in range(SIZE):

            world[(x,y)]=tile()



create_world()



def save():

    json.dump(player,open(SAVE,"w"))

    print("💾 Saved")

    wait()



def load():

    global player

    try:

        player=json.load(open(SAVE))

        print("📂 Loaded")

    except:

        print("No save")

    wait()




def draw_map():

    print("\n🌍 3D WORLD MAP\n")


    for y in range(SIZE):

        line=""

        for x in range(SIZE):

            if x==player["x"] and y==player["y"]:

                line+="😎"

            else:

                line+=world[(x,y)]

        print(line)



def status():

    print("""
╔═══════════════╗
 🌍 SURVIVAL 3D
╚═══════════════╝
""")


    print(
    "❤️",player["hp"],
    "⚡",player["energy"],
    "🍖",player["food"],
    "💧",player["water"]
    )


    print(
    "💰",player["money"],
    "⭐",player["level"]
    )

# PART 2/4


def move():

    print("""
⬆️ w
⬇️ s
⬅️ a
➡️ d
""")


    c=input("> ")


    if c=="w":
        player["y"]-=1

    elif c=="s":
        player["y"]+=1

    elif c=="a":
        player["x"]-=1

    elif c=="d":
        player["x"]+=1



    player["energy"]-=5


    limit()



def limit():

    if player["x"]<0:
        player["x"]=0

    if player["y"]<0:
        player["y"]=0

    if player["x"]>=SIZE:
        player["x"]=SIZE-1

    if player["y"]>=SIZE:
        player["y"]=SIZE-1





def current():

    return world[
    (
    player["x"],
    player["y"]
    )
    ]





def interact():


    place=current()


    print(
    "📍 You are at:",
    place
    )


    if place=="🌲":

        wood=random.randint(1,10)

        player["wood"]+=wood

        print(
        "🪵 Wood +",
        wood
        )



    elif place=="⛏️":

        mine()



    elif place=="🏪":

        shop()



    elif place=="🏠":

        house()



    elif place=="🧟":

        enemy()



    else:

        print("Nothing here")



    wait()





def mine():

    print("⛏️ Mining...")


    r=random.randint(1,3)


    if r==1:

        player["iron"]+=10

        print("⚙️ Iron +10")


    elif r==2:

        player["stone"]+=15

        print("🪨 Stone +15")


    else:

        print("Empty mine")





def house():

    print("""
🏠 HOUSE

1 Rest
2 Build Base
""")


    c=input("> ")


    if c=="1":

        player["hp"]=100

        player["energy"]=100

        print("😴 Rested")



    elif c=="2":

        if player["wood"]>=50:

            player["wood"]-=50

            player["base"]=True

            print("🏠 Base Built!")

        else:

            print("Need 50 wood")





def shop():

    print("""
🏪 SHOP

1 🍖 Food 20$
2 💧 Water 20$
3 ⚔️ Weapon 100$

""")


    c=input("> ")


    if c=="1":

        if player["money"]>=20:

            player["money"]-=20

            player["food"]+=30



    elif c=="2":

        if player["money"]>=20:

            player["money"]-=20

            player["water"]+=30



    elif c=="3":

        if player["money"]>=100:

            player["money"]-=100

            player["weapon"]="⚔️ Sword"





def npc():

    print("""
👤 NPC

1 Trader
2 Doctor
3 Hunter

""")


    c=input("> ")


    if c=="1":

        shop()


    elif c=="2":

        player["hp"]=100

        print("❤️ Healed")


    elif c=="3":

        player["food"]+=20

        print("🍖 Food gift")

# PART 3/4


def enemy():

    enemies=[

    ("🧟 Zombie",40),
    ("🐺 Wolf",30),
    ("🥷 Bandit",50),
    ("👹 Mutant",80)

    ]


    e=random.choice(enemies)

    print(
    "⚔️ Enemy:",
    e[0]
    )


    attack=player["level"]*15+random.randint(10,40)


    if attack>=e[1]:

        print("🏆 Enemy defeated")

        player["money"]+=30

        player["xp"]+=50

        level_up()



    else:

        player["hp"]-=30

        print("💥 Damage!")





def boss():

    print("""
👑 BOSS

☠️ Giant Mutant
HP:200
""")


    attack=player["level"]*20+random.randint(20,60)


    if attack>=200:

        print("🏆 BOSS defeated!")

        player["money"]+=500

        player["xp"]+=200

        level_up()


    else:

        player["hp"]-=70

        print("☠️ Boss attack!")



    wait()





def level_up():

    if player["xp"]>=100:


        player["level"]+=1

        player["xp"]=0

        print("⭐ Level UP!")





def weather():


    w=random.choice(
    [
    "☀️ Sunny",
    "🌧 Rain",
    "❄️ Snow",
    "🌪 Storm"
    ])


    print(
    "Weather:",
    w
    )


    if w=="🌪 Storm":

        player["hp"]-=10


    elif w=="🌧 Rain":

        player["water"]+=20





def night():


    if player["day"]%2==0:

        print("🌙 Night")

        player["energy"]-=20


    else:

        print("☀️ Day")





def new_day():

    player["day"]+=1


    player["food"]-=5

    player["water"]-=5


    weather()

    night()



def inventory():

    print("""
🎒 INVENTORY

⚔️ Weapon:
""",
player["weapon"])


    print("""
🛡 Armor:
""",
player["armor"])


    print(
    "🪵 Wood:",
    player["wood"]
    )

    print(
    "🪨 Stone:",
    player["stone"]
    )

    print(
    "⚙️ Iron:",
    player["iron"]
    )


    wait()





def quest():


    quests=[

    "Collect 50 Wood 🪵",

    "Defeat 5 Zombies 🧟",

    "Find Hidden Treasure 💎"

    ]


    q=random.choice(quests)


    print("""
📜 New Quest:

""",
q)


    player["xp"]+=20


    wait()





def craft():


    print("""
🛠 CRAFT

1 ⚔️ Iron Sword
2 🛡 Armor

""")


    c=input("> ")


    if c=="1":

        if player["iron"]>=20:

            player["iron"]-=20

            player["weapon"]="⚔️ Iron Sword"

            print("Crafted!")


    elif c=="2":

        if player["iron"]>=30:

            player["iron"]-=30

            player["armor"]="🛡 Iron Armor"

            print("Armor created")


    wait()
    

# PART 4/4


def survival_check():

    if player["food"]<=0:

        player["hp"]-=10

        print("🍖 No food!")


    if player["water"]<=0:

        player["hp"]-=10

        print("💧 No water!")



    if player["energy"]<=0:

        player["hp"]-=5





def run():

    while True:


        clear()


        status()


        draw_map()


        print("""
━━━━━━━━━━━━━━━━
🎮 MENU

1 🚶 Move
2 🔍 Interact
3 ⚔️ Fight
4 👑 Boss
5 🎒 Inventory
6 🛠 Craft
7 📜 Quest
8 👤 NPC
9 💾 Save
10 📂 Load
11 🌅 New Day
0 ❌ Exit

━━━━━━━━━━━━━━━━
""")


        c=input("> ")



        if c=="1":

            move()



        elif c=="2":

            interact()



        elif c=="3":

            enemy()



        elif c=="4":

            boss()



        elif c=="5":

            inventory()



        elif c=="6":

            craft()



        elif c=="7":

            quest()



        elif c=="8":

            npc()



        elif c=="9":

            save()



        elif c=="10":

            load()



        elif c=="11":

            new_day()



        elif c=="0":

            print("""
👋 Goodbye Survivor
""")

            break



        survival_check()



        if player["hp"]<=0:


            clear()


            print("""
☠️ GAME OVER

You died in the wasteland.
""")


            break



        time.sleep(1)





# START GAME

run()