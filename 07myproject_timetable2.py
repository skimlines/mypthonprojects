# This is a program that prints a time table for different subjects that a student has so that it's in a table (matrix) instead of in list form.
# Such as if they have English Mondays and Wednesdays 9am to 11am
# Math Tuesdays and Thursdays 9am to 11am
# Gym on Tuesdays and Fridays 8am to 9am
# Science on Mon, Wed, Fri 1 to 3pm
# Social Studies (S.S.) every Monday and Thursday 11am to 1pm
# Foreign language every Tuesday at noon until 2pm
# The program could check for conflicts perhaps

import os
os.system('cls')

startTime = 8
endTime = 3
startHour = startTime
endHour = endTime

# Automate the displayed time on the left depending on the start time
# startHour is (blank space) + (number) + (am/pm)
def time_with_ampm(unformattedTime):
    nullSpace =""
    if unformattedTime < 10:
        nullSpace = " "

    ap = "am"
    if 8 < unformattedTime <= 12:
        ap = "pm"

    unformattedTime = (f"{nullSpace}{unformattedTime}{ap}")
    return (unformattedTime)

#userSays = (import("What's the subject?  "))

# The print format is a table matrix with the days of the week on the top and the time on the left.
print ("   Time Table  |   Monday  |  Tuesday   | Wednesday | Thursday  |   Friday  ")
print ("=" * 75)
     
while startTime != endTime:   
    startHour = time_with_ampm(startTime)
    startTime += 1
    if startTime > 12:
        startTime = startTime - 12
    endHour = time_with_ampm(startTime)
    print (f"  {startHour} to  {endHour} |  subject  |  subject  |  subject  |  subject  |  subject  ")
    print ("-" * 75)