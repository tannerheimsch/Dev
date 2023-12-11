# objects.py

class Player:
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.firstName = first_name
        self.lastName = last_name
        self.position = position
        self.atBats = int(at_bats)
        self.hits = int(hits)

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"
    
    @property
    def battingAvg(self):
        if self.atBats == 0:
            return 0.0
        batting_avg = round(self.hits / self.atBats, 3)
        return batting_avg
    
def main():
    pass