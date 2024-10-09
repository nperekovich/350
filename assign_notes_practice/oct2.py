'''
chapter 4
working with lists
'''
#for loop = for every item in the list, do this
magicians=['alice','david','carolina']
for magician in magicians:
  print(magician)
  print(magician.title()+", that was a great trick!")
  #.title will put the attached item in title case
  print("I can't wait to see your next trick,"+magician.title()+".\n")
'''
python connects indented lines to the lines
above it, so if something after the line is not
indented, it will be considered a separate
entity
'''
#range() to specify range of numbers
for value in range(1,5):
  print(value)
  #does not print the number five, off-by-one coding situation
#convert range into list
numbers=list(range(1,6))
print(numbers)
#skip numbers in a given range
even_numbers=list(range(2,11,2))
print(even_numbers)
#two asterisks ** represent exponents
squares=[]
for value in range(1,11):
  squares.append(value**2)
print(squares)
#simple statistics
digits=[1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)
'''
list comprehension builds same list with one line of code
squares=[value**2 for value in range(1,11)]
print(squares)
'''
#slice prints specified range
players=['charles','martina','michael','florence','eli',]
print(players[0:3])
#use slice in for loop
print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())
#use ([:]) to create a copy of entire original list
'''
values that cannot change = immutable
immutable lists = tuple
'''
#styling your code
'''
indentation, four spaces per indent
line length < 80 characters
use blank lines
