
# this is an iterator that returns even numbers
class DIY_Range:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        evenNums = []
        for i in range(1, self.n+1):
            if i % 2 == 0:
                value = i
                evenNums.append(i)
            else:
                i += 1
        return evenNums

    
myrange = DIY_Range(8)
print (myrange.next())


#this is an iterator that returns vals from integer n down to 0
class NumRange:
    
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        n_list = []
        for num in range(self.n, -1, -1):
            n_list.append(num)
        return n_list



#this is an interative class for fibonacci

class fibRange:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self

    def next(self):
        fib_list = []
        for num in range(self.n):
            if num == 1 or num == 0:
                fib_list.append(num)
            else:
                fib_list.append(fib_list[num - 2] + fib_list[num - 1])
        return fib_list
    
