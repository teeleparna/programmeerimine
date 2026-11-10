
with open("data/heroes.txt", "r", encoding="utf-8") as f:
    heroes = f.readlines()

for hero in heroes:
    print(hero.strip())
