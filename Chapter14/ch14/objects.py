from dataclasses import dataclass

@dataclass
class Player:
    firstName:str = ""
    lastName:str = ""
    position:str = ""
    atBats:int = 0
    hits:int = 0

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @property
    def battingAvg(self):
        try:
            avg = self.hits / self.atBats
            return round(avg, 3)
        except ZeroDivisionError:
            return 0.0
       
def main():
    player = Player("Willie", "Mays", "CF", 100, 31)
    print(f"Player: {player.fullName}")
    print(f"Batting Avg: {player.battingAvg}")
    print("Bye!")

if __name__ == "__main__":
    main()
