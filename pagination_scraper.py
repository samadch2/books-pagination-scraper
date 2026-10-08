import requests
from bs4 import BeautifulSoup
import pandas as pd

all_books = []    # pehly 3 pages per Loop chalain ge 
for page in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    print(f"Scraping page: {page}")
    response = requests.get(url)
    response.encoding = "utf-8" # encoding set karna zaroori hai, warna kuch characters galat aa jate hain
    soup = BeautifulSoup(response.text, "html.parser")  # har kitaab k container ko dhoondna he
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").get_text(strip=True)

        all_books.append({
            "Title": title,
            "price": price
        })         #  Pandas dataframe banakar Excel mein save karna
df = pd.DataFrame(all_books)
excel_filename = "all_books_pagination.xlsx"
df.to_excel(excel_filename, index=False)
print(f"Data Successfully saved to {excel_filename}!")        

