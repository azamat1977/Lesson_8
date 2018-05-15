import datetime
from datetime import datetime, date, time
import time
import calendar


test_day = datetime.strptime('19901204', '%Y%m%d').date()

today = date.today()

month_ago = date(2018, 4, 15)
plus_one_year = date(2019, 4, 15)


print(test_day)    #for question #3
print(today - month_ago)   #for question #4
print(datetime.isoweekday(plus_one_year))   #4 what day plus one year

