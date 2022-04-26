# import everything from tkinter module
import tkinter as tk
from tkinter import *
import datetime
import matplotlib.pyplot as plt
#Time Stuff


#User1: Interested in electrical engineering (Shows ISE and CMDA)
#User2: Interested in industrial design (Shows all school of architecture)
#User3: Intersted in Business Managment (Shows BIT) (ADD INDUSTRIAL AND SYSTEM ENGINEERING URL)
cookieFiles = [ {'url': ["https://ece.vt.edu/undergrad/prospective.html", "https://ece.vt.edu/"], 'pageCount': [10, 20], 'timeOnPage': [1000.50, 500.82]}, 
                {'url': ["https://www.ais.science.vt.edu/academics/cmda.html", "https://archdesign.caus.vt.edu/ids/admissions/", "https://archdesign.caus.vt.edu/news/calhoun-discovery-program/"], 'pageCount': [10, 20, 30], 'timeOnPage': [1123.12, 534.66, 1224.98]}, 
                {'url': ["https://management.pamplin.vt.edu/", "https://www.ise.vt.edu/academics/undergrad.htmlv.html"], 'pageCount': [100, 150], 'timeOnPage': [1235.5, 520.24]}]

#url:String 
### Creates keywords to group
#pageCount:int
### Popularity of the pages
#timeOnPage:float (milliseconds)
### Interest level (if they really are reading or if they just leave)

#used to gather data while their on the website
arch = [{'type': "Engineering",     'count': 0, 'time': 0},
        {'type': "Urban Design",    'count': 0, 'time': 0},
        {'type': "Business",        'count': 0, 'time': 0}]
#Use count as overall determine what content should be greatly suggested (2)
#Use time to break ties
#Use combo to override count if they are starting to get interested i one area
#Have the feature that their last clicked it shown as the third option even if it's not the dominant trait
keywords = {'Engineering' : ["ece", "electrical", "computer", "ise", "industrial", "systems", "cmda", "science"],
            'Urban Design' : ["ids", "caus", "design", "enviromental", "sustainable", "spia", "sova", "industrial"],
            'Business': ["pamplin", "management", "bit", "liberalarts", "business"]}

#STEPS:
#STEP 1: Select a cookie file based on the user click of a button (Done)
#STEP 2: Create a createArchtype method to choose the starting arch based of the cookiefile (Done)
    #STEP 2.5: This will require creating a list of keywords, stripping the url to find these keywords, 
    # using time on page a measure to break choose between two archytpes, and figure out a use for page count (could just be analytics)
#STEP 3: Create varible that is a list of the current archtype
#STEP 4: Have a way to increment the count variable in the arch dictionary based off which button the user pressed 
# and updates the time after each press
#STEP 5: Change the text and/or color of the first two buttons based on the current archtype 
#STEP 6: The real hard part will be the escape sequence
    #STEP 6.1: Create a combo feature that switches a user's arch if they choose a specific button twice
    #STEP 6.2: Make it so that randomly (Ever three presses), it will show the least dominiant arch as an option

#LAST STEP: Create a visualization to appear after the exits the GUI based off that user's action (or whenever the user requests it with a button)

#Declares the variable for the application
userFile = {}
button1 = {}
button2 = {}
button3 = {}
lastButton = {}
startTime = datetime.datetime
switchArch = 0
enterArch = ""
exitArch  = ""

window = Tk()
window.geometry('520x420')
window.title("Customer Branding")
def open_popup(file):
    global arch
    arch = [{'type': "Engineering",     'count': 0, 'time': 0.0},
        {'type': "Urban Design",    'count': 0, 'time': 0.0},
        {'type': "Business",        'count': 0, 'time': 0.0}]
    
    userFile = file

    top = Toplevel(window)
    top.geometry("450x320")
    top.title("Cookie File")
    Label(top, text="User's Cookie File", font=("Times New Roman", 12)).pack()
    Label(top, text="Session History", font=("Times New Roman", 12)).pack()
    list = file['url']
    for i in list:
        Label(top, text=i, font=("Times New Roman", 12)).pack()        
    Label(top, text="Page Count", font=("Times New Roman", 12)).pack()
    list = file['pageCount']
    for i in list:
        Label(top, text=i, font=("Times New Roman", 12)).pack()        
    Label(top, text="Time on Page", font=("Times New Roman", 12)).pack()
    list = file['timeOnPage']
    for i in list:
        Label(top, text=i, font=("Times New Roman", 12)).pack()
    createArch(userFile)


