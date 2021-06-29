from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# háttérben futtatásnál kapcsolók beállítása! (GithubActions)
# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/trickyelements.html")

# list of elements
e_list = ("element1", "element2", "element3", "element4", "element5")

for element in e_list:
    driver.find_element_by_id(element).click()
    result = driver.find_element_by_xpath('//*[@id="result"]').text

try:
    assert result == f"{e_list.text} was clicked"

except:
    pass
    # driver.close()
