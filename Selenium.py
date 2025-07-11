"""
Web Scraping using BeautifulSoup

Requiremnts :
- beautifulsoup4
- lxml
- requests
- selenium
- Chrome Driver (I used version - 138.0.7204.94, based on my chrome version)
get it from - https://developer.chrome.com/docs/chromedriver/downloads

refs : 
https://www.youtube.com/watch?v=j7VZsCCnptM&t=1749s 

""" 

from selenium import webdriver
import os

#os.environ['PATH'] += 'C:\\Users\\gitaa\\OneDrive\\Desktop\\A2\\WebSraping\\chromedriver-win64'

url = "https://google.com"

driver = webdriver.Chrome()
driver.get(url)

print('Connected')


driver.implicitly_wait(30)