# The program input consists of 3 integer numbers:  
# a1, a2 and  n. a1 and a2 are the first two members of  progression. 
# Output the value of the n-th member.

a_1 = int(input('input the value of firts number: '))
a_2 = int(input('input the value of second number: '))
a_n = int(input('input number of n-th element : '))
result = int(a_1 + (a_n - 1)*(a_2-a_1))
print(f'the {a_n}-th element of given arithmetic progression is {result}')












