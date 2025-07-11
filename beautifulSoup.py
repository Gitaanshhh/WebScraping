"""
Web Scraping using BeautifulSoup

Requiremnts :
- beautifulsoup4
- lxml
- requests

refs : 
https://youtu.be/XVv6mJpFOb0?si=e6_rFrMD_nxin1Ho


"""
from bs4 import BeautifulSoup

"""
A basic html Website
"""

with open('WebSraping\\index.html', 'r') as file:
    content = file.read()

    soup = BeautifulSoup(content, 'lxml')
    
    # Finds the FIRST tag
    tags = soup.find('h1')
    print("First h1 tag : ")
    print(tags)

    # Find all tags
    print("All h1 tag : ")
    tags = soup.find_all('h1')
    print(tags)

    # Print only content
    print("Content : ")
    for tag in tags:
        print(tag.text)

    # find divs of one class
    """
    cards = soup.find_all('div', class_='card')
    for card in cards:
        print(card.h5)
        name = card.h5.text
        cost = card.h5.cost
        print(f"{name} costs {price}")
    """

"""
A real Website
"""

import requests

"""
Getting F1 current Standings
"""
# Get status
html_text = requests.get('https://www.formula1.com/en/results/2025/drivers')
print(html_text)
# gives <Response[200]> => success

# Get actual html text
html_text = requests.get('https://www.formula1.com/en/results/2025/drivers').text
soup = BeautifulSoup(html_text, 'lxml')
drivers = soup.find_all('span', class_="test")
for ind, driver in enumerate(drivers):
    firstName = driver.find('span', class_='max-lg:hidden').text
    lastName = driver.find('span', class_='max-md:hidden').text
    print(f"{ind+1} - {firstName} {lastName}")