currentArch = {}
def createArch(file):
    global currentArch, enterArch
    URLS = file['url']
    TIME =  file["timeOnPage"]

    ENG, UD, BUS = False, False, False
    timeENG, timeUD, timeBUS = 0.0, 0.0, 0.0

    for key in keywords["Engineering"]:
        for count,i in enumerate(URLS):
            if key in i:
                ENG = True
                if TIME[count] > timeENG:
                    timeENG = TIME[count]


    for key in keywords["Urban Design"]:
        for count,i in enumerate(URLS):
            if key in i:
                UD = True
                if TIME[count] > timeUD:
                    timeUD = TIME[count]
    for key in keywords["Business"]:
        for count,i in enumerate(URLS):
            if key in i:
                BUS = True
                if TIME[count] > timeBUS:
                    timeBUS = TIME[count]
    
    if ENG and not UD and not BUS:
        currentArch = arch[0]
    elif UD and not ENG and not BUS:
        currentArch = arch[1]
    elif BUS and not ENG and not UD:
        currentArch = arch[2]
    elif ENG and UD and not BUS:
        if timeENG > timeUD:
            currentArch = arch[0]
        else:
            currentArch = arch[1]
    elif ENG and BUS and not UD:
        if timeENG > timeBUS:
            currentArch = arch[0]
        else:
            currentArch = arch[2]
    #Can add the different cases later for robustness
    createButtons()
    handleButton()
    for i,types in enumerate(arch):
        if types["type"] == currentArch["type"]:
            arch[i]["count"] += 1 #Stores the count
    enterArch = currentArch["type"]



def createButtons():
    global buttonENG, buttonUD, buttonBUS, button1, button2, button3

    #Create button 1 with type Engineering, text "Eng", color red
    buttonENG = {'type': "Engineering", 'text': "ENG", 'color': "#477797"}
    #Create button 2 with type Urban Design, text UD, color Green
    buttonUD = {'type': "Urban Design", 'text': "UD", 'color': "#77c6fc"}
    #Create button 3 with type Business, text Bus, color blue
    buttonBUS = {'type': "Business", 'text': "BUS", 'color': "#ddf1fe"}
    if currentArch == arch[0]:
        #Create button 1 with type Engineering, text "Eng", color red
        button1 = buttonENG
        #Create button 2 with type Urban Design, text UD, color Green
        button2 = buttonBUS
        #Create button 3 with type Business, text Bus, color blue
        button3 = buttonUD
    elif currentArch == arch[1]:
        #Create button 1 with type Engineering, text "Eng", color red
        button2 = buttonENG
        #Create button 2 with type Urban Design, text UD, color Green
        button1 = buttonUD
        #Create button 3 with type Business, text Bus, color blue
        button3 = buttonBUS
    elif currentArch == arch[2]:
        #Create button 1 with type Engineering, text "Eng", color red
        button3 = buttonENG
        #Create button 2 with type Urban Design, text UD, color Green
        button2 = buttonUD
        #Create button 3 with type Business, text Bus, color blue
        button1 = buttonBUS
    

