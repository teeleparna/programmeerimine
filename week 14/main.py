
from file_utils import get_random_value
from characters import Hero, Villain


# Choose random characters and weapons
hero_name = get_random_value("data/heroes.txt")
villain_name = get_random_value("data/villains.txt")

hero_weapon = get_random_value("data/weapons.txt")
villain_weapon = get_random_value("data/weapons.txt")


# Create character objects
hero = Hero(hero_name, hero_weapon)
villain = Villain(villain_name, villain_weapon)


# Display game information
print("================================")
print("       HERO VS VILLAIN")
print("================================")

print(f"Hero: {hero.name}")
print(f"Weapon: {hero.weapon}")
print(f"HP: {hero.hp}")

print("--------------------------------")

print(f"Villain: {villain.name}")
print(f"Weapon: {villain.weapon}")
print(f"HP: {villain.hp}")

print("================================")
print("          FIGHT STARTS!")
print("================================")


# Fight until one character loses all HP
while hero.is_alive() and villain.is_alive():

    hero.attack(villain)

    if villain.is_alive():
        villain.attack(hero)


# Display the winner
print("\n================================")
print("          GAME OVER")
print("================================")

if hero.is_alive():
    print("Hero saves the day.")
else:
    print("Dark Side wins.")
