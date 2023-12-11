import csv
from objects import Player

FILENAME = "players.csv"

def read_players():
    try:
        players = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                player = Player(row[0], row[1], row[2], int(row[3]), int(row[4]))
                players.append(player)
        return players
    except FileNotFoundError:
        return None

def write_players(players):
    with open(FILENAME, "w") as file:
        for player in players:
            file.write(player.firstName + ",")
            file.write(player.lastName + ",")
            file.write(player.position + ",")
            file.write(str(player.atBats) + ",")
            file.write(str(player.hits) + "\n")

