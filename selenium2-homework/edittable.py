import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "http://localhost:9999/editable-table.html"
driver.get(URL)

add_btn = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/button')
add_btn.click()

name7 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[7]/td[1]/input').send_keys("chair")
price7 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[7]/td[2]/input').send_keys(
    "12.99")
quantity7 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[7]/td[3]/input')
quantity7.clear()
quantity7.send_keys("12")
category7 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[7]/td[4]/input')
category7.send_keys("Furniture")

add_btn.click()

name8 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[8]/td[1]/input').send_keys("table")
price8 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[8]/td[2]/input').send_keys(
    "25.99")
quantity8 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[8]/td[3]/input')
quantity8.clear()
quantity8.send_keys("4")
category8 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[8]/td[4]/input')
category8.send_keys("Furniture")
time.sleep(1)

search = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/input')
search.send_keys("iPhone 5")
time.sleep(1)
search.send_keys(Keys.BACKSPACE * 8)
time.sleep(1)

price6 = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/table/tbody/tr[6]/td[2]/input')
price6.clear()
price6.send_keys("179.99")

assert price6.get_attribute("value") == "179.99"

driver.close()
