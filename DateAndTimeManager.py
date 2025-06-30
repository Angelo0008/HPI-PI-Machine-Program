from Imports import *

dateToday = ""
timeNow = ""

def GetDateToday():
    global dateToday

    dateToday = datetime.datetime.today()
    dateToday = dateToday.strftime('%Y/%m/%d')

def GetTimeNow():
    global timeNow

    timeNow = datetime.datetime.today()
    timeNow = timeNow.strftime('%H:%M')