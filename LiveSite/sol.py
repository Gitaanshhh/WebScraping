"""
Web Scraping the below page
https://sourcing.alibaba.com/rfq/rfq_search_list.htm?spm=a2700.8073608.1998677541.1.82be65aaoUUItC&country=AE&recently=Y&tracelog=newest

Requiremnts :
- selenium
- Chrome Driver
- pandas

"""

from selenium import webdriver
import json
import pandas as pd
from datetime import datetime

url = "https://sourcing.alibaba.com/rfq/rfq_search_list.htm?spm=a2700.8073608.1998677541.1.82be65aaoUUItC&country=AE&recently=Y&tracelog=newest"

driver = webdriver.Chrome()
driver.get(url)

print('Connected')


driver.implicitly_wait(30)

"""
Gettig PAGE_DATA["index"].data from the browser as a JSON string
window.PAGE_DATA -> checks if js obj exists
window.PAGE_DATA["index"] -> checks if the index attribute exists
window.PAGE_DATA["index"].data -> checks if the data in index attribute of the js obj exists
|| [] -> returns empty list if it doesnt exist
"""

page_data_json = driver.execute_script("""
    return JSON.stringify(
        window.PAGE_DATA && 
        window.PAGE_DATA["index"] && 
        window.PAGE_DATA["index"].data || []);
""")

print('Recieved Data')

data = json.loads(page_data_json)

rows = []

# Format: 02-07-2025
today = datetime.now().strftime('%d-%m-%Y')

def tag(tags, tagname):
    return any(t.get('tagName') == tagname for t in tags)

#RFQ ID,Title,Buyer Name,Buyer Image,Inquiry Time,Quotes Left,Country,Quantity Required,Email Confirmed,Experienced Buyer,Complete Order via RFQ,Typical Replies,Interactive User,Inquiry URL,Inquiry Date,Scraping Date
for item in data:

    tags = item.get('tags', [])

    rows.append({
    'RFQ ID': item.get('rfqId'),
    'Title': item.get('subject'),
    'Buyer Name': item.get('buyerName'),
    'Buyer Image': item.get('portraitPath', ''),
    'Inquiry Time': item.get('openTimeStr'),
    'Quotes Left': item.get('rfqLeftCount'),
    'Country': item.get('country'),
    'Quantity Required': f"{item.get('quantity')} {item.get('quantityUnit')}".strip(),
    'Email Confirmed': 'Yes' if tag(tags, 'emailConfirm') else 'No',
    'Experienced Buyer': 'Yes' if tag(tags, 'experienced_buyer') else 'No',
    'Complete Order via RFQ': 'Yes' if item.get('hasQuoEquity') else 'No',
    'Typically Replies': 'Yes' if tag(tags, 'typically_replies') else 'No',
    'Interactive User': 'Yes' if tag(tags, 'interactive_user') else 'No',
    'Inquiry URL': "https:" + bytes(item.get('url', ''), 'utf-8').decode('unicode_escape'),
    'Inquiry Date': today,
    'Scraping Date': today
})

pd.DataFrame(rows).to_csv('sol.csv', index=False, encoding='utf-8-sig')

"""
# Can also use csv instead of pandas
# utf-8-sig encoding is for Excel compatibility

import csv

with open('sol.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
"""

print('Updated CSV')

driver.quit()