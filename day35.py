
# Step 1: Import libraries
import requests
from bs4 import BeautifulSoup

# Step 2: Website URL
url = "https://books.toscrape.com/"

# Step 3: Get website data
response = requests.get(url)

# Step 4: Check status code
print("Status Code:", response.status_code)

# Step 5: Convert HTML into readable structure
soup = BeautifulSoup(response.text, "html.parser")

# Step 6: Find all book elements
books = soup.find_all("article", class_="product_pod")

# Step 7: Extract book names and prices
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    print("Book Name:", title)
    print("Price:", price)
    print("-" * 30)
