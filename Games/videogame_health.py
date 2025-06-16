class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

    def status(self):
        print(f"The player, {self.name}, is alive and has {self.health} HP.")


player1 = Player("Mohit", 72)
player2 = Player("Aryan", 100)
player3 = Player("Chase", 0)

players = [player1, player2, player3]
for player in players:
    if player.is_alive():
        player.status()
    else:
        print(f"The player, {player.name}, is defeated and has 0 HP.")