import random

players = {}
basic_factions_list = {
    "The Arborec": {
        "Description": "A sentient plant species that grows its military forces instead of building them. Slow to start but powerful late game.",
        "Pros": "Can grow units for free each turn, strong late game.",
        "Cons": "Weak early game, slow expansion, relies on planets for production."
    },
    "The Barony of Letnev": {
        "Description": "A cold, warlike faction with powerful fleets and strong military production. Their economy fuels their military dominance.",
        "Pros": "Strong economy, powerful fleets, extra fleet capacity.",
        "Cons": "Weak starting position, slow unit production."
    },
    "The Clan of Saar": {
        "Description": "A nomadic people who don’t rely on planets for income. Their space docks move, making them hard to pin down.",
        "Pros": "Mobile space docks, doesn't need planets for income.",
        "Cons": "No home system to defend, vulnerable in the late game."
    },
    "The Embers of Muaat": {
        "Description": "A fiery race that starts with a War Sun, the game’s most powerful ship. Strong in combat but slow to expand.",
        "Pros": "Starts with a powerful War Sun, strong in battle.",
        "Cons": "Slow expansion, high resource costs, weak early game."
    },
    "The Emirates of Hacan": {
        "Description": "A wealthy feline-like species that dominates the galactic economy. They can trade with anyone and generate tons of resources.",
        "Pros": "Best economy, can trade freely with everyone, flexible strategies.",
        "Cons": "No direct combat buffs, targeted by other players for trade deals."
    },
    "The Federation of Sol": {
        "Description": "A disciplined, well-rounded faction with extra command tokens and strong ground forces. Great for new players.",
        "Pros": "Extra command tokens, strong ground forces, flexible playstyle.",
        "Cons": "No major strengths outside of action economy."
    },
    "The Ghosts of Creuss": {
        "Description": "Mysterious beings that manipulate wormholes, allowing them to move across the galaxy with ease.",
        "Pros": "Can move through wormholes freely, unique movement abilities.",
        "Cons": "Can be isolated, tricky to master, weak in direct combat."
    },
    "The L1Z1X Mindnet": {
        "Description": "A cybernetic empire that seeks galactic domination. Their ships are more powerful than others, making them deadly in battle.",
        "Pros": "Strong ships, easy tech access, great in combat.",
        "Cons": "Expensive units, not great at diplomacy or trade."
    },
    "The Mentak Coalition": {
        "Description": "A rebellious pirate faction that steals trade goods from others and excels in hit-and-run tactics.",
        "Pros": "Steals trade goods from others, good at hit-and-run tactics.",
        "Cons": "No strong direct combat advantages, often targeted by enemies."
    },
    "The Naalu Collective": {
        "Description": "A psychic species that always takes the first action in a round. They excel at using swarms of fighters in battle.",
        "Pros": "Always plays first, great at defense, strong fighters.",
        "Cons": "Weak early expansion, relies on fighters for strength."
    },
    "The Nekro Virus": {
        "Description": "An AI-driven faction that cannot trade or negotiate but steals technology from defeated enemies.",
        "Pros": " Steals tech from enemies, strong ships, no need for diplomacy.",
        "Cons": "Can’t trade or negotiate, relies on winning fights for tech."
    },
    "The Sardakk N'orr": {
        "Description": "A warlike insectoid species with a simple goal: conquer everything. They get a +1 bonus to all combat.",
        "Pros": "+1 combat bonus to all fights, simple and aggressive playstyle.",
        "Cons": "No special economy or tech advantages, must always be fighting."
    },
    "The Universities of Jol-Nar": {
        "Description": "A highly intelligent but fragile species that advances technology faster than any other faction.",
        "Pros": "Researches tech faster than anyone, huge tech advantage.",
        "Cons": "Weaker in combat, relies on diplomacy to survive early game."
    },
    "The Winnu": {
        "Description": "Descendants of the old Lazax Empire, obsessed with reclaiming Mecatol Rex. Good at planetary control.",
        "Pros": "Easy access to Mecatol Rex, good at controlling planets.",
        "Cons": "No strong combat advantages, weak early game."
    },
    "The Xxcha Kingdom": {
        "Description": "A peaceful, slow-moving species with strong influence in politics and good defensive abilities.",
        "Pros": "Strong in politics, great at defense, avoids combat.",
        "Cons": "Weak in direct fights, slow to expand."
    },
    "The Yin Brotherhood": {
        "Description": "A cult-like faction that uses suicide attacks and mind control to spread its influence.",
        "Pros": "Strong ground forces, suicide ships for surprise attacks.",
        "Cons": "Not great at diplomacy, needs aggression to be effective."
    },
    "The Yssaril Tribes": {
        "Description": "A sneaky faction that draws extra action cards, allowing them to delay their actions and control the game’s pace.",
        "Pros": "Draws extra action cards, great at delaying turns and outmaneuvering opponents.",
        "Cons": "No direct combat bonuses, can be seen as a big threat early."
    }
}

