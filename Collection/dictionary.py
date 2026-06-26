#dictionaries = They contain key value pairs and changeable, do not have duplicates
capitals = {"USA" :"Washington DC",
            "India" : "New Delhi",
            "China" : "Beijieng",
            "Russia" : "Moscow",
            "Thailand" : "Bangkok" }
# print(capitals.get("DFC"))
capitals.update({"Germany" : "Berlin"})
# print(capitals, end=" ")
capitals.pop("China")
print(capitals)
# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)
# value = capitals.values    
# for value in capitals.values():
#     print(value)
items = capitals.items()
for key, value in capitals.items():
    print(f"{key} : {value}")



# dictionary.get(key)
# dictionary.update({key: value})
# dictionary.pop(key)
# dictionary.keys()
# dictionary.values()
# dictionary.items()

# ---------------------- DICTIONARIES ----------------------

# A dictionary stores data as key : value pairs.
# Keys must be unique.
# Values can be duplicated.
# Dictionaries are mutable (changeable).

# Access a value
capitals["India"]        # Returns "New Delhi"

# Safer access (returns None if key doesn't exist)
capitals.get("India")

# Add or update a key-value pair
capitals.update({"Germany": "Berlin"})

# Remove a key-value pair
capitals.pop("China")

# Remove the last inserted item
capitals.popitem()

# Remove everything
capitals.clear()

# Number of key-value pairs
len(capitals)

# ----------------------------------------------------------
# keys() -> Returns all the keys

for key in capitals.keys():
    print(key)

# ----------------------------------------------------------
# values() -> Returns all the values

for value in capitals.values():
    print(value)

# ----------------------------------------------------------
# items() -> Returns both key and value as tuples

for key, value in capitals.items():
    print(f"{key} : {value}")

# Equivalent to:
# ("USA", "Washington DC")
# ("India", "New Delhi")
# ("Germany", "Berlin")

# Python automatically unpacks each tuple:
# key = "USA"
# value = "Washington DC"

# ----------------------------------------------------------
# IMPORTANT

# keys(), values(), and items() are METHODS.
# They MUST have parentheses.

capitals.keys()      # ✔ Correct
capitals.values()    # ✔ Correct
capitals.items()     # ✔ Correct

# capitals.keys      # ✘ Wrong
# capitals.values    # ✘ Wrong
# capitals.items     # ✘ Wrong

# ----------------------------------------------------------
# Dictionary indexing uses KEYS, not numbers.

capitals["India"]    # ✔ Correct
# capitals[0]        # ✘ Wrong

# ----------------------------------------------------------
# Dictionaries preserve insertion order (Python 3.7+),
# but you access elements by key, not by position.