# Nested dictionaries
# Given the following dictionary:

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
# Write a python expression that gets the email address of Ramit.
email = ramit["email"]
print(email)

# Write a python expression that gets the first of Ramit's interests.
interests = ramit["interests"][0]
print(interests)

# Write a python expression that gets the email address of Jasmine.
# email_Jas = ramit["friends"][0]["email"]
email_Jas = ramit["friends"][0].get("email")
print(email_Jas)

# Write a python expression that gets the second of Jan's two interests.
jan_ints = ramit["friends"][1]["interests"][1]
print(jan_ints)

print(ramit)