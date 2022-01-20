import datetime
d= datetime.date(2016, 7, 24)
print(d)

tday= datetime.date.today()
print(tday)
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())

tdelta= datetime.timedelta(days=7)
print(tday+ tdelta)
print(tday- tdelta)

bday= datetime.date(2022, 10, 8)
tillbday= bday-tday
print(tillbday)

t= datetime.time(9, 30, 45, 100000)
print(t.hour)

dt= datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)

tdel= datetime.timedelta(days=7)
print(dt+ tdel)

tdel= datetime.timedelta(hours=12)
print(dt+ tdel)


dt_today= datetime.datetime.today()
dt_now= datetime.datetime.now()
dt_utcnow= datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)


import pytz 
dt= datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo= pytz.UTC)
print(dt)

dt_mtn= dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)


for tz in pytz.all_timezones:
	print(tz)


dt_str= 'July 26, 2016'
dt= datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)