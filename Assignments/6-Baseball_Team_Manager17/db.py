import sqlite3
from contextlib import closing
from objects import Player, Lineup

DATABASE = "player_db.sqlite"  # Database name

def connect():
    return sqlite3.connect(DATABASE)

def close(connection):
    connection.close()

def make_player(row):
    return Player(row[2], row[3], row[4], row[5], row[6], row[0], row[1])  # Adjusted column order

def get_players():
    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Player ORDER BY batOrder")  # Ensure the data is ordered by batOrder
        players = [make_player(row) for row in cursor.fetchall()]
    return players

def get_player(player_id):
    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Player WHERE playerID = ?", (player_id,))
        row = cursor.fetchone()
        if row:
            return make_player(row)
        return None

def add_player(player):
    with closing(connect()) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits) VALUES (?, ?, ?, ?, ?, ?)",
                       (player.batOrder, player.firstName, player.lastName, player.position, player.atBats, player.hits))
        db.commit()

def delete_player(player):
    with closing(connect()) as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM Player WHERE playerID=?", (player.playerID,))
        db.commit()

def update_bat_order(lineup):
    with connect() as connection:
        cursor = connection.cursor()
        for i, player in enumerate(lineup, start=1):
            cursor.execute("UPDATE Player SET batOrder = ? WHERE playerID = ?", (i, player.playerID))
        connection.commit()

def update_player(player):
    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE Player SET position = ?, atBats = ?, hits = ? WHERE playerID = ?", (player.position, player.atBats, player.hits, player.playerID))
        connection.commit()

def main():
    pass