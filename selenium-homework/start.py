from selenium import webdriver
from bmodul import my_text

driver = webdriver.Chrome()

driver.get("https://python.org")

q = driver.find_element_by_name("q")
q.send_keys(my_text)

submit = driver.find_element_by_name("submit")
submit.click()

# driver.close()