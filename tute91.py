import re

pattern = r"([A-a]raiz)\W+"
text = """RegExr was created by gskin Zraiz ner.com.Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript fl Zraiz avors of RegEx are araiz ported. Validate your expression with Tests mode.
The side bar includes a Araiz Cheatsheet, full Reference, and Help. You can also Save & Share with the Community and view patterns you create Araiz or favorite in My Patterns.
Explore results with the Tools araiz  below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English.
"""

matchRegx = re.search(pattern, text)
mathcRegxFind = re.finditer(pattern, text)
print(matchRegx.span)

for matcheRegx in mathcRegxFind:
    print(text[matcheRegx.span()[0]: matcheRegx.span()[1]])

