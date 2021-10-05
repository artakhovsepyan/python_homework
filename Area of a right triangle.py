# The input of the program consists of two integers: 
# the legs of a right triangle. 
# Output the triangle’s area.

leg_a = int(input('Input the value of leg_a: ' ))
leg_b = int(input('Input the value of leg_b: ' ))
result = (leg_a * leg_b) / 2
print(f'The area of the given right triangle is: {result}')