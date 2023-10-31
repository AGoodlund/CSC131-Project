#import numpy as np

"""
Gotta start off with installing numpy the same way as Flask
There were some problems with numpy so I'm going with the hack method until we can get things figured out
"""


class Event:
    UserName = ""
    day = 0
    userID = 0
    startHour = 0
    startMin = 0
    endHour = 0
    endMin = 0
    priority = False
    freeTime = True

    roundedEndMin = 0
    roundedStartMin = 0

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
    """this just initializes everything. Event is primarily just temporary data storage"""

    def roundEndMin():
        minutes = Schedule.minuteChunks
        pass
    def roundStartMin():
        minutes = Schedule.minuteChunks
        pass
    """these two round the minutes to the most appropriate 15 minute mark"""
    """Hopefully the rounding just takes the minute value out of Schedule and doesn't create an entire object for it"""


class Schedule:
    hours = 24
    minuteChunks = 4
    
    event_list = {}
    eventCounter = 0
    """This is so that, later, specific events can be removed by remembering their ID, and start/end times"""
    """the user name is so that the one schedule can hold ever person and delete only their event"""
    """event counter variable is just for testing because otherwise each event needs its own ID and code to read the IDs"""
    
    CalendarM = [bool]
    CalendarP = [bool]
    i = ii = 0

    while i < hours:
        while ii < minuteChunks:
            CalendarM.append(False)
            CalendarP.append(False)
    """set both of the arrays to the right size and all false"""

    def clearSchedule():
        i = ii = 0
        while i < Schedule.hours:
            while ii < Schedule.minuteChunks:
                Schedule.CalendarM = False
                Schedule.CalendarP = False
    """clear everything (it can be more specific later)"""

    def invertSchedule():
        i = ii = 0
        while i < Schedule.hours:
            while ii < Schedule.minuteChunks:
                Schedule.CalendarM = not Schedule.CalendarM
                Schedule.CalendarP = not Schedule.CalendarP
    
    def addEvent(anEvent = Event):
        Schedule.event_list.append(anEvent)
        Schedule.eventCounter += 1

    def addEventToSchedule(counter):
        anEvent = Schedule.event_list[counter]

        start = anEvent.startHour - 1
        #also need rounded start min
        end = anEvent.endHour - 1
        #also need rounded end min

        startM = start * Schedule.minuteChunks
        endM = end * Schedule.minuteChunks
        
        if anEvent.freeTime is False:
            Schedule.invertSchedule()

        while startM < endM:
            Schedule.CalendarM[startM] = not Schedule.CalendarM[startM]
            Schedule.CalendarP[startM] = anEvent.priority
            startM += 1
        
        if anEvent.freeTime is False:
            Schedule.invertSchedule()
