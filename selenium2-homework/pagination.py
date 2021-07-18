import pprint

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

extracted = []

try:
    URL = "http://localhost:9999/pagination.html"
    driver.get(URL)
    while True:
        table = driver.find_element_by_xpath('//*[@id="contacts-table"]/tbody')
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text

            for key, value in data_row.items():
                if "first_name" in key and "A" in value:
                    extracted.append(data_row)
                else:
                    pass
        next_btn = driver.find_element_by_id("next")
        if not next_btn.is_enabled():
            break
        else:
            next_btn.click()
finally:
    driver.close()

# pprint.pprint(extracted)

with open("p_extracted.csv", "w") as csv_file:
    lines = str(extracted).replace(", ", "\n")
    for line in lines:
        csv_file.write(line)