def handleButton(currentButton={}):
    global buttonENG, buttonUD, buttonBUS, button1, button2, button3, lastButton, startTime, endTime, switchArch, currentArch
    if currentButton == {}:
        opt1.configure(text = button1["text"])
        opt2.configure(text = button1["text"])
        opt3.configure(text = button2["text"])
        opt4.configure(text = button3["text"])
        startTime = datetime.datetime.now()
        lastButton = button1;
        #Start time
    else:
        endTime = datetime.datetime.now()
        delta = endTime - startTime
        timeDifference = int(delta.total_seconds() * 1000)
        #store time date
        for i,types in enumerate(arch):
            if types["type"] == currentArch["type"]:
                arch[i]["time"] += timeDifference 
        #increment and store count data
        for i,types in enumerate(arch):
            if types["type"] == currentButton["type"]:
                arch[i]["count"] += 1

            
        countENG, countUD, countBUS = arch[0]["count"], arch[1]["count"], arch[2]["count"]
        totalClicks = countENG + countUD + countBUS
        percENG, percUD, percBUS = countENG/totalClicks, countUD/totalClicks, countBUS/totalClicks
        timeENG, timeUD, timeBUS = arch[0]["time"], arch[1]["time"], arch[2]["time"]
        
        #Changes the canvas color based on what button was pressed
        if currentButton == button1:
            canvas.configure(bg = button1["color"])
        elif currentButton == button2:
            canvas.configure(bg = button2["color"])
        elif currentButton == button3:
            canvas.configure(bg = button3["color"])

        if(lastButton == currentButton and currentButton != button1):
            streak = True
        else:
            streak = False
        
        lastButton = currentButton
        oldButton1 = button1
        #Changes what the buttons
        #STAGE 1: FIRST CLICK TESTING
        if(totalClicks==2):
            if currentButton["type"] == "Engineering":
                button1 = buttonENG
                button2 = buttonBUS
                button3 = buttonUD
            elif currentButton["type"] == "Business":
                button1 = buttonBUS
                button2 = buttonUD
                button3 = buttonENG
            elif currentButton["type"] == "Urban Design":
                button1 = buttonUD
                button2 = buttonENG
                button3 = buttonBUS
        elif(totalClicks > 2 and totalClicks <= 6):
            if countENG > countUD and countENG > countBUS:
                button1 = buttonENG
                button2 = buttonBUS
                button3 = buttonUD
            elif countUD > countENG and countUD > countBUS:
                button1 = buttonUD
                button2 = buttonENG
                button3 = buttonBUS
            elif countBUS > countENG and countBUS > countUD:
                button1 = buttonBUS
                button2 = buttonUD
                button3 = buttonENG
            else:
                if countENG == countUD and countENG > countBUS:
                    if timeENG > timeUD:
                        button1 = buttonENG
                        button2 = buttonBUS
                        button3 = buttonUD
                    else:
                        button1 = buttonUD
                        button2 = buttonENG
                        button3 = buttonBUS
                elif countENG == countBUS and countBUS > countUD:
                    if timeENG > timeBUS:
                        button1 = buttonENG
                        button2 = buttonBUS
                        button3 = buttonUD
                    else:
                        button1 = buttonBUS
                        button2 = buttonUD
                        button3 = buttonENG
                elif countUD == countBUS and countUD > countENG:
                    if timeUD > timeBUS:
                        button1 = buttonUD
                        button2 = buttonENG
                        button3 = buttonBUS
                    else:
                        button1 = buttonBUS
                        button2 = buttonUD
                        button3 = buttonENG
                elif countUD == countBUS  and countENG == countUD:
                    if timeENG > timeBUS and timeENG > timeUD:
                        button1 = buttonENG
                        button2 = buttonBUS
                        button3 = buttonUD
                    elif timeUD > timeENG and timeUD > timeBUS:
                        button1 = buttonUD
                        button2 = buttonENG
                        button3 = buttonBUS
                    elif timeBUS > timeENG and timeBUS > timeUD:
                        button1 = buttonBUS
                        button2 = buttonUD
                        button3 = buttonENG
        elif(totalClicks > 6):
            if(percENG > 0.5):
                button1 = buttonENG
                button2 = buttonENG
                if(countUD > countBUS):
                    button3 = buttonUD
                elif(countBUS > countUD):
                    button3 = buttonBUS
                else:
                    if(timeUD > timeBUS):
                        button3 = buttonUD
                    else:
                        button3 = buttonBUS
                if(streak):
                    button2 = button3
            elif(percBUS > 0.5):
                button1 = buttonBUS
                button2 = buttonBUS
                if(countUD > countENG):
                    button3 = buttonUD
                elif(countENG > countUD):
                    button3 = buttonENG
                else:
                    if(timeUD > timeENG):
                        button3 = buttonUD
                    else:
                        button3 = buttonENG
                if(streak):
                    button2 = button3
            elif(percUD > 0.5):
                button1 = buttonUD
                button2 = buttonUD
                if(countENG > countBUS):
                    button3 = buttonENG
                elif(countBUS > countENG):
                    button3 = buttonBUS
                else:
                    if(timeENG > timeBUS):
                        button3 = buttonENG
                    else:
                        button3 = buttonBUS
                if(streak):
                    button2 = button3
            else:
                if countENG > countUD and countENG > countBUS:
                    button1 = buttonENG
                    button2 = buttonBUS
                    button3 = buttonUD
                elif countUD > countENG and countUD > countBUS:
                    button1 = buttonUD
                    button2 = buttonENG
                    button3 = buttonBUS
                elif countBUS > countENG and countBUS > countUD:
                    button1 = buttonBUS
                    button2 = buttonUD
                    button3 = buttonENG
                else:
                    if countENG == countUD and countENG > countBUS:
                        if timeENG > timeUD:
                            button1 = buttonENG
                            button2 = buttonBUS
                            button3 = buttonUD
                        else:
                            button1 = buttonUD
                            button2 = buttonENG
                            button3 = buttonBUS
                    elif countENG == countBUS and countBUS > countUD:
                        if timeENG > timeBUS:
                            button1 = buttonENG
                            button2 = buttonBUS
                            button3 = buttonUD
                        else:
                            button1 = buttonBUS
                            button2 = buttonUD
                            button3 = buttonENG
                    elif countUD == countBUS and countUD > countENG:
                        if timeUD > timeBUS:
                            button1 = buttonUD
                            button2 = buttonENG
                            button3 = buttonBUS
                        else:
                            button1 = buttonBUS
                            button2 = buttonUD
                            button3 = buttonENG
                    elif countUD == countBUS  and countENG == countUD:
                        if timeENG > timeBUS and timeENG > timeUD:
                            button1 = buttonENG
                            button2 = buttonBUS
                            button3 = buttonUD
                        elif timeUD > timeENG and timeUD > timeBUS:
                            button1 = buttonUD
                            button2 = buttonENG
                            button3 = buttonBUS
                        elif timeBUS > timeENG and timeBUS > timeUD:
                            button1 = buttonBUS
                            button2 = buttonUD
                            button3 = buttonENG

        opt1.configure(text = button1["text"])
        opt2.configure(text = button1["text"])
        opt3.configure(text = button2["text"])
        opt4.configure(text = button3["text"])

        if button1["type"] != oldButton1["type"]:
            switchArch += 1
        
        startTime = datetime.datetime.now()
        
         #increment and store count data
        for i,types in enumerate(arch):
            if types["type"] == currentButton["type"]:
                currentArch = arch[i]

        print(arch)
        print(switchArch)


