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
t = 8
if t > 12:
    t = t-12

#userSays = (import("What's the subject?  "))

# The print format is a table matrix with the days of the week on the top and the time on the left.
print ("   Time Table |   Monday  |  Tuesday   | Wednesday | Thursday  |   Friday  ")
print ("=" * 75)
print (f"  {t}am to  {t+1}am |   Monday  |  Tuesday   | Wednesday | Thursday  |   Friday  ")
print ("-" * 75)
print (f"  {t+1}am to {t+2}am |   Monday  |  Tuesday   | Wednesday | Thursday  |   Friday  ")
print ("-" * 75)
print (f" {t+2}am to {t+3}am |   Monday  |  Tuesday   | Wednesday | Thursday  |   Friday  ")
print ("-" * 75)
print (f" {t+3}pm to  {t+4}pm |   Monday  |  Tuesday   | Wednesday | Thursday  |   Friday  ")
print ("-" * 75)
print (f"  {t+4}pm to  {t+5}pm |   Monday  |  Tuesday   | Wednesday | Thursday  |   Friday  ")
print ("-" * 75)
print (f"  {t+5}pm to  {t+6}pm |   Monday  |  Tuesday   | Wednesday | Thursday  |   Friday  ")
