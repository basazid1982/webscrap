import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the web page
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the table
table = soup.find('table')

# Step 4: Extract rows (excluding header)
rows = table.find_all('tr')[1:]

# Step 5: Extract data into a list of dictionaries
language_data = []
for row in rows:
    cols = row.find_all('td')
    language = cols[1].text.strip()
    salary = cols[3].text.strip()
    language_data.append({'Programming Language': language, 'Average Salary': salary})

# Step 6: Create DataFrame
df = pd.DataFrame(language_data)

# Step 7: Save to CSV
df.to_csv('popular-languages.csv', index=False)

print("Data saved to 'popular-languages.csv'")
