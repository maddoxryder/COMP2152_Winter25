# Import the random library to use for the dice
import random

# Define the weapons array with increasing strength levels
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Define Variables
try:
    numLives = 10  # number of player's lives remaining
    mNumLives = 12  # number of monster's lives remaining

    diceOptions = [1, 2, 3, 4, 5, 6]

    # Input validation for combat strength
    combatStrength = int(input("Enter your combat Strength (integer only): "))
    mCombatStrength = int(input("Enter the monster's combat Strength (integer only): "))

    # Roll the dice for health points
    input("Roll the dice for your health points (Press enter)")
    healthPoints = random.choice(diceOptions)
    print("You rolled " + str(healthPoints) + " health points")

    # Roll the dice for the monster's health points
    input("Roll the dice for the monster's health points (Press enter)")
    mHealthPoints = random.choice(diceOptions)
    print("You rolled " + str(mHealthPoints) + " health points for the monster")

    # Roll the dice to see if you find a healing potion
    input("Roll the dice to see if you find a healing potion (Press enter)")
    healingPotion = random.choice([0, 1])
    print("Have you found a healing potion?: " + str(bool(healingPotion)))

    # --- Weapon Selection ---
    input("Roll the dice to choose your weapon (Press enter)")
    weaponRoll = random.choice(diceOptions) - 1  # Subtract 1 to match array indexing
    selectedWeapon = weapons[weaponRoll]
    print("You rolled a " + str(weaponRoll + 1) + " and got the weapon: " + selectedWeapon)

    # Add weapon strength to combat strength
    combatStrength += weaponRoll + 1
    print("Your updated combat strength with the weapon is: " + str(combatStrength))

    # Weapon condition messages
    if weaponRoll + 1 <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll + 1 <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    if selectedWeapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

    # --- Expanded if statement ---
    if healthPoints >= 5:
        print("--- Your health is ok")
    elif healingPotion == 1:
        healingPotion = 0
        healthPoints = 6
        print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
    else:
        print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

    # --- Combat ---
    print("You meet the monster. FIGHT!!")
    input("You strike first (Press enter)")

    print("Your weapon (" + selectedWeapon + ") with combat strength (" + str(combatStrength) +
          ") ---> Monster (" + str(mHealthPoints) + ")")
    if combatStrength >= mHealthPoints:
        mHealthPoints = 0
        print("You've killed the monster!")
    else:
        mHealthPoints -= combatStrength
        print("You've reduced the monster's health to: " + str(mHealthPoints))

        print("The monster strikes!!!")
        print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
        if mCombatStrength >= healthPoints:
            healthPoints = 0
            print("You're dead")
        else:
            healthPoints -= mCombatStrength
            print("The monster has reduced your health to: " + str(healthPoints))

except ValueError:
    print("Error: Please enter valid integers for combat strength and try again.")
except IndexError:
    print("Error: Something went wrong with the weapon roll. Please check the dice roll logic.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
