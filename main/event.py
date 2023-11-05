#import numpy as np

"""
Gotta start off with installing numpy the same way as Flask
There were some problems with numpy so I'm going with the hack method until we can get things figured out
"""

event_list = []
#The list of events for later use


standard_size = (24 * 4)    #24 hour day with hours broken into four 15 minute pieces

def openID():
    temp = 0
    for events in event_list:
        if events["EventID"] > temp:
            temp = events["EventID"]
    next = temp + 1
    return next


def addEventToList(EventName = "", UserName = "", day = 0, userID = 0, startHour = 0, startMin = 0, endHour = 0, endMin = 0, priority = False, freeTime = True):
    
    roundedStartMin = roundMin(startMin)
    roundedEndMin = roundMin(endMin)

    eventID = openID()
    eventData = {"UserID": userID, "EventID": eventID, "UserName": UserName, "EventName": EventName, "Day": day, "startHour": startHour, "startMin": startMin, "endHour": endHour, "endMin": endMin, "Priority": priority, "freeTime": freeTime, "roundedEndMin": roundedEndMin, "roundedStartMin": roundedStartMin}
    event_list.append(eventData)
#    globalID += 1
    return eventData
#creates and adds an event to the events list

def roundMin(min):
    if min < 15:
        return 0
        
    if min < 30:
        return 1

    if min < 45:
        return 2

    if min < 60:
        return 3
        
    else:
        return 0
#rounds minutes down to the 15 minute part. THIS IS ONLY NECESSARY IF THE INPUT ISN'T ALREADY LIMITED
#TODO: find if incoming time is already limited

def schedule():         #BE CAREFUL THIS HAS AN INFINITE LOOP THAT DOESN'T HAVE AN OUT YET
    calendarM = createList(standard_size)
    calendarP = createList(standard_size)
    #Create the minute and priority schedules    
    endFlag = False
    while endFlag == False:
        #TODO:add stuff like "if given an event addEventToSchedule(ID, calendarM)" then fill calendarP with EventID[priority] for the same spots
        break
    #This function should then be its own little "main" that holds all that's needed and loops until it is told to stop

def clearSchedule(list, size):
    i = 0
    while i < size:
        list[i] = False
        i += 1
#Clear list completely

def removeEvent(ID, list):
    for event in event_list:
        if event['EventID'] == ID:
            start = (event['startHour'] * 4 + event['roundedStartMin'])
            end = (event['endHour'] * 4 + event['roundedEndMin'])
            while start < end:
                list[start] = False
                start += 1
            event_list.remove(event)
            return list
    return "Event ID not found"

def addEventToSchedule(ID, list): #should always go with addPrioritytoSchedule
    for event in event_list:
        if event['EventID'] == ID:
            start = (event['startHour'] * 4 + event['roundedStartMin'])
            end = (event['endHour'] * 4 + event['roundedEndMin'])
            if event['freeTime'] == False:
                invertList(list)
            while start < end:
                list[start] = True
                start += 1
            if event['freeTime'] == False:
                invertList(list)
            return list
    return "Event ID not found"

def addPrioritytoSchedule(ID, list): #should always go with addEventToSchedule
    for event in event_list:
        if event['EventID'] == ID:
            start = (event['startHour'] * event['roundedStartMin'])
            end = (event['endHour'] * event['roundedEndMin'])
            while start < end:
                list[start] = event['Priority']
                start += 1
            return list
    return "Event ID not found"



def invertList(list, size = standard_size):
    i = 0
    while i < size:
        list[i] = not list[i]
        i += 1
    return list

def createList(size = standard_size):
    array = []
    i = 0
    while i < size:
        array.append(False)
        i += 1
    return array

def viewEvents():
    print(event_list)

def test():
    schedule = createList()
    print("Regular schedule: ",schedule)
    schedule = invertList(schedule)
    print("Inveted schedule: ",schedule)
    schedule = invertList(schedule)

    addEventToList("","",0,1,5,15,7,30)
    addEventToSchedule(1,schedule)
    
    print("adding event 1 w/ open time 5:15-7:30:\n",schedule)
    
    addEventToList("","",0,2,9,0,12,45,True,True)
    addEventToSchedule(2,schedule)

    print("adding event2 w/ open time and priority 9:00-12:45:\n",schedule)

    addEventToList("","",0,5,7,0,10,00,False,False)
    addEventToSchedule(3,schedule)

    print("adding event3 w/ closed time 7:00-10:00:\n",schedule)

    print("events list:\n")
    viewEvents()
    print("Removing event 1:\n")
    removeEvent(1,schedule)
    viewEvents()






#test()
#I removed this test so that console looks cleaner on startup. There is still a test function at api/test as of 11/5/23 -Sl




# I SUMMON AARON'S CODE FROM THE GRAVEYARD
# RESTORING 500 LIFE POINTS TO AARON'S CODE
# I USE POT OF GREED, AND THEN
# I HAVE MY SPAGHETTI CODE ATTACK YOU FOR 999 DAMAGE
# -SL




#Code Graveyard

