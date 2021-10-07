"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

#Access a value by its key -- lookup
print(f"UNC has {schools['UNC']} students")

#Remove a key-value pair from a dictionary by its key
schools.pop("Duke")

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else: 
    print("No key 'Duke' in schools")

# Update and Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

#empty dictionary literal
schools = {}
print(schools)

# Alternatively, intialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# Calling a nonexistent key
# print(schools["UNCC"])

for school in schools: 
    print(f"Key: {school} -> Value: {schools[school]}")