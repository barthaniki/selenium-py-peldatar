from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999")

with open("links.txt", "w") as file1:
    links = driver.find_elements_by_xpath("//a")
    l_links = []
    for link in links:
        l_links.append(link.text)
    l2 = str(l_links).replace(", ", "\n")
    file1.write(l2)

print("Numbers of links: ", len(l_links))

driver.close()
