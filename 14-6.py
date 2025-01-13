from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

file = open('log.txt', 'w')
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

driver.get('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
driver.maximize_window()

# End of setup

sleep(1)

click_drop = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[1]/div[2]/span/span[1]/span')
click_drop.click()
drop_box = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
drop_box.send_keys("Denmark")
sleep(1)
drop_box.send_keys(Keys.ENTER)


file.close()
#driver.quit()
