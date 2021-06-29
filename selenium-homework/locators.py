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

driver.get("http://localhost:9999/kitchensink.html")

# Keresés ID alapján
find_id = driver.find_element_by_id("mousehover")
print(find_id.get_attribute("class"))
# driver.close()

# Keresés NAME alapján
find_name = driver.find_element_by_name("multiple-select-example")
print(find_name.text)
# driver.close()

# Keresés XPATH kifejezéssel
find_xpath = driver.find_element_by_xpath('//*[@id="hide-textbox"]')
print(find_xpath.get_attribute("value"))
# driver.close()
