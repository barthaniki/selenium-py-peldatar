import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    URL = "http://localhost:9999/simplevalidation.html"
    driver.get(URL)

    inputs = driver.find_elements_by_xpath('//*[@class="validate-input"]')
    val_msg = WebDriverWait(driver, 2).until(
        ec.invisibility_of_element_located((By.CLASS_NAME, "validate-field-error-message"))
    )

    for i in inputs:
        i.click()
        time.sleep(0.5)
        assert val_msg is not None

    ch_boxes = driver.find_elements_by_xpath('//*[@type="checkbox"]')
    val_ch_msg = WebDriverWait(driver, 2).until(
        ec.visibility_of_element_located((By.CLASS_NAME, "validate-field-error-message"))
    )

    for ch in ch_boxes:
        ch.send_keys("\t")
        time.sleep(0.5)
        assert val_msg is not None

finally:
    pass
    driver.close()
