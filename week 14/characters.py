
import random


class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.hp = len(name) + 10
        self.weapon = weapon

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0


class Hero(Character):
    def attack(self, other):
        damage = len(self.weapon)

        print(f"\n{self.name} attacks {other.name} with {self.weapon}!")

        if damage == 0:
            print(f"{other.name} dodges the attack!")
        else:
            if damage > other.hp:
                print("CRITICAL HIT!")

            other.take_damage(damage)
            print(f"{other.name} loses {damage} HP.")

        # Hero may recover some health
        if random.random() < 0.3:
            healing = random.randint(1, 3)
            self.hp += healing
            print(f"{self.name} recovers {healing} HP!")

        print(f"{self.name}: {self.hp} HP")
        print(f"{other.name}: {other.hp} HP")


class Villain(Character):
    def attack(self, other):
        damage = random.randint(0, len(self.weapon) * 2 + 5)

        # Villain becomes more dangerous when low on HP
        if self.hp <= 5 and damage > 0:
            damage += random.randint(2, 5)

        print(f"\n{self.name} attacks {other.name} with {self.weapon}!")

        if damage == 0:
            print(f"{other.name} dodges the attack!")
        else:
            if damage > other.hp:
                print("CRITICAL HIT!")

            other.take_damage(damage)
            print(f"{other.name} loses {damage} HP.")

        print(f"{self.name}: {self.hp} HP")
        print(f"{other.name}: {other.hp} HP")
