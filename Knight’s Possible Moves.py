# You are given the coordinates of a cell on a standard chess board: py and px. 
# It is guaranteed that the coordinates are correct, i.e. are integers from the interval [1,8]. 
# Output all cells that the knight can move in a single move(each coordinate pair on separate line). 
# It is guaranteed that for a given input cell all 8 moves exist. The output cells order does not matter.


knight_coordinate_x = int(input('input x coordinate: '))
knight_coordinate_y = int(input('input y coordinate: '))
x = knight_coordinate_x
y = knight_coordinate_y

print('1-st possible coordinate: ', y - 1, x - 2)
print('2-nd possible coordinate: ', y - 1, x + 2)
print('3-rd possible coordinate: ', y - 2, x - 1)
print('4-th possible coordinate: ', y - 2, x + 1)
print('5-th possible coordinate: ', y + 1, x - 2)
print('6-th possible coordinate: ', y + 1, x + 2)
print('7-th possible coordinate: ', y + 2, x - 1) 
print('8-th possible coordinate: ', y + 2, x + 1)







