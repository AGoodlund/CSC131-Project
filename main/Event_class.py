#import numpy as np
import math

"""
Gotta start off with installing numpy the same way as Flask
There were some problems with numpy so I'm going with the hack method until we can get tests figured out
"""



class Events:
    openTimes = []
    event_list = []
        #The list of Events for later use TODO: remove anything about the event list because this is a class that gets passed things and that's it. it has no memory
    standard_size = (24 * 4)    #24 hour day with hours broken into four 15 minute pieces

    def findOpenID():
        temp = 0
        for event in Events.event_list:
            if event["EventID"] > temp:
                temp = event["EventID"]
        next = temp + 1
        return next


    def addEventToList(UserName = "",userID = 0, startHour = 0, startMin = 0, endHour = 0, endMin = 0, priority = False, isFreeTime = True):
        roundedStartMin = Events.roundMin(startMin)
        roundedEndMin = Events.roundMin(endMin)

        eventID = Events.findOpenID()
        eventData = {"UserID": userID, "EventID": eventID, "UserName": UserName,"startHour": startHour, "startMin": startMin, "endHour": endHour, "endMin": endMin, "Priority": priority, "isFreeTime": isFreeTime, "roundedEndMin": roundedEndMin, "roundedStartMin": roundedStartMin}
        #cut this eventData down to userID/UserName, start/end times priority, and isFreeTime
        Events.event_list.append(eventData)
        return eventData
    #creates and adds an event to the Events list

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



    def clearSchedule(list):
        i = 0
        while i < Events.standard_size:
            list[i] = False
            i += 1
        Events.openTimes.clear()
        

    def removeEvent(ID, list):
        for event in Events.event_list:
            if event['EventID'] == ID:
                start = (event['startHour'] * 4 + event['roundedStartMin'])
                end = (event['endHour'] * 4 + event['roundedEndMin'])
                while start < end:
                    list[start] = False
                    start += 1
                Events.event_list.remove(event)
                return list
        return "Event ID not found"

    def addEventToSchedule(ID, list):#should always go with addPrioritytoSchedule
        for event in Events.event_list:
            if event['EventID'] == ID:
                start = (event['startHour'] * 4 + event['roundedStartMin'])
                end = (event['endHour'] * 4 + event['roundedEndMin'])
                if event['isFreeTime'] == False:
                    Events.invertList(list)
    #how this flips needs to be rethought. it should remain flipped until the button is no longer active to give more accurate open/closed times
    #TODO:just have inverList be its own thing to be called 4head
                while start < end:
                    list[start] = True
                    start += 1
                if event['isFreeTime'] == False:
                    Events.invertList(list)
                return list
        return "Event ID not found"

    def addPrioritytoSchedule(ID, list):#should always go with addEventToSchedule
        for event in Events.event_list:
            if event['EventID'] == ID:
                start = (event['startHour'] * event['roundedStartMin'])
                end = (event['endHour'] * event['roundedEndMin'])
                while start < end:
                    list[start] = event['Priority']
                    start += 1
                return list
        return "Event ID not found"
    #Priority is being nixed



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
        print("array size " + str(i))
        return array

    def viewEvents():
        print(Events.event_list)

    def findOpenTime(planner):
        theHour = minute = 0
        temp = -1
        hour = 0
        foundTime = False
        for time in planner:
            if time is True:
                foundTime = True
                if temp < hour:
                    temp = hour
                    Events.openTimes.append({"Open hour": hour})
                    Events.openTimes.append({"Open minute": (minute)})
                else:
                    Events.openTimes.append({"Open minute": (minute)})
            theHour += 1
            hour = math.floor(theHour / 4)+1
            minute = theHour % 4 * 15
        if foundTime is False:
            return "no open time found"
        return Events.openTimes
    
             

