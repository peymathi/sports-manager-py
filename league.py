class League(object):

    name = ""
    sport = ""
    # Private Variables because __numTeams is set by the number of elements in __teamNames
    __numTeams = 0
    __teamNames = [None]
    
    


    #Initializer method does not make default values. NumTeams property and list of strings
    #property are always initialized with default values 0 and an empty list
    def __init__(self, name, s):

        # Set properties for instance.
        self.sport = s
        self.name = name
        self.__numTeams = 0
        self.__teamNames = [None]

    # Getter Method for private vars

    def getNumTeams(self):
        return self.__numTeams

    def getTeamNames(self):
        return self.__teamNames

    """
         Setter Methods for private var __teamNames__. addTeam method appends name to
         __teamNames__ list. removeTeam method tries to find name in __teamNames__.
         Removes it from the list if it finds it and subtracts one from __numTeams__, does
         nothing if name is not in the list  """

    def addTeam(self, name):

        if(self.__teamNames[0] == None):
            self.__teamNames[0] = name
            self.__numTeams += 1

        else:
            self.__teamNames.append(name)
            self.__numTeams += 1

    def removeTeam(self, name):

        try:
            self.__teamNames.remove(name)
            self.__numTeams -= 1

        except:
            pass

    # Object Testing Main Method
def main():
    nfl = League("NFL", "Football")
    another = League("Hi", "Hello")

    nfl.addTeam("Colts")
    another.addTeam("This doesnt make sense")

    print(nfl.getTeamNames())
    print(another.getTeamNames())
    
if(__name__ == "__main__"):
    main()

