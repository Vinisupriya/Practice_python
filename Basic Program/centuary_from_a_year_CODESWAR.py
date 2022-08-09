#The first century spans from the year 1 up to and including the year 100, 
# the second century - from the year 101 up to and including the year 200, etc.
#Task Given a year, return the century it is in.
#Examples 1705 --> 18 1900 --> 19 1601 --> 17 2000 --> 20
def century(year):
    if year==0:
        print("Pls enter vaild year")
    elif year<=100:
        print("1st centuary")
    elif year % 100 == 0:
        print( year// 100,"century")
    else:
        print(year // 100 + 1,"century")
year = int(input("Enter your year"))
century(year) 
    