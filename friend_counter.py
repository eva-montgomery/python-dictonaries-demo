# Friend counter
# Using the dictionary from the Nested dictionaries exercise above, 

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],

  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# write a function countFriends() that accepts a dictionary as an argument and returns 
def count_friends(dic):
    friend_count = len(dic["friends"])
    dic["friends_count"] = friend_count
    print(dic)

count_friends(ramit)

# a new dictionary that includes a new key friends_count:

# friend_count = len(ramit["friends"])
# print(friend_count)

# ramit["friends_count"] = friend_count
# print(ramit)


