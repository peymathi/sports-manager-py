from tkinter import *
import database as dat
from team import Team
from league import League

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        # If creation of an object fails, this is set to false
        self.creationBoo = True

        # If an object is being viewed, this is set to true
        self.objectView = False

        # Global object variable for viewing an object
        self.currentObject = None

        self.string = ""
        self.title("Sport Manager")
        self.headerFont = ("Helvetica", "24", "bold italic")

        # Create a list of all current widgets
        self.currentWidgets = []

        # Run the mainPage
        self.mainPage()

    # Main Page of the app, this will run first
    def mainPage(self):

        self.currentObject = None
        self.objectView = False

        # Set creationBoo to True
        self.creationBoo = True
            
        # Hide all existing widgets if there are any
        for widget in self.currentWidgets:
            widget.grid_forget()

        # Remove all widgets in currentWidgets
        self.currentWidgets = []         

        # Create Header
        mainHeader = Label(self, text = "League / Team Manager", font = self.headerFont)

        # Create a frame to hold all the buttons
        mainFrame = Frame(self, borderwidth = 4, relief = "ridge", padx = 4, pady = 4)

        # Create each button
        toCreateTeam = Button(mainFrame, text = "Create Team", command = self.createTeam)
        toCreateLeague = Button(mainFrame, text = "Create League", command = self.createLeague)
        toViewTeam = Button(mainFrame, text = "View or Change a Team", command = self.viewTeam)
        toViewLeague = Button(mainFrame, text = "View or Change a League", command = self.viewLeague)
        exitApp = Button(mainFrame, text = "Quit", command = self.destroy)

        # Grid each widget and add it to the list of active widgets. This will run everytime the main page is created
        mainHeader.grid()
        self.currentWidgets.append(mainHeader)

        mainFrame.grid()
        self.currentWidgets.append(mainFrame)
        
        toCreateTeam.grid()
        self.currentWidgets.append(toCreateTeam)
        
        toCreateLeague.grid()
        self.currentWidgets.append(toCreateLeague)
        
        toViewTeam.grid()
        self.currentWidgets.append(toViewTeam)
        
        toViewLeague.grid()
        self.currentWidgets.append(toViewLeague)
        
        exitApp.grid()
        self.currentWidgets.append(exitApp)
        
    def createTeam(self):

        # Hide all other active widgets 
        
        for widget in self.currentWidgets:
            widget.grid_forget()

        self.currentWidgets = []
            
        if (not self.creationBoo):
            incorrect = Label(self, text = "You entered some of the information incorrectly. You must enter a name to make a team, and you must enter a number for every other field", foreground = "red")
            incorrect.grid()
            self.currentWidgets.append(incorrect)
        

        # Create the Widgets
        createTeamHeader = Label(self, text = "Create A Team", font = self.headerFont)
        backBtn = Button(self, text = "Main Menu", command = self.mainPage)

        # Description Label
        description = Label(self, text = "Enter the starting values for your new team. You must enter at least a name. All other fields can have 0 or a starting value.")

        # Frame to hold all of the entry and labels
        createTframe = Frame(self, borderwidth = 4, relief = "ridge", padx = 4, pady = 4)
            
        teamNameLbl = Label(createTframe, text = "Team Name: ")
        teamNameTxt = Entry(createTframe)

        winsLbl = Label(createTframe, text = "Wins: ")
        winsTxt = Entry(createTframe)

        lossesLbl = Label(createTframe, text = "Losses: ")
        lossesTxt = Entry(createTframe)

        tiesLbl = Label(createTframe, text = "Ties: ")
        tiesTxt = Entry(createTframe)

        rosterLbl = Label(createTframe, text = "Roster Count: ")
        rosterTxt = Entry(createTframe)

        pointsLbl = Label(createTframe, text = "Points: ")
        pointsTxt = Entry(createTframe)

        rankLbl = Label(createTframe, text = "Rank: ")
        rankTxt = Entry(createTframe)

        submitBtn = Button(self, text = "Create Team", command = self.makeTeam)

        # Grid all the widgets and add to the list of current widgets
        createTeamHeader.grid()
        self.currentWidgets.append(createTeamHeader)
        
        backBtn.grid()
        self.currentWidgets.append(backBtn)
        
        description.grid()
        self.currentWidgets.append(description)

        createTframe.grid()
        self.currentWidgets.append(createTframe)
        
        teamNameLbl.grid(row = 4, column = 0)
        self.currentWidgets.append(teamNameLbl)
        
        teamNameTxt.grid(row = 4, column = 1)
        self.currentWidgets.append(teamNameTxt)

        winsLbl.grid(row = 5, column = 0)
        self.currentWidgets.append(winsLbl)
        
        winsTxt.grid(row = 5, column = 1)
        self.currentWidgets.append(winsTxt)
        
        lossesLbl.grid(row = 6, column = 0)
        self.currentWidgets.append(lossesLbl)
        
        lossesTxt.grid(row = 6, column = 1)
        self.currentWidgets.append(lossesTxt)

        tiesLbl.grid(row = 7, column = 0)
        self.currentWidgets.append(tiesLbl)
        
        tiesTxt.grid(row = 7, column = 1)
        self.currentWidgets.append(tiesTxt)

        rosterLbl.grid(row = 8, column = 0)
        self.currentWidgets.append(rosterLbl)
        
        rosterTxt.grid(row = 8, column = 1)
        self.currentWidgets.append(rosterTxt)

        pointsLbl.grid(row = 9, column = 0)
        self.currentWidgets.append(pointsLbl)
        
        pointsTxt.grid(row = 9, column = 1)
        self.currentWidgets.append(pointsTxt)

        rankLbl.grid(row = 10, column = 0)
        self.currentWidgets.append(rankLbl)
        
        rankTxt.grid(row = 10, column = 1)
        self.currentWidgets.append(rankTxt)

        submitBtn.grid()
        self.currentWidgets.append(submitBtn)

    def createLeague(self):
        
        # Hide all other active widgets
        for widget in self.currentWidgets:
            widget.grid_forget()

        self.currentWidgets = []

        # Check to display the error message
        if (not self.creationBoo):
            incorrect = Label(self, text = "You entered some of the information incorrectly. You must enter the team name, and then put a number for the other fields", foreground = "red")
            incorrect.grid()
            self.currentWidgets.append(incorrect)

        # Create the widgets
        header = Label(self, text = "Create a League", font = self.headerFont)

        backBtn = Button(self, text = "Main Menu", command = self.mainPage)

        description = Label(self, text = "Enter the starting values for your new league. You must have a name and all other fields can have starting values or enter 0.")

        frame = Frame(self, borderwidth = 4, relief = "ridge", padx = 4, pady = 4)

        leagueNameLbl = Label(frame, text = "League Name: ")
        leagueNameTxt = Entry(frame)

        sportLbl = Label(frame, text = "Sport: ")
        sportTxt = Entry(frame)

        submitBtn = Button(self, text = "Make League", command = self.makeLeague)

        # Grid all the widgets and add them to currentWidgets

        header.grid()
        self.currentWidgets.append(header)
        
        backBtn.grid()
        self.currentWidgets.append(backBtn)
        
        description.grid()
        self.currentWidgets.append(description)
        
        frame.grid()
        self.currentWidgets.append(frame)

        leagueNameLbl.grid(row = 4, column = 0)
        self.currentWidgets.append(leagueNameLbl)
        
        leagueNameTxt.grid(row = 4, column = 1)
        self.currentWidgets.append(leagueNameTxt)

        sportLbl.grid(row = 5, column = 0)
        self.currentWidgets.append(sportLbl)
        
        sportTxt.grid(row = 5, column = 1)
        self.currentWidgets.append(sportTxt)

        submitBtn.grid()
        self.currentWidgets.append(submitBtn)

    def viewTeam(self):
        # Hide all other active widgets
        for widget in self.currentWidgets:
            widget.grid_forget()

        self.currentWidgets = []

        # Check to see if error message is needed
        if(not self.creationBoo):
            incorrect = Label(self, text = "Some of the information you entered was incorrect. Try again.", foreground = "red")
            incorrect.grid()
            self.currentWidgets.append(incorrect)
            
        # Create the widgets
        header = Label(self, text = "View / Change Team", font = self.headerFont)

        backBtn = Button(self, text = "Main Menu", command = self.mainPage)

        # Searching for Team Frame
        searchFrame = Frame(self)
        searchLbl = Label(searchFrame, text = "Search for the team you would like to view: ")
        searchTxt = Entry(searchFrame)
        searchBtn = Button(searchFrame, text = "Search", command = self.loadTeam)

        # Changing Team Frame
        changeFrame = Frame(self, borderwidth = 4, padx = 4, pady = 4, relief = "ridge")

        nameLbl = Label(changeFrame, text = "Change Name: ")
        nameTxt = Entry(changeFrame)
        nameBtn = Button(changeFrame, text = "Change", command = self.changeTeamName)

        winsLbl = Label(changeFrame, text = "Change Wins: ")
        winsTxt = Entry(changeFrame)
        winsBtn = Button(changeFrame, text = "Change", command = self.changeWins)

        lossesLbl = Label(changeFrame, text = "Change Losses: ")
        lossesTxt = Entry(changeFrame)
        lossesBtn = Button(changeFrame, text = "Change", command = self.changeLosses)

        tiesLbl = Label(changeFrame, text = "Change Ties: ")
        tiesTxt = Entry(changeFrame)
        tiesBtn = Button(changeFrame, text = "Change", command = self.changeTies)

        rosterLbl = Label(changeFrame, text = "Change Roster Count: ")
        rosterTxt = Entry(changeFrame)
        rosterBtn = Button(changeFrame, text = "Change", command = self.changeRosterCount)

        pointsLbl = Label(changeFrame, text = "Change Points: ")
        pointsTxt = Entry(changeFrame)
        pointsBtn = Button(changeFrame, text = "Change", command = self.changePoints)

        rankLbl = Label(changeFrame, text = "Change Rank: ")
        rankTxt = Entry(changeFrame)
        rankBtn = Button(changeFrame, text = "Change", command = self.changeRank)

        deleteTeamBtn = Button(changeFrame, text = "Delete Team", command = self.deleteTeam)

        # Viewing Team Frame
        viewFrame = Frame(self, borderwidth = 4, padx = 4, pady = 4, relief = "ridge")

        nameConstant = Label(viewFrame, text = "Team Name: ")
        #nameVariable

        winsConstant = Label(viewFrame, text = "Wins: ")
        #winsVariable

        lossesConstant = Label(viewFrame, text = "Losses: ")
        #lossesVariable

        tiesConstant = Label(viewFrame, text = "Ties: ")
        #tiesVariable

        rosterConstant = Label(viewFrame, text = "Roster Count: ")
        #rosterVariable

        pointsConstant = Label(viewFrame, text = "Points: ")
        #pointsVariable

        rankConstant = Label(viewFrame, text = "Rank: ")
        #rankVariable

        if(self.objectView):
            nameVariable = Label(viewFrame, text = self.currentObject.name)
            winsVariable = Label(viewFrame, text = str(self.currentObject.wins))
            lossesVariable = Label(viewFrame, text = str(self.currentObject.losses))
            tiesVariable = Label(viewFrame, text = str(self.currentObject.ties))
            rosterVariable = Label(viewFrame, text = str(self.currentObject.rosterCount))
            pointsVariable = Label(viewFrame, text = str(self.currentObject.points))
            rankVariable = Label(viewFrame, text = str(self.currentObject.rank))

        else:
            nameVariable = Label(viewFrame, text = "N/A")
            winsVariable = Label(viewFrame, text = "N/A")
            lossesVariable = Label(viewFrame, text = "N/A")
            tiesVariable = Label(viewFrame, text = "N/A")
            rosterVariable = Label(viewFrame, text = "N/A")
            pointsVariable = Label(viewFrame, text = "N/A")
            rankVariable = Label(viewFrame, text = "N/A")
        
        # Grid all the widgets and add them to currentWidgets
        header.grid()
        self.currentWidgets.append(header)

        backBtn.grid(sticky = "w")
        self.currentWidgets.append(backBtn)

        # Search Frame
        searchFrame.grid()
        self.currentWidgets.append(searchFrame)

        searchLbl.grid()
        self.currentWidgets.append(searchLbl)

        searchTxt.grid()
        self.currentWidgets.append(searchTxt)

        searchBtn.grid()
        self.currentWidgets.append(searchBtn)

        # Change Frame
        changeFrame.grid()
        self.currentWidgets.append(changeFrame)

        nameLbl.grid(row = 6, column = 0)
        self.currentWidgets.append(nameLbl)

        nameTxt.grid(row = 6, column = 1)
        self.currentWidgets.append(nameTxt)

        nameBtn.grid(row = 6, column = 2)
        self.currentWidgets.append(nameBtn)

        winsLbl.grid(row = 6, column = 4)
        self.currentWidgets.append(winsLbl)

        winsTxt.grid(row = 6, column = 5)
        self.currentWidgets.append(winsTxt)

        winsBtn.grid(row = 6, column = 6)
        self.currentWidgets.append(winsBtn)

        lossesLbl.grid(row = 6, column = 8)
        self.currentWidgets.append(lossesLbl)

        lossesTxt.grid(row = 6, column = 9)
        self.currentWidgets.append(lossesTxt)

        lossesBtn.grid(row = 6, column = 10)
        self.currentWidgets.append(lossesBtn)

        tiesLbl.grid(row = 7, column = 0)
        self.currentWidgets.append(tiesLbl)

        tiesTxt.grid(row = 7, column = 1)
        self.currentWidgets.append(tiesTxt)

        tiesBtn.grid(row = 7, column = 2)
        self.currentWidgets.append(tiesBtn)

        rosterLbl.grid(row = 7, column = 4)
        self.currentWidgets.append(rosterLbl)

        rosterTxt.grid(row = 7, column = 5)
        self.currentWidgets.append(rosterTxt)

        rosterBtn.grid(row = 7, column = 6)
        self.currentWidgets.append(rosterBtn)

        pointsLbl.grid(row = 7, column = 8)
        self.currentWidgets.append(pointsLbl)

        pointsTxt.grid(row = 7, column = 9)
        self.currentWidgets.append(pointsTxt)

        pointsBtn.grid(row = 7, column = 10)
        self.currentWidgets.append(pointsBtn)

        rankLbl.grid(row = 7, column = 12)
        self.currentWidgets.append(rankLbl)

        rankTxt.grid(row = 7, column = 13)
        self.currentWidgets.append(rankTxt)

        rankBtn.grid(row = 7, column = 14)
        self.currentWidgets.append(rankBtn)

        deleteTeamBtn.grid()
        self.currentWidgets.append(deleteTeamBtn)

        # View Frame
        viewFrame.grid()
        self.currentWidgets.append(viewFrame)

        nameConstant.grid(row = 9, column = 0)
        self.currentWidgets.append(nameConstant)

        nameVariable.grid(row = 9, column = 1)
        self.currentWidgets.append(nameVariable)

        winsConstant.grid(row = 10, column = 0)
        self.currentWidgets.append(winsConstant)

        winsVariable.grid(row = 10, column = 1)
        self.currentWidgets.append(winsVariable)

        lossesConstant.grid(row = 11, column = 0)
        self.currentWidgets.append(lossesConstant)

        lossesVariable.grid(row = 11, column = 1)
        self.currentWidgets.append(lossesVariable)

        tiesConstant.grid(row = 12, column = 0)
        self.currentWidgets.append(tiesConstant)

        tiesVariable.grid(row = 12, column = 1)
        self.currentWidgets.append(tiesVariable)

        rosterConstant.grid(row = 13, column = 0)
        self.currentWidgets.append(rosterConstant)

        rosterVariable.grid(row = 13, column = 1)
        self.currentWidgets.append(rosterVariable)

        pointsConstant.grid(row = 14, column = 0)
        self.currentWidgets.append(pointsConstant)

        pointsVariable.grid(row = 14, column = 1)
        self.currentWidgets.append(pointsVariable)

        rankConstant.grid(row = 15, column = 0)
        self.currentWidgets.append(rankConstant)

        rankVariable.grid(row = 15, column = 1)
        self.currentWidgets.append(rankVariable)


    # Method for loading a team object
    def loadTeam(self):

        # Find out which indices are good
        if(not self.creationBoo):
                
            # Try to find the object
            try:
                self.currentObject = dat.loadTeam(self.currentWidgets[5].get())
                self.objectView = True
                self.creationBoo = True
                self.viewTeam()

            except:
                self.creationBoo = False
                self.viewTeam()

        # Exact same with adjusted indices
        else:

            try:
                self.currentObject = dat.loadTeam(self.currentWidgets[4].get())
                self.objectView = True
                self.creationBoo = True
                self.viewTeam()


            except:
                self.creationBoo = False
                self.viewTeam()

    # Method for changing name of a team object
    def changeTeamName(self):

        if(not self.objectView):
            self.viewTeam()

        else:

            # Find out which indices are good
            if(not self.creationBoo):
                if(self.currentWidgets[9].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                else:

                    dat.removeTeam(self.currentObject.name)
                    self.currentObject.name = self.currentWidgets[9].get()
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

            # Exact same with adjusted indices
            else:
                if(self.currentWidgets[8].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()
                    
                else:

                    dat.removeTeam(self.currentObject.name)
                    self.currentObject.name = self.currentWidgets[8].get()
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()
            

    # Method for changing wins of a team object, very similar to all other change property functions
    def changeWins(self):

        if(not self.objectView):
            self.viewTeam()

        else:

            if(not self.creationBoo):
                if(self.currentWidgets[12].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.wins = int(self.currentWidgets[12].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

            else:
                if(self.currentWidgets[11].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.wins = int(self.currentWidgets[11].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()
            
    
    # Method for changing losses of a team object. Very similar to all other change property functions. Same for below.
    def changeLosses(self):
        if(not self.objectView):
            self.viewTeam()
            
        else:

            if(not self.creationBoo):
                if(self.currentWidgets[15].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.losses = int(self.currentWidgets[15].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

            else:
                if(self.currentWidgets[14].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.losses = int(self.currentWidgets[14].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

    # Mehtod for changing ties of a team object
    def changeTies(self):
        if(not self.objectView):
            self.viewTeam()

        else:

            if(not self.creationBoo):
                if(self.currentWidgets[18].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.ties = int(self.currentWidgets[18].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

            else:
                if(self.currentWidgets[17].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.ties = int(self.currentWidgets[17].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()
    
    # Method for changing rosterCount of a team object
    def changeRosterCount(self):
        if(not self.objectView):
            self.viewTeam()

        else:

            if(not self.creationBoo):
                if(self.currentWidgets[21].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.rosterCount = int(self.currentWidgets[21].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

            else:
                if(self.currentWidgets[20].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.rosterCount = int(self.currentWidgets[20].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

    # Method for changing points of a team object
    def changePoints(self):
        if(not self.objectView):
            self.viewTeam()

        else:

            if(not self.creationBoo):
                if(self.currentWidgets[24].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.points = int(self.currentWidgets[24].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

            else:
                if(self.currentWidgets[23].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.points = int(self.currentWidgets[23].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

    # Method for changing rank of a team object
    def changeRank(self):
        if(not self.objectView):
            self.viewTeam()

        else:

            if(not self.creationBoo):
                if(self.currentWidgets[27].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()
    
                try:
                    self.currentObject.rank = int(self.currentWidgets[27].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()

            else:
                if(self.currentWidgets[26].get() == ""):
                    self.creationBoo = False
                    self.viewTeam()

                try:
                    self.currentObject.rank = int(self.currentWidgets[26].get())
                    dat.removeTeam(self.currentObject.name)
                    dat.saveTeam(self.currentObject)
                    self.creationBoo = True
                    self.viewTeam()

                except:
                    self.creationBoo = False
                    self.viewTeam()
    
    # Method for deleting a team object
    def deleteTeam(self):
        if(not self.objectView):
            self.viewTeam()
            
        else:

            dat.removeTeam(self.currentObject.name)
            self.objectView = False
            self.creationBoo = True
            self.viewTeam()
    
    def viewLeague(self):
        # Hide all other active widgets
        for widget in self.currentWidgets:
            widget.grid_forget()

        self.currentWidgets = []

        if(not self.creationBoo):
            incorrect = Label(self, text = "Some of the information you entered was incorrect. Try again.", foreground = "red")
            incorrect.grid()
            self.currentWidgets.append(incorrect)

        # Create the widgets
        header = Label(self, text = "View / Change a League", font = self.headerFont)
        backBtn = Button(self, text = "Main Menu", command = self.mainPage)

        # Search Frame
        searchFrame = Frame(self, borderwidth = 4, padx = 4, pady = 4)
        searchLbl = Label(searchFrame, text = "Search for a League: ")
        searchTxt = Entry(searchFrame)
        searchBtn = Button(searchFrame, text = "Search", command = self.loadLeague)

        # Change Frame
        changeFrame = Frame(self, borderwidth = 4, padx = 4, pady = 4, relief = "ridge")

        changeNameLbl = Label(changeFrame, text = "Change League Name: ")
        changeNameTxt = Entry(changeFrame)
        changeNameBtn = Button(changeFrame, text = "Change", command = self.changeLeagueName)

        changeSportLbl = Label(changeFrame, text = "Change Sport: ")
        changeSportTxt = Entry(changeFrame)
        changeSportBtn = Button(changeFrame, text = "Change", command = self.changeSport)

        addTeamLbl = Label(changeFrame, text = "Add a Team: ")
        addTeamTxt = Entry(changeFrame)
        addTeamBtn = Button(changeFrame, text = "Add", command = self.addTeamToLeague)

        delLeagueBtn = Button(changeFrame, text = "Delete League", command = self.delLeague)

        # View Frame
        viewFrame = Frame(self, borderwidth = 4, padx = 4, pady = 4, relief = "ridge")

        nameConstant = Label(viewFrame, text = "League Name: ")
        #nameVar

        sportConstant = Label(viewFrame, text = "Sport: ")
        #sportVar

        teamsConstant = Label(viewFrame, text = "Teams in the League: ")
        #teams labels

        numTeamsConstant = Label(viewFrame, text = "Number of Teams: ")
        #numTeamsVar


        # If the object is being displayed, show the value, if not, show N/A
        if(self.objectView):
            nameVar = Label(viewFrame, text = self.currentObject.name)
            sportVar = Label(viewFrame, text = self.currentObject.sport)
            numTeamsVar = Label(viewFrame, text = self.currentObject.getNumTeams())

        else:
            nameVar = Label(viewFrame, text = "N/A")
            sportVar = Label(viewFrame, text = "N/A")
            numTeamsVar = Label(viewFrame, text = "N/A")
            teamsVar = Label(viewFrame, text = "N/A")
        

        # Grid all the widgets and add them to currentWidgets
        header.grid()
        self.currentWidgets.append(header)

        backBtn.grid(sticky = "w")
        self.currentWidgets.append(backBtn)

        # Search Frame
        searchFrame.grid()
        self.currentWidgets.append(searchFrame)

        searchLbl.grid()
        self.currentWidgets.append(searchLbl)

        searchTxt.grid()
        self.currentWidgets.append(searchTxt)

        searchBtn.grid()
        self.currentWidgets.append(searchBtn)
        
        # Change Frame
        changeFrame.grid(row = 6, column = 0)
        self.currentWidgets.append(changeFrame)

        changeNameLbl.grid(row = 6, column = 1)
        self.currentWidgets.append(changeNameLbl)

        changeNameTxt.grid(row = 6, column = 2)
        self.currentWidgets.append(changeNameTxt)

        changeNameBtn.grid(row = 6, column = 4)
        self.currentWidgets.append(changeNameBtn)

        changeSportLbl.grid(row = 6, column = 5)
        self.currentWidgets.append(changeSportLbl)

        changeSportTxt.grid(row = 6, column = 6)
        self.currentWidgets.append(changeSportTxt)

        changeSportBtn.grid(row = 6, column = 7)
        self.currentWidgets.append(changeSportBtn)

        addTeamLbl.grid(row = 6, column = 9)
        self.currentWidgets.append(addTeamLbl)

        addTeamTxt.grid(row = 6, column = 10)
        self.currentWidgets.append(addTeamTxt)

        addTeamBtn.grid(row = 6, column = 11)
        self.currentWidgets.append(addTeamBtn)

        delLeagueBtn.grid(row = 7)
        self.currentWidgets.append(delLeagueBtn)

        # View Frame
        viewFrame.grid()
        self.currentWidgets.append(viewFrame)

        nameConstant.grid(row = 8, column = 0)
        self.currentWidgets.append(nameConstant)

        nameVar.grid(row = 8, column = 1)
        self.currentWidgets.append(nameVar)

        sportConstant.grid(row = 9, column = 0)
        self.currentWidgets.append(sportConstant)

        sportVar.grid(row = 9, column = 1)
        self.currentWidgets.append(sportVar)

        numTeamsConstant.grid(row = 10, column = 0)
        self.currentWidgets.append(numTeamsConstant)

        numTeamsVar.grid(row = 10, column = 1)
        self.currentWidgets.append(numTeamsVar)

        teamsConstant.grid(row = 11, column = 0)
        self.currentWidgets.append(teamsConstant)

        teams = ""

        # If the object is being displayed, display the value
        if(self.objectView and not (self.currentObject.getTeamNames() == [None] or self.currentObject.getTeamNames() == [])):
            for i in range(len(self.currentObject.getTeamNames())):
                teams += self.currentObject.getTeamNames()[i] + ", "

            teams = teams.rstrip(', ')
            teamsVar = Label(viewFrame, text = teams)
            teamsVar.grid(row = 11, column = 1)
            self.currentWidgets.append(teamsVar)

        elif(self.objectView):
            teamsVar = Label(viewFrame, text = "None")
            teamsVar.grid(row = 11, column = 1)
            self.currentWidgets.append(teamsVar)
        
        else:
            teamsVar.grid(row = 11, column = 1)

    # Function to load a league, exactly like load team
    def loadLeague(self):
        # Find out which indices are good
        if(not self.creationBoo):
            if(self.currentWidgets[5].get() == ""):
                self.creationBoo = False
                self.viewLeague()

            try:
                self.currentObject = dat.loadLeague(self.currentWidgets[5].get())
                self.objectView = True
                self.creationBoo = True
                self.viewLeague()

            except:
                self.creationBoo = False
                self.viewLeague()

        else:
            if(self.currentWidgets[4].get() == ""):
                self.creationBoo = False
                self.viewLeague()

            try:
                self.currentObject = dat.loadLeague(self.currentWidgets[4].get())
                self.objectView = True
                self.creationBoo = True
                self.viewLeague()

            except:
                self.creationBoo = False
                self.viewLeague()
        

    # Function to change league name, very similar to the function for changing team attributes. Same for all below EXCEEPT addTeam because it changes a list attribute
    def changeLeagueName(self):
        if(not self.objectView):
            self.viewLeague()

        else:

            if(not self.creationBoo):
                self.currentWidgets[9].grid()
                if(self.currentWidgets[9].get() == ""):
                    self.creationBoo = False
                    self.viewLeague()

                else:

                    dat.removeLeague(self.currentObject.name)
                    self.currentObject.name = self.currentWidgets[9].get()
                    dat.saveLeague(self.currentObject)
                    self.creationBoo = True
                    self.viewLeague()

            else:
                if(self.currentWidgets[8].get() == ""):
                    self.creationBoo = False
                    self.viewLeague()
                
                else:
                    dat.removeLeague(self.currentObject.name)
                    self.currentObject.name = (self.currentWidgets[8].get())
                    dat.saveLeague(self.currentObject)
                    self.creationBoo = True
                    self.viewLeague()

    # Function to change sport
    def changeSport(self):
        if(not self.objectView):
            self.viewLeague()

        else:

            if(not self.creationBoo):
                if(self.currentWidgets[12].get() == ""):
                    self.creationBoo = False
                    self.viewLeague()
                
                else:
                
                    dat.removeLeague(self.currentObject.name)
                    self.currentObject.sport = self.currentWidgets[12].get()
                    dat.saveLeague(self.currentObject)
                    self.creationBoo = True
                    self.viewLeague()

            else:
                if(self.currentWidgets[11].get() == ""):
                    self.creationBoo = False
                    self.viewLeague()

                else:

                    dat.removeLeague(self.currentObject.name)
                    self.currentObject.sport = self.currentWidgets[11].get()
                    dat.saveLeague(self.currentObject)
                    self.creationBoo = True
                    self.viewLeague()
    
    # Function to add a team to the league
    def addTeamToLeague(self):
        if(not self.objectView):
            self.viewLeague()
            
        else:

            if(not self.creationBoo):
                if(self.currentWidgets[15].get() == ""):
                    self.creationBoo = False
                    self.viewLeague()
                
                else:
                    dat.removeLeague(self.currentObject.name)
                    self.currentObject.addTeam(self.currentWidgets[15].get())
                    dat.saveLeague(self.currentObject)
                    self.creationBoo = True
                    self.viewLeague()

            else:
                if(self.currentWidgets[14].get() == ""):
                    self.creationBoo = False
                    self.viewLeague()

                else:

                    dat.removeLeague(self.currentObject.name)
                    self.currentObject.addTeam(self.currentWidgets[14].get())
                    dat.saveLeague(self.currentObject)
                    self.creationBoo = True
                    self.viewLeague()
    
    # Function to a delete a league
    def delLeague(self):
        if(not self.objectView):
            self.viewLeague()

        else:
            
            dat.removeLeague(self.currentObject.name)
            self.currentObject = None
            self.objectView = False
            self.creationBoo = True
            self.viewLeague()
    
    # Function for making a new team object and storing it
    def makeTeam(self):
        
        fieldsFilled = False
        # Check to see if all the fields were filled out.
        # Correct indices for incorrect label
        if(not self.creationBoo):
            if(not self.currentWidgets[6].get() == ""):
                if(not self.currentWidgets[8].get() == ""):
                    if(not self.currentWidgets[10].get() == ""):
                        if(not self.currentWidgets[12].get() == ""):
                            if(not self.currentWidgets [14].get() == ""):
                                if(not self.currentWidgets[16].get() == ""):
                                    if(not self.currentWidgets[18].get() == ""):
                                        fieldsFilled = True

            if(fieldsFilled):
                # Create the team, save it, and send the user to viewTeam page. And set creationBoo to True
                self.creationBoo = True
                team = Team(self.currentWidgets[6].get(), self.currentWidgets[8].get(), self.currentWidgets[10].get(), self.currentWidgets[12].get(),
                            self.currentWidgets[14].get(), self.currentWidgets[16].get(), self.currentWidgets[18].get())
                
                dat.saveTeam(team)
                self.currentObject = team
                self.creationBoo = True
                self.objectView = True
                self.viewTeam()

            else:
                # Deny the user, and send them back to createTeam with error message
                self.creationBoo = False
                self.createTeam()
                
        else:
            if(not self.currentWidgets[5].get() == ""):
                if(not self.currentWidgets[7].get() == ""):
                    if(not self.currentWidgets[9].get() == ""):
                        if(not self.currentWidgets[11].get() == ""):
                            if(not self.currentWidgets [13].get() == ""):
                                if(not self.currentWidgets[15].get() == ""):
                                    if(not self.currentWidgets[17].get() == ""):
                                        fieldsFilled = True

            if(fieldsFilled):
                # Create the team, save it, and send the user to viewTeam page. And set creationBoo to True
                self.creationBoo = True
                team = Team(self.currentWidgets[5].get(), self.currentWidgets[7].get(), self.currentWidgets[9].get(),
                            self.currentWidgets[11].get(), self.currentWidgets[13].get(), self.currentWidgets[15].get(), self.currentWidgets[17].get())
                
                dat.saveTeam(team)
                self.currentObject = team
                self.creationBoo = True
                self.objectView = True
                self.viewTeam()

            else:
                # Deny the user, and send them back to createTeam with error message
                self.creationBoo = False
                self.createTeam()
        
    # Function for making a new league object and storing it
    def makeLeague(self):
        
        fieldsFilled = False
        # Check to see if all the fields were filled out
        # Correct indices for incorrect label
        if(not self.creationBoo):
            if(not self.currentWidgets[6].get() == ""):
                if(not self.currentWidgets[8].get() == ""):
                    fieldsFilled = True
                    
            if(fieldsFilled):
                # Make the league object, save it, send the user to the viewLeague page, and set creationBoo to True
                league = League(self.currentWidgets[6].get(), self.currentWidgets[8].get())
                dat.saveLeague(league)
                self.creationBoo = True
                self.currentObject = league
                self.objectView = True
                self.viewLeague()

            else:
                # Deny the user, and send them back to createTeam with the error message.
                self.creationBoo = False
                self.createLeague()

        else:
            if(not self.currentWidgets[5].get() == ""):
                if(not self.currentWidgets[7].get() == ""):
                    fieldsFilled = True

            if(fieldsFilled):
                # Make the league object, save it, send the user to the viewLeague page, and set creationBoo to True
                self.creationBoo = True
                league = League(self.currentWidgets[5].get(), self.currentWidgets[7].get())
                dat.saveLeague(league)
                self.currentObject = league
                self.objectView = True
                self.viewLeague()

            else:
                # Deny the user, and send them back to createTeam with the error message
                self.creationBoo = False
                self.createLeague()

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
    
