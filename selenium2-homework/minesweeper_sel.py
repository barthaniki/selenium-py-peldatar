import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/minesweeper-game.html")

covered = driver.find_elements_by_class_name("covered")

if covered:
    for i in covered[-1::-8]:
        i.click()
else:
    for j in covered:
        j.click()

time.sleep(2)
driver.close()