def goodTimeString(dictionary = []):

    timeFlag = False
    isATime = times = False
    startTime = endTime = timer = startHours = startMins = endHrs = endMins = 0
    timeString = "The open times are:\n"
    Sextra = Eextra = ""

    if len(dictionary) == 0:
        return "this is Empty"

    for times in dictionary:
        if times is True:
            isATime = True
            if timeFlag is False:
                timeFlag = True
                startTime = timer


        if times is False:
            if timeFlag is True:
                startHours = math.floor(startTime / 4) + 1
                startMins = ((startTime % 4) * 15)
                endHrs = math.floor(endTime / 4) + 1
                endMins = ((endTime % 4) * 15)
                if startMins == 0: 
                    Sextra = "0"
                if endMins == 0:
                    Eextra = "0"

                timeString = timeString + str(startHours) + ":" + str(startMins) + Sextra + " - " + str(endHrs) + ":" + str(endMins) + Eextra + "\n"
                Sextra = Eextra = ""
                startTime = endTime
                timeFlag = False
            

        timer += 1
        endTime = timer
    if times is True and timeFlag is True:
        startHours = math.floor(startTime / 4) +1
        startMins = ((startTime % 4) * 15)
        endHrs = math.floor(endTime / 4) 
        endMins = ((endTime % 4) * 15)

        if startMins == 0: 
            Sextra = "0"
        if endMins == 0:
            Eextra = "0"

        timeString = timeString + str(startHours) + ":" + str(startMins) + Sextra + " - " + str(endHrs) + ":" + str(endMins) + Eextra + "\n"
    if isATime is False:
        return "there are no open times"
    return timeString


def test():

    test = Events

    schedule = test.createList()
    print("length of schedule is " + str(len(schedule)))
    print("Regular schedule: ",schedule)
    schedule = test.invertList(schedule)
    print("Inveted schedule: ",schedule)
    schedule = test.invertList(schedule)

    opening = test.findOpenTime(schedule)
    print("\nstarting open times: ",opening)

    test.addEventToList("steve", 0, 5, 15, 7 ,30)
    test.addEventToSchedule(1,schedule)
        
    print("adding event 1 w/ open time 6:15-8:30")#:\n",schedule)
        
    test.addEventToList("steve", 0, 9, 0, 12 ,45)
    test.addEventToSchedule(2,schedule)

    print("adding event2 w/ open time 9:00-12:45")#:\n",schedule)

    test.addEventToList("steve", 0, 7, 0, 10 ,0)
    test.addEventToSchedule(3,schedule)

    print("adding event3 w/ open time 7:00-10:00")#:\n",schedule)
    
    test.addEventToList("steve", 0, 0, 0, 1 ,0)
    test.addEventToSchedule(4,schedule)

    print("adding event4 w/ open time 0:00-1:00")#:\n",schedule)

    test.addEventToList("steve", 0, 15, 0, 23 ,45)
    test.addEventToSchedule(5,schedule)

    print("adding event5 w/ open time 15:00-24:45")#:\n",schedule)


    print("Events list:")
    test.viewEvents()

    opening = test.findOpenTime(schedule)
    print("\nopen times: \n", opening)


    
    print("length of schedule is " + str(len(schedule)))
    goodTimes = goodTimeString(schedule)
    print(goodTimes)



    test.clearSchedule(schedule)
    print("\ncleared schedule: \n",schedule, "\ncleared openTimes: \n", test.openTimes)

    opening = test.findOpenTime(schedule)
    print("\nopen times: \n", opening)
    print("open times test\n", test.openTimes)

    goodTimes = goodTimeString(schedule)
    print(goodTimes)



    del schedule
    del opening
    del test

#addEventToList(UserName = "",userID = 0, startHour = 0, startMin = 0, endHour = 0, endMin = 0, priority = False, isFreeTime = True)
#addEventToSchedule(ID, list) with ID being whatever ID you want to give the event and list being the array for the schedule

#test()
#Turning the test event off by default for now for smoother loading. It can be accessed under 127.0.0.1:5000/api/test -SL

#Try making a class that just reads from a dictionary that has start/end times, priority, and a test "user ID" which is all set to 0
#for now mash everytest into a single schedule array and then later make it so that it makes one for each user with Events


