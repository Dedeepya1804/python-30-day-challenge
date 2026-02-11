try:
    a = int(input('enter a number: '))
    b = int(input('enter another number: '))

    op = input('neter an operator eg: *,-,/,...: ')

    if op == '+' :
        print(a +b )
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        div = a/b
        print(div)
        
except ZeroDivisionError:
    print('canot divide by zero')

except ValueError:
    print('invalid input')
