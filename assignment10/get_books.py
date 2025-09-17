#task1
#Since we have rule 
#User-agent: *
#Disallow: /staff/
#we can scrape everything, but section /staff/

#task3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import csv
from time import sleep

#task2
CONTAINER = "li.row.cp-search-result-item"
TITLE = "span.title-content"
AUTHOR = "a.author-link"
PUBLISHED_YEAR = "span.display-info-primary"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    sleep(15)

    results=[]
    li_elem=driver.find_elements(By.CSS_SELECTOR, CONTAINER)
    print(f"got {len(li_elem)} results")

    for elem in li_elem:
        try:
            title=elem.find_element(By.CSS_SELECTOR, TITLE).text.strip()
        except:
            title="N/A"

        try:
            authors = [a.text.strip() for a in elem.find_elements(By.CSS_SELECTOR, AUTHOR) if a.text.strip() ]
            author="; ".join(authors) if authors else "N/A"
        except:
            author = "N/A"

        try:
            format_year = elem.find_element(By.CSS_SELECTOR, PUBLISHED_YEAR).text.strip()
        except:
            format_year = "N/A"

        results.append({"Title": title,
                        "Author": author,
                        "Format-Year": format_year})  
    df=pd.DataFrame(results)
    print(df)   
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")
finally:
    driver.quit()           

#task4
with open('get_books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Format-Year"])
    for result in results:
        writer.writerow([result["Title"], result["Author"], result["Format-Year"]])  

data = {"result": results}
with open('get_books.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
print("Created: get_books.csv and get_books.json")