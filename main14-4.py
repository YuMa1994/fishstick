from selenium import webdriver
from time import sleep
from datetime import datetime, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/date-picker')
driver.maximize_window()

# End of setup


date_input = driver.find_element(By.XPATH,'//*[@id="datePickerMonthYearInput"]')
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.DELETE)
sleep(1)

current_date = datetime.now()
future_date = (current_date + timedelta(days=10)).strftime("%m.%d.%Y")
date_input.send_keys(future_date)
date_input.send_keys(Keys.ENTER)



file.close()
#driver.quit()

