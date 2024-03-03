import requests

# res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/human')

# print(type(res.text))



url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Content-type": "application/json; charset=UTF-8"
}
data = {
    "title": "foo", 
    "body": "bar",
    "userId": 2,
}

req = requests.post(url, headers=headers, json=data)

print(req.text)
