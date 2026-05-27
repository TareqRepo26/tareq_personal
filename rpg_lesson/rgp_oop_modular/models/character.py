from .weapon import Weapon

class Character:
    def __init__(self, name, health, damage, weapon_name=None, weapon_damage=0):
        self.name = name
        self._health = health
        self.damage = damage
        self.weapon = Weapon(weapon_name, weapon_damage) if weapon_name else None

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = max(0, health)

    def attack(self, enemy):
        total_damage = self.damage

        if self.weapon:
            total_damage += self.weapon.damage_bonus

        enemy.set_health(enemy.get_health() - total_damage)

        print(f"{self.name} attacks {enemy.name} for {total_damage} damage!")

        return total_damage