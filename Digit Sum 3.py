# The program’s input is a three-digit number 
# (do not check that fact, just assume it to be true). 
# Output the sum of its digits.

number = int(input('Input a three-digit number: '))

first_digit = number // 100
second_digit = (number // 10) % 10 
third_digit = number % 10
result = first_digit + second_digit + third_digit

print(f'The sum of digits in given number is: {result}')


#Some digits in generall

n = int(input('input natural number: '))
result = 0
while n != 0:
    if n % 10 != 0:
        result += n % 10
    n = n // 10

print(f'The sum of digits in given number is: {result}')
    

def sum_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n//10
    return sum

print(f'The sum of digits in given number is: {sum_digits(123)}')