from models.character import Character
from models.boss import Boss

class Game:
    def __init__(self):
        self.player = None
        self.bosses = []

    # -------------------------
    # INTRO
    # -------------------------
    def intro(self):
        print("=================================")
        print("        RPG ADVENTURE")
        print("=================================")
        print("In a world where darkness looms...")
        print("You are the chosen hero.")
        print("Defeat all bosses to restore peace!\n")

    # -------------------------
    # CREATE PLAYER
    # -------------------------
    def create_player(self):
        name = input("Enter your character name: ")

        print("\nChoose your weapon:")
        print("1. Rock (+2)")
        print("2. Paper (+3)")
        print("3. Scissors (+4)")

        choice = input("Choice: ")

        if choice == "1":
            weapon_name, weapon_damage = "Rock", 2
        elif choice == "2":
            weapon_name, weapon_damage = "Paper", 3
        else:
            weapon_name, weapon_damage = "Scissors", 4

        self.player = Character(name, 110, 10, weapon_name, weapon_damage)

        print(f"\n{name} equipped {weapon_name}!\n")

    # -------------------------
    # CREATE BOSSES
    # -------------------------
    def create_bosses(self):
        self.bosses = [
            Boss("Goblin King", 50, 8),
            Boss("Dark Sorcerer", 60, 9)
        ]

    # -------------------------
    # BATTLE SYSTEM
    # -------------------------
    def battle(self, boss):
        print(f"\n===== {boss.name} APPEARS =====")

        while self.player.get_health() > 0 and boss.get_health() > 0:

            print("\n--- STATUS ---")
            print(f"{self.player.name}: {self.player.get_health()} HP")
            print(f"{boss.name}: {boss.get_health()} HP")

            input("\nPress Enter to attack...")

            # Player turn
            self.player.attack(boss)

            if boss.get_health() <= 0:
                print(f"\n{boss.name} defeated!")
                return True

            # Boss turn
            boss.attack(self.player)

            if self.player.get_health() <= 0:
                print("\nYou have been defeated...")
                return False

        return True

    # -------------------------
    # START GAME
    # -------------------------
    def start(self):
        self.intro()
        self.create_player()
        self.create_bosses()

        for boss in self.bosses:
            result = self.battle(boss)

            if not result:
                print("\nGAME OVER")
                return

        print("\n=========================")
        print(" YOU WIN!")
        print(" All bosses defeated!")
        print("=========================")