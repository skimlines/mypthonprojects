# This is a program that prints a time table for different subjects that a student has so that it's in a table (matrix) instead of in list form.
# Such as if they have English Mondays and Wednesdays 9am to 11am
# Math Tuesdays and Thursdays 9am to 11am
# Gym on Tuesdays and Fridays 8am to 9am
# Science on Mon, Wed, Fri 1 to 3pm
# Social Studies (S.S.) every Monday and Thursday 11am to 1pm
# Foreign language (German) every Tuesday at noon until 2pm
# ***Bonus*** The program could check for scheduling conflicts

import os
os.system('cls')

startTime = 8
endTime = 3
subjects = {
    'English': {'days': [1, 3],'hours': [9, 10],},
    'Math': {'days': [2, 4],'hours': [9, 10],},
    'Swimming': {'days': [2, 5],'hours': [8, 8],},
    'Science': {'days': [1, 3],'hours': [1, 2],},
    'S.S': {'days': [1, 4],'hours': [11, 12],},
    'German': {'days': [2, 0],'hours': [12, 1],},
    }

def weekday_names(x):
    # Here, it will convert numerical days to the actual name of the day, and it will read 0 and 1 position in the string to do this.
    daysOfTheWeek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    newList = []
    for numbers in x:
        numbers = daysOfTheWeek[numbers-1]
        newList.append(numbers)
    return newList

for name, time in subjects.items():
    # print(name.title() + " happens on: ", end="")
    timesHeld = time['hours']
    daysHeld = time['days']
    # print (weekday_names(daysHeld), end="")
    # print(" During the Hours of: ", timesHeld)

def time_with_ampm(unformattedTime):
# Automate the displayed time on the left depending on the start time
# startHour is (blank space) + (number) + (am/pm)
    nullSpace =""
    if unformattedTime < 10:
        nullSpace = " "

    ap = "pm"
    if 8 <= unformattedTime < 12:
        ap = "am"

    unformattedTime = (f"{nullSpace}{unformattedTime}{ap}")
    return (unformattedTime)

#subject = (input("What's the subject?  "))

def is_there_class(whichClass):
# Class data is stored as a dictionary!: subject {days held, hours}
# Such as if they have English Mondays and Wednesdays 9am to 11am
    
    row = column = 0
    while row < 5:
        for name, time in subjects.items():
            if time['hours'] == 9:
                whichClass = time['name']
                row += 1
            while column < 7:
                column += 1

    # Formats it to fit in the middle of the matrix        
    if len(whichClass) % 2 == 0:
        whichClass = str(whichClass) + " "
    while len(whichClass) < 14:
        whichClass = " " + str(whichClass) + " "

    return(whichClass)


# The print format is a table matrix with the days of the week on the top and the time on the left.
print ("\n                       ~~~~*  Y o u r   S t u d y   S c h e d u l e *~~~~\n")
print ("                |     Monday    |    Tuesday    |   Wednesday   |   Thursday    |     Friday    |")
print ("=" * 97)
     
while startTime != endTime:   
    startHour = time_with_ampm(startTime)
    startTime += 1
    if startTime > 12:
        startTime = startTime - 12
    endHour = time_with_ampm(startTime)

#    subject = " " * 11
    print (f"  {startHour} to {endHour}  |", end='')
    
    # This prints the subjects
    x = 0
    while x < 5:
        subject = is_there_class(subjects)
        print(f"{subject}|", end='')        
        x += 1 

    print ()
    
    # This prints a line under each time slot
    x = 0
    while x < 6:
        print ("+", end="")
        print ("-" * 15, end="")
        x += 1
    print ("+")
print ()