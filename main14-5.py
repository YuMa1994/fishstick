from selenium import webdriver
from time import sleep
from datetime import datetime, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

file = open('log.txt', 'w')
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

driver.get('https://html5css.ru/howto/howto_js_rangeslider.php')
driver.maximize_window()

# End of setup


slider = driver.find_element(By.XPATH, '//*[@id="id2"]')
action = ActionChains(driver)
sleep(2)
action.click_and_hold(slider).move_by_offset(-500, 0).release().perform()



file.close()
#driver.quit()

