class Player:
    def __init__(self, first_name, last_name, position, at_bats, hits, playerID, batOrder=0):
        self.firstName = first_name
        self.lastName = last_name
        self.position = position
        self.atBats = int(at_bats)
        self.hits = int(hits)
        self.playerID = int(playerID)
        self.batOrder = int(batOrder)

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @property
    def battingAvg(self):
        if self.atBats == 0:
            return 0.0
        batting_avg = round(self.hits / self.atBats, 3)
        return batting_avg

class Lineup:
    def __init__(self):
        self.__list = []

    @property
    def count(self):
        return len(self.__list)

    def add(self, player):
        return self.__list.append(player)

    def remove(self, number):
        return self.__list.pop(number-1)

    def get(self, number):
        return self.__list[number-1]

    def set(self, number, player):
        self.__list[number-1] = player

    def move(self, oldNumber, newNumber):
        player = self.__list.pop(oldNumber - 1)
        self.__list.insert(newNumber - 1, player)

        # Update batOrder after moving the player
        for i, player in enumerate(self.__list, start=1):
            player.batOrder = i

    def update_bat_order(self):
        # Update batOrder after any changes in the lineup
        for i, player in enumerate(self.__list, start=1):
            player.batOrder = i

    def __iter__(self):
        for player in self.__list:
            yield player

def main():
    lineup = Lineup()
    lineup.add(Player(1, "Willie", "Mays", "CF", 100, 31))
    lineup.add(Player(2, "Hank", "Aaron", "RF", 100, 32))

    for player in lineup:
        print(player.batOrder, player.fullName, player.position,
              player.atBats, player.hits, player.battingAvg)

    print("Bye!")

if __name__ == "__main__":
    main()
