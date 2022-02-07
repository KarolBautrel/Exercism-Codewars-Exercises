from datetime import datetime, timedelta


a0 = 100
a = 101 
p = 0.98



def date_nb_days(a0, a, p):
    time = datetime(2016, 1, 1)
    print(time)
    n=1
    while a > a0:
        a0 += (a0*p/100/360)
        time += timedelta(days=n)
    return datetime.strftime(time, '%Y-%m-%d')

print(date_nb_days(100 , 101, 0.98))
	    