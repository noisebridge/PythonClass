import calendar
import pprint

c = calendar.TextCalendar(calendar.SUNDAY)

print dir(c) # to view objects
pprint.pprint(c.yeardatescalendar(2015))

# uncomment to view large prints below
#print calendar.TextCalendar(calendar.SUNDAY).formatyear(2007, 2, 1, 1, 2)

#html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
#print html_cal.formatmonth(2015, 5)
