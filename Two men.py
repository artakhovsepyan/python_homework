# Two men start to shoot several cans of Coca-Cola they have put on a log. 
# The first man began shooting the cans in order, starting with the leftmost, 
# the second man from the rightmost. At some point, they simultaneously shot the same last can. 
# And at this point they stop.
# You are given the number of cans the first man has shot, and the number of cans the second man has shot. 
# Output the number of cans the first man missed because of the second man, and the number of cans 
# the second man missed because of the first man.

# 1.
man_1 = int(input('Input tne number of first man shoots: '))
man_2 = int(input('Input tne number of second man shoots: '))
missed_1 = man_2 - 1
missed_2 = man_1 - 1
print(f'first man missed {missed_1} shoots\nseccond man missed {missed_2} shoots\n')

#2.
cans = (man_1 + man_2) - 1
missed_1 = cans - man_1
missed_2 = cans - man_2
print(f'first man missed {missed_1} shoots\nseccond man missed {missed_2} shoots')
