#Create a mapping of state of abbrivationn
 
states = {
          'Oregon' : 'OR',
          'Florida' : 'FL',
          'California': 'CA',
           'New York' : 'NY',
           'Michigan': 'MI'
         }


# CREATES A BASIC SET OF STATES AND SOME CITIES IN THEM

cities = {
          'CA': 'San Francisco',
          'MI': 'Detroit',
          'FL':  'Jacksonville'
         }

#Add more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Printout some cities

print(' - ' * 10)

print("NY city has :" , cities['NY'])
print("OR city has :" , cities['OR'])

#Print some states
print(' - ' * 10)

print("Michigan's abbreviation:", states['Michigan'] )

print("Florida's abbreviation:", states['Florida'] )

#do it by states than cities dictionary  
print(' - ' * 10)
print("Michigan has :", cities[states['Michigan']] )

print("Florida has :", cities[states['Florida']] )

#print every state abbrivation   
print(' - ' * 10)

for i in list(states.items()) :
    print(f"State  abbrivation is :{i}")

#print every cities in state 
print(' - ' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at same time
print(' - ' * 10)

for state, abbrev in list(states.items()):
    print(f" {state} is abbrevatied {abbrev}")
    print(f"and has cities {cities[abbrev]}")

# Safely get a abbrivation by state that might not be there
state = states.get('Texas')

if not state:
   print("Sorry no Texas")

#Get a city with default value

city = cities.get('TX', 'Does not Exist')

print (f"city for the state 'TX' is :{city}")