expansion_factions_list = {
    "The Argent Flight": {
        "Description": "A bird-like warrior species that acts as the galaxy’s self-appointed police force, using powerful defensive fleets.",
        "Pros": "Strong fleet, good at defense and offense, powerful PDS network.",
        "Cons": "Limited economic advantages, requires aggressive play."
    },
    "The Empyrean": {
        "Description": "A shadowy race that controls wormholes and influences galactic politics from behind the scenes.",
        "Pros": "Manipulates wormholes, strong influence over negotiations.",
        "Cons": "Weaker in combat, relies on trade and politics."
    },
    "The Mahact Gene": {
        "Description": "A tyrannical empire that steals command tokens from opponents and manipulates DNA for power.",
        "Pros": "Steals command tokens from other players, strong economy.",
        "Cons": "Makes enemies fast, slow start without early aggression."
    },
    "The Naaz-Rokha Alliance": {
        "Description": "A coalition of cybernetic feline beings that use mechs in unique ways, making them great at ground warfare.",
        "Pros": "Can move mechs like spaceships, good at planetary control.",
        "Cons": "Weak in space combat early on, relies on mechs."
    },
    "The Nomad": {
        "Description": "A mysterious faction with a flagship that can teleport, allowing for incredible flexibility and surprise attacks.",
        "Pros": "Has a unique flagship that can teleport, strong action economy.",
        "Cons": "Needs time to set up, can be unpredictable."
    },
    "The Titans of Ul": {
        "Description": "A slow-moving but powerful faction that transforms planets into mechs, making them nearly unstoppable in defense.",
        "Pros": "Turns planets into mechs, great at defense and slow expansion.",
        "Cons": "Weak economy at first, needs time to grow strong."
    },
    "The Vuil’Raith Cabal": {
        "Description": "A horrifying species that steals enemy ships and turns them into their own, making them a nightmare in battle.",
        "Pros": "Can capture enemy ships and use them, strong economy.",
        "Cons": "Makes enemies fast, requires aggressive play."
    }
}

first_choice = list(basic_factions_list.keys())
second_choice = first_choice + list(expansion_factions_list.keys())

while True:
    try:
        player_number = int(input("Please enter the number of players: "))
        break
    except ValueError:
        print("Invalid input. Please enter the number again.")

while len(players) < player_number:
    player_name = input(f"Please enter your name: ").strip()
    if player_name in players:
        print("This name is already taken. Please choose the other name.")
    else:
        player_first_choice = random.choice(first_choice)
        second_choice.remove(player_first_choice)
        player_second_choice = random.choice(second_choice)
        players[player_name] = (player_first_choice, player_second_choice)
        print(f"Welcome {player_name}. You have 2 choices: {player_first_choice} and {player_second_choice}")
        print("Do you want to know short description, pros and/or cons?")
        print("1. description only.")
        print("2. Pros only.")
        print("3. Cons only.")
        print("4. Prs and Cons.")
        print("5. All information")

        while True:
            try:
                player_choice = int(input("I choose: "))
                break
            except ValueError:
                print("Invalid input. Please choose again.")

        if player_choice == 1:
            print()