def generateReport():
    global endTime, startTime, button1, arch, switchArch, enterArch, exitArch
    endTime = datetime.datetime.now()
    delta = endTime - startTime
    timeDifference = int(delta.total_seconds() * 1000)
    for i,types in enumerate(arch):
        if types["type"] == button1["type"]:
            arch[i]["time"] += timeDifference 
    #Create bar graph with count
    archetypes = [arch[0]["type"], arch[1]["type"], arch[2]["type"]]
    counts = [arch[0]["count"], arch[1]["count"], arch[2]["count"]]
    times = [(arch[0]["time"]) / 1000, arch[1]["time"] / 1000, arch[2]["time"] / 1000]
    for i,t in enumerate(times):
        if t==0:
            times[i] = 0.001

    percentage = [ counts[0] / times[0], counts[1] / times[1], counts[2] / times[2] ]

    New_Colors = ['#477797','#77c6fc','#ddf1fe']
    exitArch = button1["type"]

    top2 = Toplevel(window)
    top2.geometry("550x150")
    top2.title("Statistics")
    Label(top2, text="STATISTIC 1", font=("Times New Roman", 18)).pack()

    Label(top2, text="Number of times the archetype of the user has changed: " + str(switchArch), font=("Times New Roman", 16)).pack()

    Label(top2, text="STATISTIC 2", font=("Times New Roman", 18)).pack()

    Label(top2, text="Entered as " + enterArch +", Exited as " + exitArch, font=("Times New Roman", 16)).pack()
    
    plot1 = plt.figure(1, figsize=(3,3))

    plt.bar(archetypes, counts, color=New_Colors)
    plt.title('Amount of Clicks Per Archetype')
    plt.xlabel('Archetypes')
    plt.ylabel('Number of Clicks')

    plot2 = plt.figure(2, figsize=(3,3))
    plt.bar(archetypes, times, color=New_Colors)
    plt.title('Amount of Time Per Archetype')
    plt.xlabel('Archetypes')
    plt.ylabel('Times (Seconds)')

    plot3 = plt.figure(3, figsize=(3,3))
    plt.bar(archetypes, percentage, color=New_Colors)
    plt.title('Count over Time Per Archetype')
    plt.xlabel('Archetypes')
    plt.ylabel('Percentage')

    plt.show()
    




