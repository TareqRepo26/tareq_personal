from .character import Character

class Boss(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "Boss Weapon", 5)

    def attack(self, enemy):
        base_damage = super().attack(enemy)

        special_damage = 1
        enemy.set_health(enemy.get_health() - special_damage)

        print(f"{self.name} uses SPECIAL ATTACK for +{special_damage} damage!")

        return base_damage + special_damage

class Sauron(Boss):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)