# Given a year, return the century it is in. 
# The first century spans from the year 1 up to and including the year 100, 
# the second - from the year 101 up to and including the year 200, etc.

year = int(input("Input a year "))
century = (year + 99) // 100
print(century)







