import pickle, os
from team import Team
from league import League

# Function that adds a new team object to the teamObj list and saves it to teamobjects.dat. Parameter is a team object.
def saveTeam(team):
    # Check to see if the file exists, create array and a file if it doesn't
    # If it does exist, update it with the new team obj
    if(os.path.isfile("teamobjects.dat")):
        file = open("teamobjects.dat", "rb")
        teamObj = pickle.load(file)
        file.close()
        file = open("teamobjects.dat", "wb")
        teamObj.append(team)
        pickle.dump(teamObj, file)
        file.close()

    else:
        teamObj = [team]
        file = open("teamobjects.dat", "wb")
        pickle.dump(teamObj, file)
        file.close()

# Function that removes a team object from the teamObj list and resaves the teamobjects.dat file. Parameter is a string for the name property of the team object
def removeTeam(team):
    # Open the file reading binary
    file = open("teamobjects.dat", "rb")

    # Use pickle.load to get the teamObj list
    teamObj = pickle.load(file)

    # Close the file
    file.close()

    # Open file to write over teamobjects.dat using "wb"
    file = open("teamobjects.dat", "wb")

    # Use for loop to iterate through teamObj list to find the team name property matching the team string and remove that league object from the list
    for i in range(len(teamObj)):
        if(teamObj[i].name == team):
            del teamObj[i]
            break

    # Dump teamObj to the file
    pickle.dump(teamObj, file)

    # Close the file
    file.close()
    

""" Function that attempts to load the data for a team object.
    Parameter is a string for the name property of the team object Returns the teamObj.
    Exception handling is not utilized in this function if the team object does not exist,
    Exception handling must be used where this function is called """
def loadTeam(team):
    # Load file teamobjects.dat in "rb" mode
    file = open("teamobjects.dat", "rb")

    # Use pickle.load to store data to teamObj list
    teamObj = pickle.load(file)

    # Find the team object matching the name of team
    # Save this object to a new variable
    for i in range(len(teamObj)):
        if(team == teamObj[i].name):
            resultTeam = teamObj[i]
            break

    # Close the file
    file.close()

    # Return the object
    return resultTeam

# Function that adds a new league object to the leagueObj list and saves it to leagueobjects.dat. Parameter is a league object
def saveLeague(league):
    # Check to see if the file exists, create array and a file if it doesn't
    # If it does exist, update it with the new league obj
    if(os.path.isfile("leagueobjects.dat")):
        file = open("leagueobjects.dat", "rb")
        leagueObj = pickle.load(file)
        file.close()
        file = open("leagueobjects.dat", "wb")
        leagueObj.append(league)
        pickle.dump(leagueObj, file)
        file.close()

    else:
        leagueObj = [league]
        file = open("leagueobjects.dat", "wb")
        pickle.dump(leagueObj, file)
        file.close()

# Function that removes a league object from the leagueObj list and saves the new leagueObj list back to leagueobjects.dat. Parameter is a string of the league name
def removeLeague(league):
    # Open the file reading binary
    file = open("leagueobjects.dat", "rb")

    # Use pickle.load to get the leagueObj list
    leagueObj = pickle.load(file)

    # Close the file
    file.close()

    # Open file to write over teamobjects.dat using "wb"
    file = open("leagueobjects.dat", "wb")

    # Use for loop to iterate through leagueObj list to find the league name property matching the league string and remove that league object from the list
    for i in range(len(leagueObj)):
        if(leagueObj[i].name == league):
            del leagueObj[i]
            break

    # Dump teamObj to the file
    pickle.dump(leagueObj, file)

    # Close the file
    file.close()

""" Function that attempts to load the data for a league object. Returns the leagueObj.
    Parameter is a string for the league objects name property
    Exception handling is not utilized in this function if the team object does not exist,
    Exception handling must be used where this function is called """

def loadLeague(league):
    # Load file leagueobjects.dat in "rb" mode
    file = open("leagueobjects.dat", "rb")

    # Use pickle.load to store data to leagueObj list
    leagueObj = pickle.load(file)

    # Find the league object matching the name of league
    # Save this object to a new variable
    for i in range(len(leagueObj)):
        if(league == leagueObj[i].name):
            resultLeague = leagueObj[i]
            break

    # Close the file
    file.close()

    # Return the object
    return resultLeague

# Main Function that only runs if namespace is main. Creates a temporary data file to test the functions above and then deletes them. Do not run this after database.py module is completed.
def main():
    newTeam = Team("Colts")
    newLeague = League("NFL", "Football")
    anotherTeam = Team("Steelers")
    anotherLeague = League("MLS", "Soccer")

    #saveLeague(newLeague)
    #saveLeague(anotherLeague)

    #removeLeague(newLeague.name)
    newLeague.addTeam("Colts")
    #saveLeague(newLeague)

    
    #removeLeague(anotherLeague.name)
    anotherLeague.addTeam("LA Galaxy")
    #saveLeague(anotherLeague)

    print(newLeague.getTeamNames())

    

if (__name__ == "__main__"):
    main()
