player = input("Please enter your name: ")
print(f"Hello {player}, let's begin your adventure!")

player_info = {
    "heal" : 10,
    "attack" : 3,
    "defense" : 2,
    "level" : 1,
    "XP" : 0,
    "level_up" : 10,
}

forest_beast = {
    "Wolf": {"health": 8, "attack": 4, "defense": 1},
    "Wild Boar": {"health": 12, "attack": 5, "defense": 2},
    "Bandit": {"health": 15, "attack": 6, "defense": 3}
}

swamp_beast = {
    "Giant Spider": {"health": 10, "attack": 4, "defense": 2},
    "Swamp Serpent": {"health": 14, "attack": 6, "defense": 2},
    "Bog Golem": {"health": 18, "attack": 7, "defense": 5}
}

snowy_beast = {
    "Polar Bear": {"health": 16, "attack": 6, "defense": 4},
    "Frost Viking": {"health": 20, "attack": 7, "defense": 5},
    "Ice Phantom": {"health": 12, "attack": 5, "defense": 3}
}

mountain_beast = {
    "Shadow Wraith": {"health": 14, "attack": 7, "defense": 3},
    "Undead Knight": {"health": 18, "attack": 8, "defense": 5},
    "Bone Wyvern": {"health": 25, "attack": 10, "defense": 6}
}

print("\n\nPrologue: The Journey Begins")
paragraph1 = "The gentle creak of wooden wheels and the rhythmic clatter of hooves on a dusty road pulled you from a deep, dreamless sleep. Blinking against the morning light, you found yourself lying on a makeshift bed in the back of a merchant’s carriage."
paragraph2 = "A voice greeted you—a kindly merchant sitting at the reins, glancing back over their shoulder. 'Ah, you're awake! We found you by the roadside. You looked like you needed help, so we brought you along. But now that you're up...' The merchant paused, studying you with curiosity. 'Who are you, traveler?'"
paragraph3 = "You hesitated. The question hung in the air, but the answer wouldn’t come easily"

text1 = paragraph1 + "\n\n" + paragraph2 + "\n\n" + paragraph3 + "\n"
print(text1)

print("1. Tell the merchant your name.")
print("2. Stay silent.")
print("3. Admit you can’t remember.")

print("\nThe merchant tilted their head, waiting patiently for your response.")

while True:
    try:
        player_choice1 = int(input("Please enter the number of your choice: "))
        break
    except ValueError:
        print("Invalid input. Please enter your choice again.")

if player_choice1 == 1:
    print(f"You clear your throat and speak, though your voice feels unfamiliar to your ears. 'My name is {player}.' You give the merchant your name, though the words feel strange, as though they belong to someone else.")
elif player_choice1 == 2:
    print("You remain silent, unsure of how to respond. The merchant’s expression softened. 'No need to say anything if you’re not ready. Rest for now. You’re safe here.'")
else:
    print("You shake your head, frustration bubbling inside. 'I don’t know. I can’t remember anything.'")

paragraph4 = "The merchant’s eyes widened slightly, then softened with sympathy. 'Perhaps it’s fate that brought you here. We’ll do our best to help you figure it out.'"
paragraph5 = "After the exchange, you shifted your attention to a small bag near your side. Inside, you found a handful of coins, three healing potions, and an old, worn book. Its cover was faded, the title illegible, and its pages seemed incomplete, as though something vital had been torn away."
paragraph6 = "The merchant nods, his expression thoughtful. 'A myth. They say it’s a place where lost memories can be restored—or erased—depending on what the seeker desires. But a book like that…' He gestures toward the strange object in your hands. 'It needs something to awaken it. Something like… this.'"
paragraph7 = "From his belt, he pulled out a pen unlike any you had ever seen. It shimmered faintly with an otherworldly glow, its sleek surface etched with intricate runes that pulsed softly in harmony with the book. As they held it closer, the inkpot on the book’s cover seemed to react, glowing faintly, as though the two were meant to be together."
paragraph8 = "'This pen,' the merchant said, 'was a gift I received years ago. It’s not easy to come by, but it could help you unlock the book’s secrets. However...'  They hesitated before continuing, 'it won’t come cheap. I’ll sell it to you for 100 coins'"
paragraph9 = "You looked down at your small bag of coins, realizing the cost would leave you with nothing for the journey ahead.\n\nThe merchant noticed your hesitation. 'If that’s too steep, perhaps there’s another way. What do you say?'"

text2 = paragraph4 + "\n\n" + paragraph5 + "\n\n" + paragraph6 + "\n\n" + paragraph7 + "\n\n" + paragraph8 + "\n\n" + paragraph9 + "\n"
print(text2)

print("1. Pay for it")
print("2. Offer to help the merchants.")

while True:
    try:
        player_choice2 = int(input("Please enter the number of your choice: "))
        break
    except ValueError:
        print("Invalid input. Please enter your choice again.")

if player_choice2 == 1:
    print("You sighed and handed over your coins. 'Here you are,' you said reluctantly.\n\nThe merchant nodded, passing you the pen with a knowing smile. 'A fair trade. This pen is yours now. Treat it well—it’s more than just a tool.'")
else:
    print("You cleared your throat. 'I don’t have enough to pay for it. Is there something I can do in exchange?'\n\nThe merchant’s eyes gleamed with interest. 'As a matter of fact, yes. We’ve had a bit of trouble lately, and someone with your determination might just be able to help us.'")


