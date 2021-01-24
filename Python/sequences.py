
# String (Properties : Imutable, orderd)
name = "Kalidas S V"

print(name[5])

# this function can use for getting the legth of all sequence 
len(name)

#List : mutable and ordered
names = ["Harry", "Lisa", "Arnold"]

names.append("Jhoney")

print(names[0])

names.sort()

print(names)

#Set : not an ordered sequence, Duplicates are not allowed
cities = set()

cities.add("new delhi")
cities.add("Bombay")
cities.add("Bangalore")
cities.add("Chennai")

print(cities)

cities.remove("Chennai")

len(cities)

#Tuples are used to store two or three values together as a single unit. it is unmutable and ordered
point = (1.5,3.5)

print(point)

print(f"length of tuple : {len(point)}")

#Dictionaries : Used to same key value paris. It is mutable and is not ordered
capitals = {"Kerala":"Trivandrum", "Tamilnadu":"Chenani", "Karnataka":"Bangaluru"}

print(capitals)

capitals["Andrapradesh"] = "Hyderabad"

print(capitals["Andrapradesh"])