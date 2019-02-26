import re
from datetime import datetime, timedelta, timezone
def to_timestamp(dt_str, tz_str):

	# str to datetime
	# note: the datetime has no timezone
	lcday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

	# get timezone number
	tz = re.match(r'^UTC([+-]\d{1,2}):\d{1,2}$', tz_str).group(1)

	# create timezone
	tz_utc = timezone(timedelta(hours = int(tz)))
    
    #set timezone
    # the datetime has timezone
	tzday = lcday.replace(tzinfo = tz_utc)

	#datetime to timestamp
	timestamp = tzday.timestamp()
	return timestamp


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')