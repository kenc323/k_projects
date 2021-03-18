import requests
from bs4 import BeautifulSoup
reuters = "https://www.google.co.uk/search?q=reuters"
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
senate = "https://efdsearch.senate.gov/search/"
# This parses the html response into a bs object
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

html = list(soup.children)[2]
body = list(html.children)[3]
p = list(body.children)[1]

p.get_text()