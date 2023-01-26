x = int(input("Enter a value: "))
y = int(input("Enter another value: "))

if x % y == 0:
    multiple = '{} is a multiple of {}'.format(x,y)
    print(multiple)
else:
    not_multiple = '{} is not a multiple {}'.format(x,y)
    print(not_multiple)