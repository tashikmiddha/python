# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# browser=webdriver.Chrome()
# element=input("enter the element")
# file=0
# for i in range(2):
#  browser.get(f"https://www.amazon.in/s?k={element}&page={i}&xpid=NysdkkEjXE2zm&crid=K2CZSURF13DRqid=1741697831&sprefix=laptop%2Caps%2C308&ref=sr_pg_2")
#  elems=browser.find_elements(By.CLASS_NAME,"puis-card-container")
#  for i in elems:
#     # print(i.text)
#     d=i.get_attribute("outerHTML")
#     with open(f"data/{element}_{file}.html","w",encoding="utf-8")as f:
#       f.write(d)
#       file+=1
#  time.sleep(2)
# browser.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Setup WebDriver
browser = webdriver.Chrome()

element = input("Enter the element: ").strip()
if not element:
    print("Error: Search element cannot be empty!")
    browser.quit()
    exit()

file = 0
os.makedirs("data", exist_ok=True)  # Ensure 'data' folder exists

for i in range(2):
    url = f"https://www.amazon.in/s?k={element}&page={i}&ref=sr_pg_2"
    print(f"Fetching: {url}")  # Debugging output
    browser.get(url)

    elems = browser.find_elements(By.CLASS_NAME, "puis-card-container")
    
    if not elems:
        print("Warning: No elements found. The class name might be incorrect!")
    
    for item in elems:
        if item is not None:
            d = item.get_attribute("outerHTML")
            with open(f"data/{element}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
            file += 1
    
    time.sleep(2)

browser.quit()
