bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message="My first bicycle was a "+bicycles[0].title()+"."
print(message)
#.append('') adds item to end of list without changing rest of list
#.insert(0,'') adds an item to a specified position in the list
#del motorcycles[1] will delete the specified item in the list, making it no longer accessible
#pop() does same as delete, but u can still access it later, example:
'''
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
'''
#can add position number in parentheses for specific value
#.sort will sort a list permanently
cars=['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#example above will sort the list alphabetically)
#.sort(reverse=True) will sort in reverse alphabetical order
#.reverse() will reverse the list in its original order (whether alphabetical or not)
#sorted(cars) will sort the list without changing the oiriginal list positions
#len() shows how many items are in a list
