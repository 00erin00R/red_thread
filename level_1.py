class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.strength} damage!")
        target.health -= self.strength

    def __str__(self):
        return f"Character({self.name}, Health: {self.health}, Strength: {self.strength})"

def game():
    starter=Character("human",70,10)
    print("Welcome to the game, you are a stranded human with limited resources. Can u make it to the next level?")
    print("######################################################################################################")
    