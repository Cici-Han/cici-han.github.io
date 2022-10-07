from bs4 import BeautifulSoup
from requests import head

with open("bs4/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
# print(tag.getText())
# print(tag.get("href"))

section_heading = soup.find(name="h3", class_="heading")  # class后面必须加"_"
# print(section_heading.text)

company_url = soup.select_one(selector="p a")
print(company_url)
heading = soup.select(".heading")
print(heading)
