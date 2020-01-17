class Team(object):

    # Properties for the object
    name = ""
    wins = 0
    losses = 0
    ties = 0
    rosterCount = 0
    points = 0
    rank = 0

    # Initializer Method
    def __init__ (self, name, wins = 0, losses = 0,
        ties = 0, rosterCount = 0, points = 0, rank = 0):

        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.rosterCount = rosterCount
        self.points = points
        self.rank = rank

# Main Tester Method
def main():
    colts = Team("Colts")

    print(colts.name)
    print(colts.wins)

    colts.losses = 23
    print(colts.losses)

if(__name__ == "__main__"):
    main()
