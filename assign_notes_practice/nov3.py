'''
chapter 7
'''
i = 1
while i < 6:
  print(i)
  i += 1
#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''
for
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for x in "banana":
  print(x)
#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
    fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#range
for x in range(6):
  print(x)
for x in range(2, 6):
  print(x)
for x in range(2, 30, 3):
  print(x)
#else
for x in range(6):
  print(x)
else:
  print("Finally finished!")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#pass
for x in [0, 1, 2]:
  pass

'''
chapter 8
'''
def my_function():
  print("Hello from a function")

my_function()
#arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#arbitrary
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#keyword
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#default parameter
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#list
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#return
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#pass
def myfunction():
  pass
#positional
def my_function(x, /):
  print(x)

my_function(3)
def my_function(x):
  print(x)

my_function(x = 3)
#keyword only
def my_function(*, x):
  print(x)

my_function(x = 3)
def my_function(x):
  print(x)

my_function(3)
#combination
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
