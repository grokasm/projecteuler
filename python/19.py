def get_months_in_year(y):
	days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
	days_in_month_leap = [0,31,29,31,30,31,30,31,31,30,31,30,31]
	
	if y % 4 == 0 and (y % 100 or y % 400 == 0):
		return days_in_month_leap
	else:
		return days_in_month

def days(dow, ymd1, ymd2):
	(y,m,d) = ymd1
	months_in_year = get_months_in_year(y)

	while (y,m,d) <= ymd2:
		yield (dow, d,m,y)		
		d += 1
		dow = (dow + 1) % 7
		if d > months_in_year[m]:
			d = 1
			m += 1
			if m > 12:
				m = 1
				y += 1
				months_in_year = get_months_in_year(y)

				
# sunday = 0
# saturday = 6
# 
dow = 0
epoch = (1900,1,1)
start = (1901,1,1)
end = (2000,12,31)

# find the day of the week on the start day
for x in days(1,epoch,start):
	(dow,d,m,y) = x

count = 0
for x in days(dow,start,end):
	(dow,d,m,y) = x
	if dow == 0 and d == 1:
		count += 1

print count
