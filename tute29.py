# Dictionaries 
dic = {
    'name': "araiz",
    "fname": "zahid",
    'rollno': "BC220423372"
}

print(dic['rollno']) # Gives error if not avaiable
print(dic.get('rollno'))
# Returns Keys 
print(dic.keys())
# Returns Values
print(dic.values())

for key in dic.keys():
    print(f"The Key is {key} and Value is {dic[key]}")

print(dic.items())


for key, value in dic.items():
    print(f"The Key is {key} and Value is {value}")