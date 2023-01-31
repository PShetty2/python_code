#get 3 numbers from users, then find the max value.
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a 2nd number: '))
num3 = int(input('Enter a 3rd number: '))

if num1 > num2 and num3:
    print('The first number {} is the max.'.format(num1))
else:
    if num2 > num1 and num3:
        print('The second number {} is the max.'.format(num2))
    else:
        if num3 > num1 and num2:
            print('The third number {} is the max'.format(num3))
