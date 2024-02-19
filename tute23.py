# Operation on Tuples 
countries = ["Pakstan", "Japan", "Canada", "China", "Chile"]
countries.append("England")
countries.pop(2)
countries[2] = "Finland"
countriesTup = tuple(countries)
print(countriesTup)
for x in countriesTup:
    print(x.lower())

# How many times a value is in the tuple
print(countries.count("Japan"))
# Gives Index of First Occurances (str, start, end)
print(len(countries))
print(countries.index("Japan",1, 3))