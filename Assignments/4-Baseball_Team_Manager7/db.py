import csv

FILENAME = "players.csv"

def read_players():
    players = []
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            players.append(row)
    return players

def write_players(players):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        for player in players:
            writer.writerow(player)