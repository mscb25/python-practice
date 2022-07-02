
#retrieves odd numbers from 1 till integer n, generating a list
def odd(n):
    for num in range(n+1):
        if num % 2 == 1:
            yield num


#returns all the integers from int n down until 0

def reverse(n):
    for num in range(n, -1, -1):
        yield num

#returns fibonacci sequence up till int n

def fibonacci(n):
    fib_array = []
    for num in range(n):
        if num == 0 or num == 1:
            fib_array.append(num)
            yield num
        else:
            new_num = fib_array[num - 2] + fib_array[num - 1]
            fib_array.append(new_num)
            yield new_num
