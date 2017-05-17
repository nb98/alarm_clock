import time
import datetime

print "Time in seconds since the epoch: %s" %time.time()
print "Current date and time: " , datetime.datetime.now()
print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")


print "Current year: ", datetime.date.today().strftime("%Y")
print "Month of year: ", datetime.date.today().strftime("%B")
print "Week number of the year: ", datetime.date.today().strftime("%W")
print "Weekday of the week: ", datetime.date.today().strftime("%w")
print "Day of year: ", datetime.date.today().strftime("%j")
print "Day of the month : ", datetime.date.today().strftime("%d")
print "Day of week: ", datetime.date.today().strftime("%A")

DWT = datetime.date.today().strftime("%A")

if DWT = "monday"
    print("Ok")
else
    print("NoK")

def alarm_clock(day, on_vacation):
    '''Alarm Clock'''
    if on_vacation:
        if day in range(1,6):
            return '10:00'
        elif day in [0,6]:
            return 'off'
    else:
        if day in range(1,6):
            return '7:00'
        elif day in [0,6]:
            return '10:00'
