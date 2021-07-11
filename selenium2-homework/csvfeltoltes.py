import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/another_form.html")


def find_and_clear_by_id(element_id):
    element = driver.find_element_by_id(element_id)
    element.clear()
    return element


submit = driver.find_element_by_id("submit")
export = driver.find_element_by_xpath("//*[contains(text(), 'Export HTML table to CSV file')]")

with open("table_in.csv", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        find_and_clear_by_id("fullname").send_keys(row[0])
        find_and_clear_by_id("email").send_keys(row[1].replace(" ", ""))
        find_and_clear_by_id("dob").send_keys(row[2])
        find_and_clear_by_id("phone").send_keys(row[3].replace(" 0", "0"))
        submit.click()

export.click()

driver.close()
