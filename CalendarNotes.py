import os
import datetime

CURRENT_DIR = getcwd()
#YYYY-MM-DD HH:MM:SS.SSSS
TODAYS_DATE = datetime.now()

def cleanInput(calendar):
    print("hello")
    #delete unneeded stuff
    # loop until you find todays date
    # once you do, delete everything before it
	
def saveDates(calendar):
    print("hello")
    # get Todays date
    # parse dates and delete whatever you don't need
    # start from the end and delete whatever comes before todays date
    # iterate through file and save dates and summary
    # DTSTART seems to be the date that I am looking for 
    # ?? clean file: dont need anything before todays date??

def birthdayMessage(participant, date):
    x = calculateLengthOfTime(date)
    print(participant + "'s" + " birthday is " + x + " days away")
    print("Be sure to wish them a happy birthday")

def calculateLengthOfTime(date):
    print(date)

# Can we override this and pass in different types??
def appointment(typeOfAppointment, date)
    if(typeOfAppointment == derm):
        dermAppointment(date)
    else if(typeOfAppointment == doc):
        docAppointment(date)
    else if(typeOfAppointment == dent):
        dentAppointment(date)
    else if(typeOfAppointment == car):
        carAppointment(date)

def dermAppointment(date):
    amountOfTime = getTimeUntil(date);
    print("You have a dermatologist appointment in " + amountOfTime + "days")
    print("Be sure to send any paperwork you may need")

def docAppointment(date):
    amountOfTime = getTimeUntil(date);
    print("You have a doctor appointment in " + amountOfTime + "days")
    print("Be sure to send any paperwork you may need")

def dentAppointment(date):
    amountOfTime = getTimeUntil(date);
    print("You have a dentist appointment in " + amountOfTime + "days")
    print("Be sure to send any paperwork you may need")

def carAppointment(date):
    amountOfTime = getTimeUntil(date);
    print("You have a car appointment in " + amountOfTime + "days")
    print("Be sure to send any paperwork you may need")

def getTimeUntil(date):
    # amountOfTime = date - TODAYS_DATE
    return amountOfTime

def getInput():
    print("hello")
    # start Google calendar api
    # export input to CURRENT_DIR
    # cd to CURRENT_DIR
    # unzip *.zip to ./calender
    # remove .zip
    # for item in ./calender/
    #	cleanInput(item)
    return birthdays, calendar, email

	
def cleanUp():
    cmd = "rm calendar/*"
    #os.(cmd)

def main():
    # input files
    #birthdays, calendar, email = getInput()
    birthdays = "./calendar/"
    calender = "./calendar/"
    email = "./calendar/tcjc107@gmail.com.ics"
    
    # initial cleanInput, only save summaries and dates <- maybe do this during save
    # or don't do this and only do it if you need to iterate over the data multiple times
    # saveDates(inputFile)
    
    # based on savedDates/Events look for words in description like Birthday,name,appointments
    # write useful messages for each event
    
    #cleanUp()

if __name__ == "__main__":
    main()
