import requests
from bs4 import BeautifulSoup
wordToSearch = input("Enter Any Word: ")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{wordToSearch}"

response = requests.get(url)


if "definition" in response.text:
    indexOfDefinition = response.text.index("definition")
    if "synonyms" in response.text:
        indexOfSynonyms = response.text.index("synonyms")
        print(response.text[indexOfDefinition + 29:indexOfSynonyms -4])
else:
    print("invalid")
