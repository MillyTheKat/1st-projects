player = input("Please enter your name: ")
print(f"Hello {player}, let's begin your adventure!")

print("Prologue: The Journey Begins")
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
paragraph6 = "The merchant noticed the book and leaned closer. 'That book… it looks like the kind described in the stories of the Pond of Peace,' he said. 'They say such books can restore lost memories—but only with a special pen to guide their magic.'"
