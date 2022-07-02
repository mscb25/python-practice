#funct to find the first occurence of element
#will return the index the element can be found at

# s = string
# p = char you're looking to find
def findOcc(s, p):
    a = s.find(p)
    return a

#function to change the case of string, pretty self explan

# s = the string
def changeCase(s):
    upper_string = s.upper()
    lower_string = s.lower()
    return upper_string, lower_string

#to get the average of a list

#list1 = the list 
def listAvg(list1):
    avg = sum(list1) / len(list1)
    return avg


#to remove a sublist from a larger list

# list1 = the main list
# list2 = the sublist you're looking to kick out

def removeSublist(list1, list2):
    for elm in list2:
        list1.remove(elm)
    return list1

#prints a list of all the numbers in the specified range that are divisible by 3

# list1 = the initial list
# num_range = the range of numbers to be considered (int)
def divisBy3(list1, num_range):
    print [x for x in range(num_range) if x % 3 == 0]


# create a new list of nums that are the squared vers of the original list

# orig_list = the starting list

def squaredList(orig_list):
    sq_list = [x ** 2 for x in orig_list]
    return sq_list

# finding greatest common divisor by importing math

# a = num 1
# b = num 2

import math

def findGCD(a, b):
    return math.gcd(a, b)


#determine if a list has any duplicates

def hasDuplicates(my_list):
    for i in range(len(my_list)):
        for k in range(i+1, len(my_list)):
            if (my_list[i] == my_list[k]):
                return True
    return False


#making a dictionary with the same keys but different vals

# d = initial dictionary
# n = how much the values (integers) should be incremented by

def updateValues(d, n):
  newvals = {}
  for key in d:
    newvals[key] = d[key] + n
  return newvals
 
