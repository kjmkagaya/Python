


"""


The time Module
There is a popular time module available in Python, which provides functions for working with times and for converting between representations. Here is the list of all available methods.

S.No.	Function & Description
1	time.altzone
The offset of the local DST timezone, in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK). Use this if the daylight is nonzero.

2	time.asctime([tupletime])
Accepts a time-tuple and returns a readable 24-character string such as 'Tue Dec 11 18:07:14 2008'.

3	time.clock( )
Returns the current CPU time as a floating-point number of seconds. To measure computational costs of different approaches, the value of time.clock is more useful than that of time.time().

4	time.ctime([secs])
Like asctime(localtime(secs)) and without arguments is like asctime( )

5	time.gmtime([secs])
Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the UTC time. Note − t.tm_isdst is always 0

6	time.localtime([secs])
Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the local time (t.tm_isdst is 0 or 1, depending on whether DST applies to instant secs by local rules).

7	time.mktime(tupletime)
Accepts an instant expressed as a time-tuple in local time and returns a floating-point value with the instant expressed in seconds since the epoch.

8	time.sleep(secs)
Suspends the calling thread for secs seconds.

9	time.strftime(fmt[,tupletime])
Accepts an instant expressed as a time-tuple in local time and returns a string representing the instant as specified by string fmt.

10	time.strptime(str,fmt = '%a %b %d %H:%M:%S %Y')
Parses str according to format string fmt and returns the instant in time-tuple format.

11	time.time( )
Returns the current time instant, a floating-point number of seconds since the epoch.

12	time.tzset()
Resets the time conversion rules used by the library routines. The environment variable TZ specifies how this is done.

There are two important attributes available with time module. They are −

S.No.	Attribute & Description
1	
time.timezone

Attribute time.timezone is the offset in seconds of the local time zone (without DST) from UTC (>0 in the Americas; <=0 in most of Europe, Asia, Africa).

2	
time.tzname

Attribute time.tzname is a pair of locale-dependent strings, which are the names of the local time zone without and with DST, respectively.

The calendar Module
The calendar module supplies calendar-related functions, including functions to print a text calendar for a given month or year.

By default, calendar takes Monday as the first day of the week and Sunday as the last one. To change this, call the calendar.setfirstweekday() function.

Here is a list of functions available with the calendar module −

S.No.	Function & Description
1	
calendar.calendar(year,w = 2,l = 1,c = 6)

Returns a multiline string with a calendar for year year formatted into three columns separated by c spaces. w is the width in characters of each date; each line has length 21*w+18+2*c. l is the number of lines for each week.

2	
calendar.firstweekday( )

Returns the current setting for the weekday that starts each week. By default, when calendar is first imported, this is 0, meaning Monday.

3	
calendar.isleap(year)

Returns True if year is a leap year; otherwise, False.

4	
calendar.leapdays(y1,y2)

Returns the total number of leap days in the years within range(y1,y2).

5	
calendar.month(year,month,w = 2,l = 1)

Returns a multiline string with a calendar for month month of year year, one line per week plus two header lines. w is the width in characters of each date; each line has length 7*w+6. l is the number of lines for each week.

6	
calendar.monthcalendar(year,month)

Returns a list of lists of ints. Each sublist denotes a week. Days outside month month of year year are set to 0; days within the month are set to their day-of-month, 1 and up.

7	
calendar.monthrange(year,month)

Returns two integers. The first one is the code of the weekday for the first day of the month month in year year; the second one is the number of days in the month. Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 to 12.

8	
calendar.prcal(year,w = 2,l = 1,c = 6)

Like print calendar.calendar(year,w,l,c).

9	
calendar.prmonth(year,month,w = 2,l = 1)

Like print calendar.month(year,month,w,l).

10	
calendar.setfirstweekday(weekday)

Sets the first day of each week to weekday code weekday. Weekday codes are 0 (Monday) to 6 (Sunday).

11	
calendar.timegm(tupletime)

The inverse of time.gmtime: accepts a time instant in time-tuple form and returns the same instant as a floating-point number of seconds since the epoch.

12	
calendar.weekday(year,month,day)

Returns the weekday code for the given date. Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 (January) to 12 (December).

Other Modules and Functions
If you are interested, then here you would find a list of other important modules and functions to play with date & time in Python −

The datetime Module
The pytz Module
The dateutil Module


"""

