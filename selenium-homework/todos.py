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

driver.get("http://localhost:9999/todo.html")

todo_list = driver.find_elements_by_xpath("//li")

for element in todo_list:
    print(element.text)
