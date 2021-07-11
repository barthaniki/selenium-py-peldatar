import time
from datetime import datetime, date

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/forms.html")

my_date = date(2021, 5, 6)
driver.find_element_by_id("example-input-date").send_keys(my_date.strftime("%Y\t%m%d"))

date_time = datetime(2012, 5, 5, hour=5, minute=5, second=5, microsecond=555)
driver.find_element_by_id("example-input-date-time").send_keys(date_time.strftime('%Y.%m.%d %H:%M:%S:%f'))

date_local = datetime(2000, 5, 12, hour=12, minute=1)
driver.find_element_by_id("example-input-date-time-local").send_keys(date_local.strftime('%Y\t%m%d%H%M'))

date_month = "00199512"
driver.find_element_by_id("example-input-month").send_keys(date_month)

date_week = "522015"
driver.find_element_by_id("example-input-week").send_keys(date_week)

date_time = "0025"
driver.find_element_by_id("example-input-time").send_keys(date_time)

time.sleep(4)
driver.close()
