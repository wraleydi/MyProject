class Character:
    def __init__(self, name, health, weapon, attack_power):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack_power = attack_power
        self.inventory = []

class Game:
    def __init__(self):
        self.character = None

    def play(self):
        print("Selamat datang di permainan RPG!")
        play = input("==========  Play  ==========\n==========  Exit  ==========\n\n        ketik Y/N: ")
        if play.lower() == "y":
            character_name = input("Masukkan nama karakter Anda: ")
            self.character = Character(character_name, 100, "Sword", 20)
            print(f"\n       Informasi Hero: \nNama: {character_name}\n"
                f"Darah: {self.character.health}\n"
                f"Senjata: {self.character.weapon}\n"
                f"Damage: {self.character.attack_power}")
        else:
            print("Terimakasih")

game = Game()
game.play()