"""class Event:
    UserName = ""
    day = 0
    userID = 0
    startHour = 0
    startMin = 0
    endHour = 0
    endMin = 0
    priority = False
    freeTime = True

    roundedEndMin = 0       #these two are for if the app doesn't already restrict people to 0, 15, 30, and 45 for minute markers
    roundedStartMin = 0     #They can be deleted in that case, along with the roundStart/EndMin functions



    def __init__(EventName = "", UserName = "", day = 0, userID = 0, startHour = 0, startMin = 0, endHour = 0, endMin = 0, priority = False, freeTime = True):
        Event.UserName = UserName
        Event.EventName = EventName
        Event.day = day
        Event.userID = userID
        Event.startHour = startHour
        Event.startMin = startMin
        Event.endHour = endHour
        Event.endMin = endMin
        Event.priority = priority
        Event.freeTime = freeTime

        Event.roundStartMin()
        Event.roundEndMin()

    #this just initializes everything. Event is primarily just temporary data storage

    def roundStartMin():

        if Event.startMin < 15:
            Event.roundedStartMin = 0
            return
        
        if Event.startMin < 30:
            Event.roundedStartMin = 1
            return

        if Event.startMin < 45:
            Event.roundedStartMin = 2
            return

        if Event.startMin < 60:
            Event.roundedStartMin = 3
            return
        
        else:
            Event.roundedStartMin = 0
            return
        

        
    def roundEndMin():

        if Event.endMin < 15:
            Event.roundedEndMin = 0
            return
        
        if Event.endMin < 30:
            Event.roundedEndMin = 1
            return

        if Event.endMin < 45:
            Event.roundedEndMin = 2
            return

        if Event.endMin < 60:
            Event.roundedEndMin = 3
            return
        
        else:
            Event.roundedEndMin = 0
            return

"""
"""these two round the minutes to the most appropriate 15 minute mark"""
"""Hopefully the rounding just takes the minute value out of Schedule and doesn't create an entire object for it"""

"""
class Schedule:
    hours = 24
    minuteChunks = 4
    
    event_list = []
    eventCounter = 0
   #This is so that, later, specific events can be removed by remembering their ID, and start/end times
    #the user name is so that the one schedule can hold ever person and delete only their event
    #event counter variable is just for testing because otherwise each event needs its own ID and code to read the IDs
    
    CalendarM = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    CalendarP = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, ]
    

  def __init__():
        i = ii = 0
        while i < Schedule.hours:
            while ii < Schedule.minuteChunks:
                Schedule.CalendarM.append(False)        #for some reason append was doing literally nothing when tested. It's supposed to just staple a False to the end of the list
                Schedule.CalendarP.append(False)
                ii += 1
            i += 1
            ii = 0
    set both of the arrays to the right size and all false

    def clearSchedule():
        
        for i in Schedule.CalendarM:
            Schedule.CalendarM[i] = False
        i = ii = 0
        while i < Schedule.hours:
            while ii < Schedule.minuteChunks:
                Schedule.CalendarM = "False"
                Schedule.CalendarP = "False"
                ii += 1
            i += 1
    #clear everything (it can be more specific later)

    def invertSchedule():

        for i in Schedule.CalendarM:
#            if calendar[i] == False:
                Schedule.CalendarM[i] = True                  #for some reason this does not interact with the list
#            else:
#                calendar[i] = False

       i = 0
        while i < (Schedule.hours * Schedule.minuteChunks):
                if Schedule.CalendarM[i] == False:
                    Schedule.CalendarM[i] = True
                else:
                    Schedule.CalendarP[i] = False
                i += 1"

    
    def addEvent(anEvent = Event):
        Schedule.event_list.append(anEvent)
        Schedule.eventCounter += 1

    def addEventToSchedule(counter):
        anEvent = Schedule.event_list[counter]

        start = anEvent.startHour - 1
        startMin = anEvent.roundedStartMin
        end = anEvent.endHour - 1
        endMin = anEvent.roundedEndMin

        startM = start * Schedule.minuteChunks + startMin
        endM = end * Schedule.minuteChunks + endMin
        
        if anEvent.freeTime is False:                       #this function call will need to change
            Schedule.invertSchedule()
        ""if the person marked that they are putting time they are busy flip everything""

        while startM < endM:
            Schedule.CalendarM[startM] = True #not Schedule.CalendarM[startM]
            Schedule.CalendarP[startM] = anEvent.priority
            startM += 1
        
        if anEvent.freeTime is False:
            Schedule.invertSchedule()
    ""flip it back""
    
    def invertSchedule():
        i = 0
        while i < 24:
            Schedule.CalendarM[i] = True
            i += 1
"""
"""e = Event("event",0,0,7,15,9,30,True,True)
    e2 = Event("event2",0,1,0,0,3,15,True,False)

    s = Schedule()

    print("Starting availabilities:\n", s.CalendarM)

    invertSchedule(s)
    i = 0
    while i < 24:
        s.CalendarM[i] = True
        i += 1
    #This gets the locations to invert, but for some reason functions from a class can't be called

    print("Inverted availability:\n", s.CalendarM)""

    ""s.addEvent(e)
    s.addEventToSchedule(0)

    print("Event 1 availabilities:\n", s.CalendarM)
    print("Event 1 Priorities:\n", s.CalendarP)

    s.addEvent(e2)
    s.addEventToSchedule(1)

    print("Event 2 availabilities:\n", s.CalendarM)
    print("Event 2 Priorities:\n", s.CalendarP)"""
