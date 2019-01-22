
from bs4 import BeautifulSoup
import requests, lxml


url = "https://www.covers.com/Sports/NBA/Odds/US/SPREAD/competition/Online/ML"

req = requests.get(url)

resp = req.text

soup = BeautifulSoup(resp,'html.parser')

print(soup.prettify())