d1 = {}  # create new empty dict

# initialize dict with key/value pairs 
# (keys can be any string, number or tuple of strings or numbers)
airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',  
            'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}

d2 = dict()  # new empty dict -- {} preferred

# initialize dict with named parameters; keys must be valid identifier names
d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)

pairs = [('Washington', 'Olympia'), ('Virginia', 'Richmond'),
         ('Oregon', 'Salem'), ('California', 'Sacramento')]
state_capitols = dict(pairs)  # initialize dict with an iterable of pairs

print(f"{d3['red'] = }") # print value for given key

print(f"{airports['LAX'] = }")

airports['SLC'] = 'Salt Lake City'  # assign to new key
airports['LAX'] = 'Los Angeles (main)'  # overwrite existing value (re-use key)
print(f"{airports['SLC'] = }")
print()

print(f"{airports = }")

for code, city in sorted(airports.items()):
    print(code, city)

print(f"{len(airports) = }")

print(f"{'LAX' in airports = }")
print(f"{'abc' in airports = }")


airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['OAK'] = }")
print(f"{airports.get('MVX') = }")
print(f"{airports.get('MVX', 'NO SUCH KEY') = }")
print(airports.get('MVX'))
KEY = 'MVX'
if KEY in airports:
    print(airports[KEY])
else:
    print("NOT FOUND")


#   KEY   VALUE
for code, city in sorted(airports.items()):
    print(code, city)

for code in airports:
    print(code)

for value in airports.values():
    print(value)