#Throw all of creating the window and setting it up into a method


title = tk.Label(window, text = "Cookie Crew Backend Prototype", font=("Times New Roman", 18)).pack(side=tk.TOP)
userText = tk.Label(window, text = "Select User", font=("Times New Roman", 14)).pack()

user1B = tk.Button(window, text="User 1", width=10, height=1, command=lambda: open_popup(cookieFiles[0]))
user1B.place(x=85, y=60)
user2B = tk.Button(window, text="User 2", width=10, height=1, command=lambda: open_popup(cookieFiles[1]) )
user2B.place(x=218, y=60)
user3B = tk.Button(window, text="User 3", width=10, height=1, command=lambda: open_popup(cookieFiles[2]))
user3B.place(x=353, y=60)



canvas = Canvas(window, height=40, width=100, bg='gray', highlightbackground="black", highlightthickness=1)
canvas.place(x=327, y=190)
content = tk.Label(window, text = "Previous Choice of Content", font=("Times New Roman", 12))
content.place(x=292, y=165)

opt1 = Button(window, text="Cur 1", width=10, height=1, command=lambda: handleButton(button1))
opt1.place(x=40, y=340)
opt2 = Button(window, text="Cur 2", width=10, height=1, command=lambda: handleButton(button1))
opt2.place(x=160, y=340)
opt3 = Button(window, text="Alt 1", width=10, height=1, command=lambda: handleButton(button2))
opt3.place(x=280, y=340)
opt4 = Button(window, text="Alt 2", width=10, height=1, command=lambda: handleButton(button3))
opt4.place(x=400, y=340)

dataReport = Button(window, text="Data Report", width=15, height=1, command=lambda: generateReport()).pack(pady = 10, side=tk.BOTTOM)


key = Canvas(window, width = 150, height = 180, bg='lightgray')
key.place(x = 50, y = 120)
key.create_text(75, 20, text="KEY", font=("Times New Roman", 12))
key.create_rectangle(20, 40, 40, 60, fill="#477797")
key.create_rectangle(20, 90, 40, 110, fill="#77c6fc")
key.create_rectangle(20, 140, 40, 160, fill="#ddf1fe")
key.create_text(90, 50, text="Engineering", font=("Times New Roman", 12))
key.create_text(98, 100, text="Urban Design", font=("Times New Roman", 12))
key.create_text(85, 150, text="Business", font=("Times New Roman", 12))


window.mainloop()

### What to do
# Change the names of the buttons on the bottom based off the arch
# For example, if engineering, then the alt will change between the other two 
# Add the pop outs for the users to show the populated data
# Add the populated data
# Create the algoriths with the keyword and such to do a weighted arch option
