import os
import random
import json
import time


SAVE="save.json"


player={
"x":0,
"hp":100,
"food":50,
"water":50,
"wood":0,
"stone":0,
"money":20,
"level":1,
"xp":0,
"day":1,
"weapon":"🪵 Stick",
"pet":"❌",
"vehicle":"❌"
}


world={}



def clear():
    os.system("clear")



def wait():

    input("\n⏎ Press Enter...")



def refresh():

    clear()
    status()



def save():

    json.dump(player,open(SAVE,"w"))

    print("💾 Saved!")

    wait()



def load():

    global player

    try:

        player=json.load(open(SAVE))

        print("📂 Loaded!")

    except:

        print("❌ No save")

    wait()




def zone(x):

    if x not in world:

        world[x]=random.choice(
        [
        "🌲 Forest",
        "🏜 Desert",
        "🏙 City",
        "🚇 Metro",
        "🏠 House",
        "🏪 Shop"
        ])

    return world[x]




def status():

    print("""
╔════════════════════╗
   🌍 SURVIVAL RPG
╚════════════════════╝
""")

    print("📅 Day:",player["day"])
    print("⭐ Level:",player["level"])
    print("❤️ HP:",player["hp"])
    print("🍖 Food:",player["food"])
    print("💧 Water:",player["water"])
    print("🪵 Wood:",player["wood"])
    print("🪨 Stone:",player["stone"])
    print("💰 Money:",player["money"])
    print("⚔️ Weapon:",player["weapon"])
    print("🐾 Pet:",player["pet"])
    print("🚗 Car:",player["vehicle"])

    print("\n📍 Location:",zone(player["x"]))





def move():

    c=input("""
⬅️ a
➡️ d

> """)


    if c=="a":

        player["x"]-=1


    elif c=="d":

        player["x"]+=1


    print("🚶 Moved!")

    wait()





def collect():

    z=zone(player["x"])


    if "🌲" in z:

        n=random.randint(1,10)

        player["wood"]+=n

        print("🪵 Wood +",n)



    elif "🏜" in z:

        player["stone"]+=5

        print("🪨 Stone +5")



    elif "🏙" in z:

        player["money"]+=10

        print("💰 Money +10")



    else:

        print("❌ Nothing found")


    wait()
# Part 2/2


def fight():

    enemy=random.choice(
    [
    ("🧟 Zombie",30),
    ("🐺 Wolf",25),
    ("🥷 Bandit",45)
    ])


    name,power=enemy


    print("⚔️ Enemy:",name)


    attack=player["level"]*10+random.randint(5,30)


    if attack>=power:


        print("🏆 Enemy defeated!")

        player["money"]+=20

        player["xp"]+=30


        if player["xp"]>=100:

            player["level"]+=1

            player["xp"]=0

            print("⭐ LEVEL UP!")



    else:


        player["hp"]-=20

        print("💥 You got damage!")



    wait()





def house():

    print("""
🏠 HOUSE

1 😴 Sleep
2 🌱 Farm
3 Exit
""")


    c=input("> ")


    if c=="1":

        player["hp"]=100

        player["day"]+=1

        print("😴 Rest complete")



    elif c=="2":

        player["food"]+=20

        print("🌱 Food +20")


    wait()





def metro():

    print("🚇 Metro exploring...")


    r=random.randint(1,3)


    if r==1:

        player["money"]+=50

        print("💰 Treasure found")


    elif r==2:

        player["stone"]+=20

        print("🪨 Materials found")


    else:

        fight()


    wait()





def shop():

    print("""
🏪 SHOP

1 🍖 Food 10$
2 💧 Water 10$
3 ⚔️ Sword 50$

""")


    c=input("> ")



    if c=="1" and player["money"]>=10:

        player["money"]-=10

        player["food"]+=30

        print("🍖 Bought")



    elif c=="2" and player["money"]>=10:

        player["money"]-=10

        player["water"]+=30

        print("💧 Bought")



    elif c=="3" and player["money"]>=50:

        player["money"]-=50

        player["weapon"]="⚔️ Sword"

        print("⚔️ Sword unlocked")


    wait()





def pet():

    if player["pet"]=="❌":

        player["pet"]=random.choice(
        [
        "🐕 Dog",
        "🐈 Cat",
        "🐺 Wolf"
        ])

        print("🐾 New pet:",player["pet"])


    else:

        print("🐾 Your pet:",player["pet"])


    wait()





def vehicle():


    print("""
🚗 VEHICLE

1 🏍 Bike 100$
2 🚙 Car 300$

""")


    c=input("> ")


    if c=="1" and player["money"]>=100:

        player["money"]-=100

        player["vehicle"]="🏍 Bike"

        print("🏍 Bike bought")



    elif c=="2" and player["money"]>=300:

        player["money"]-=300

        player["vehicle"]="🚙 Car"

        print("🚙 Car bought")


    wait()





def damage_survival():

    player["food"]-=1
    player["water"]-=1


    if player["food"]<=0:

        player["hp"]-=5


    if player["water"]<=0:

        player["hp"]-=5





# MAIN LOOP


while True:


    clear()

    status()


    print("""
━━━━━━━━━━━━━━

1 🚶 Move
2 🌍 Collect
3 ⚔️ Fight
4 🏠 House
5 🚇 Metro
6 🏪 Shop
7 🐾 Pet
8 🚗 Vehicle
9 💾 Save
10 📂 Load
0 ❌ Exit

━━━━━━━━━━━━━━
""")


    choice=input("> ")



    if choice=="1":

        move()



    elif choice=="2":

        collect()



    elif choice=="3":

        fight()



    elif choice=="4":

        house()



    elif choice=="5":

        metro()



    elif choice=="6":

        shop()



    elif choice=="7":

        pet()



    elif choice=="8":

        vehicle()



    elif choice=="9":

        save()



    elif choice=="10":

        load()



    elif choice=="0":

        print("👋 Bye")

        break



    damage_survival()


    if player["hp"]<=0:

        clear()

        print("""
☠️ YOU DIED

Game Over
""")

        break