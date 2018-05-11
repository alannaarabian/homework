import calender
cal = calender. TextCalender()
cal.pryear(2012)

cal = calender.TextCalender(3)
cal.pryear(2018)

cal= calender.TextCalender(6)
cal.prmonth(2018,10)

d = calender.LocaletextCalender(6, "spanish")
d.pryear(2012)

#exercise 2

import math
myvar= math.floor(78.89)
print(myvar)

#copy makes a shallow copy - the refs stay the same- deepcopy created a com