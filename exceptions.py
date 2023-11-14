import sys



try:
    x = int(input('x: '))
    y = int(input('y: '))   
except ValueError:
    print('Error a integer value must be provided')
    sys.exit(9)


try:
    result = x/y
except ZeroDivisionError:
    print('Error: cannot divide by 0')
    sys.exit(1)



print(f'{x} / {y} = {result}')