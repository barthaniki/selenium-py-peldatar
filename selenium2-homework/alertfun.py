import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "http://localhost:9999/alert_playground.html"
driver.get(URL)

alert_btn = driver.find_element_by_name("alert").click()
alert = driver.switch_to.alert
time.sleep(2)
alert.accept()

confirmation_btn = driver.find_element_by_name("confirmation").click()
time.sleep(2)
alert.accept()

prompt_btn = driver.find_element_by_name("prompt").click()
time.sleep(2)
prompt_message = "alert message"
alert.send_keys(prompt_message)
alert.accept()
assert driver.find_element_by_tag_name("p").text == f"You entered: {prompt_message}"

action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()
time.sleep(2)
alert.accept()

driver.close()
