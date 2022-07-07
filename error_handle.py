def div52(divideBy):
    try:
        return 52 / divideBy
    except ZeroDivisionError:
        print('Error: you tried to divide by zero.')


print(div52(2))
print(div52(7))
print(div52(0))
print(div52(1))


#input validation

print('How many frogs do you have?')
numFrogs = input()

try:
    if int(numFrogs) >= 15:
        print('I love your frog dedication.')
    else:
        print('I think you need more frogs.')
          
except ValueError:
    print('That was not a number of frogs.')

#try except statements will handle the error without crashing the entire program
