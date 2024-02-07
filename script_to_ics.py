#Written to run with with Python 3.10.12

import sys

print("This script is used to generate an .ics file for workdays in order to import into a calendar application. \n ")
print("The file will be saved to the directory ~/home/Documents/Python/Calendar_Files when you run the script.\n")

input_year = input("Enter year in 4 digit format ex. YYYY:")
input_month = input("Enter month in 2 digit format ex. DD:")
input_starttime = input("Enter shift start time in 24hr format ex. HHMMSS:")
input_days = [str(n) for n in input('Enter work days in 2 digit format with a space after each day: ').split()]
input_3dig_month = input("Enter 3 character month for ics file name ex. AUG:")
BEGIN = "BEGIN:VEVENT"
DURATION = "DURATION:P0DT8H30M0S"
SUMMARY = "SUMMARY:Work"
END = "END:VEVENT" 

#You will need to make sure to modify the directory to the one that you want to save the file to
file_path = "/home/USER_HOME/Documents/Calendar_Files/" + input_3dig_month + input_year + '.ics'
sys.stdout = open(file_path, "w")

print("BEGIN:VCALENDAR" + "\n" + "VERSION:2.0")

for i in input_days:
    print(BEGIN + "\n" + "DTSTART:" + input_year + input_month + i + "T" + input_starttime + "\n" + DURATION + "\n" + SUMMARY + "\n" + END)

print ("END:VCALENDAR")