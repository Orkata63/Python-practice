#https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar

if __name__ ==  "__main__":
    month, day , year  = map(int, input().split(" ")) #was wrong at start day, month , year was using European
    dayName = calendar.weekday(year,month,day)
    print(calendar.day_name[dayName].upper())
