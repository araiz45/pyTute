import requests
from bs4 import BeautifulSoup
url = "https://www.everywhereist.com/about/"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup.prettify())
for heading in soup.find_all("li"):
    print(heading.text)
print(res.text)
