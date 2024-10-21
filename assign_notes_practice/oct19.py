'''
chapter 6
dictionaries
'''
#dictionary is collection of key-value pairs
#each key connected to a value
#key can be a number/string/list/another dictionary/etc.
#dictionary wrapped in braces {}
alien_0 = {'color' : 'green', 'points' : 5}
#key-value pair is a set of values associated with each other
#to get value, give name of dictionary and place key inside square brackets:
print(alien_0['color'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
#setting aliens position
alien_0['x position'] = 0
alien_0['y position'] = 25
print(alien_0)
'''
starting with empty dictionary and adding values
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
'''
#modifying values
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
#track position of alien at different speeds
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print("Original x-position: " + str(alien_0['x_position']))
#move alien to the right
#determine how far to move the alien based on current speed
if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3
#new position is original position plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
#change speed of alien
alien_0['speed'] = 'fast'

#dictionary of similar objects in multiple lines
favorite_languages = {
  'jen':'python',
  'sarah':'c',
  'edward':'ruby',
  'phil':'pythoon',
}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

#looping
user_0 = {
  'username':'efermi',
  'first':'enrico',
  'last':'fermi',
}
#loop all key-value points
for key, value in user_0.items():
  print("\nKey: " + key)
  print("Value: " + value)
  #can also abbrev. variables
  #i.e. 'for k, v in user_0.items()'
for name, language in favorite_languages.items():
  print(name.title() + "'s favorite language is " +
        language.title() + ".")

'''nesting'''
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
  print(alien)
#empty list for storing aliens
aliens = []
#make 30 green aliens
for alien_number in range(30):
  new_alien = {'color':'green', 'points':5, 'speed':'slow'}
  aliens.append(new_alien)
#show first 5 aliens
for alien in aliens[:5]:
  print(alien)
print("...")
#show how many aliens created
print("Total number of aliens: " + str(len(aliens)))
for alien in aliens[0:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10
elif alien['color'] == 'yellow':
  alien['color'] = 'red'
  alien['speed'] = 'fast'
  alien['points'] = 15

'''list in a dictionary'''
pizza = {
  'crust':'thick',
  'toppings':['mushrooms', 'extra cheese'],
}
#summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
  print("\t" + topping)
#dictionary in a dictionary
users = {
  'aeinstein': {
    'first':'albert',
    'last':'einstein',
    'location':'princeton',
  },
  'mcurie': {
    'first':'marie',
    'last':'curie',
    'location':'paris',
  },
}
for username, user_info in users.items():
  print("\nUsername: " + username)
  full_name = user_info['first'] + " " + user_info['last']
  location = user_info['location']
print("\tFull name: " + full_name.title())
print("\tLocation: " + location.title())
