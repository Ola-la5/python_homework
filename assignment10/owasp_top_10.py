#task6
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")


list_10 = []


li_elem = driver.find_elements(By.XPATH, "//ul/li[a/strong]")  

for li in li_elem:  
    a_tag = li.find_element(By.TAG_NAME, "a")
    title = a_tag.find_element(By.TAG_NAME, "strong").text.strip()
    link = a_tag.get_attribute("href")
    list_10.append({"title": title, "link": link})

# for debugging
print(list_10)

with open('owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    for item in list_10:
        writer.writerow([item["title"], item["link"]])

driver.quit()