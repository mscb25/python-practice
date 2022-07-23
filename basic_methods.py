import copy
from pprint import pprint #pretty print, for lists and dicts

#working with the copy module, which creates an entierly new copy of a list

mylist = ['yo', 'this', 'is', 'crazy', 67, 9, 12, 4]
#print(mylist)

newlist = copy.deepcopy(mylist)

newlist[2] = 'frog'
newlist.append(1111)

print(mylist)
print(newlist)

#revisiting dictionaries

mydict = {'maddie': 'frog', 'erin': 'indeed', 'teal': 'color', 'dom': 'hockey'}

print(mydict.keys())
print(mydict.values())

#prints in tuples
print(mydict.items())
          
# finding num occurences of a letter in a string

message = "Maddie and Erin visited the movie theater last weekend."
letter_count = {}

for letter in message.lower():
    letter_count.setdefault(letter, 0)
    letter_count[letter] = letter_count[letter] + 1

pprint(letter_count)

#multiline print

print(""" Surprise


this is still part of the string

consider yourself pranked """)

#function to pad strings

print("Hey".rjust(10))
print("Yo".ljust(20, "*"))
print("Maddie".center(20, "~"))

#string formatting

sample = "Much like coding in c, you can insert a variable within a string using the % sign"

print("Some advice: %s" % (sample))
