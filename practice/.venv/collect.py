import os
import csv
from bs4 import BeautifulSoup

# Folder containing HTML files
data_folder = "data"

# Output CSV file
output_file = "amazon_products.csv"

# List to store extracted data
products = []

# Loop through all HTML files
for filename in os.listdir(data_folder):
    if filename.endswith(".html"):  # Ensure only HTML files are processed
        filepath = os.path.join(data_folder, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

            # Extract product title
           
            title_tag = soup.find("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")

            title = title_tag.text.strip() if title_tag else "N/A"

            # Extract product price
            price_tag = soup.find("span", class_="a-price-whole")
            price = price_tag.text.strip() if price_tag else "N/A"

            # Extract product link
            link_tag = soup.find("a", class_="a-link-normal")
            link = f"https://www.amazon.in{link_tag['href']}" if link_tag else "N/A"

            # Append data to list
            products.append([title, price, link])

# Save to CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price", "Link"])  # CSV Header
    writer.writerows(products)

print(f"✅ Extracted {len(products)} products and saved to {output_file}")
