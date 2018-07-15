#datetime module gets the current date
##import datetime
##now_date = datetime.date.today()
##print(now_date)

#Constructed and formatted like:

##import datetime
##now = datetime.date(2015,1,1)
##print(now.strftime("%m-%d-%y. %d %b %Y is a \
##%A on the %d day of %B"))

#Supports calendar math:

import datetime
now = datetime.date.today()
birthday = datetime.date(1998,3,18)
age = now - birthday

print("I am", age.days, "days old.")
print("Which is", age.days/365, "years.")

#Use the datetime module to get the
#current day and time together:
import datetime

now_time = datetime.datetime.today()
print(now_time)
print(now_time.date())
print(now_time.time())

#Can use the time module to measure time passed:
import time

#click the stopwatch
start = time.clock()

#do an operation
for i in range(300):
    print(i)

#click it again
end = time.clock()

print("\nTotal time:", end - start, "seconds.")

