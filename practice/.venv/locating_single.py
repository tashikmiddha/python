from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()
# element=input("enter the element")
# for i in range(20):
browser.get(f"https://www.amazon.in/s?k={"phone"}&page={1}&xpid=NysdkkEjXE2zm&crid=K2CZSURF13DRqid=1741697831&sprefix=laptop%2Caps%2C308&ref=sr_pg_2")
ele=browser.find_element(By.CLASS_NAME,"puis-card-container")
print(ele.get_attribute("outerHTML"))
time.sleep(2)
browser.close()