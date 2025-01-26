# Maddox Duggan
# 101483006
# January 26, 2025s


import random

# define Variables
numLives = 10  # Number of player's lives remaining
mNumLives = 12  # Number of monster's lives remaining

# generate dice options dynamically
diceOptions = list(range(1, 7))

# display available weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Available Weapons:")
for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")

# player information
while True:
    try:
        # get input for combat strength
        combatStrength = int(input("Enter your combat strength (1-6): "))
        # if input is within range, keep going with simulation
        if 1 <= combatStrength <= 6:
            break
        # if input is not within range, output
        else:
            print("Input must be an integer between 1 and 6.")
    # if input is not an int, output
    except ValueError:
        print("Please enter a valid integer.")

# monster information
while True:
    try:
        mCombatStrength = int(input("Enter the monster's combat strength (1-6): "))
        # if input is within range, keep going with simulation
        if 1 <= mCombatStrength <= 6:
            break
        # if input is not in range, output
        else:
            # output
            print("Input must be an integer between 1 and 6.")
    # if input is not an int, output
    except ValueError:
        print("Please enter a valid integer.")

# actual battle
for round_num in range(1, 20, 2):
    print(f"\n--- Round {round_num} ---")

    # dice roll for weapon
    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)

    # dice roll for strength
    hero_strength = combatStrength + hero_roll
    monster_strength = mCombatStrength + monster_roll

    # Determine weapons based on dice rolls
    hero_weapon = weapons[hero_roll - 1]
    monster_weapon = weapons[monster_roll - 1]

    # output
    print(f"Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_strength}, Monster Total Strength: {monster_strength}.")

    # who wins
    if hero_strength > monster_strength:
        print("Hero wins the round!")
    elif hero_strength < monster_strength:
        print("Monster wins the round!")
    else:
        print("It's a tie!")

    # truce conditional
    if round_num == 11:
        print("Battle Truce declared in Round 11. Game Over!")
        break
