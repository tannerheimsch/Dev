import csv
from objects import Player

FILENAME = "players.csv"

def read_players():
    try:
        with open(FILENAME, 'r', newline='') as file:
            reader = csv.reader(file)
            players = [Player(*row) for row in reader]
    except FileNotFoundError:
        players = []
    return players

def write_players(players):
    with open(FILENAME, 'w', newline='') as file:
        csv.writer(file).writerows([p.firstName, p.lastName, p.position, p.atBats, p.hits] for p in players)
