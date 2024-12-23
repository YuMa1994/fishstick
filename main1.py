from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://saucedemo.com/')
driver.maximize_window()

user_name = driver.find_element(By.ID, 'user-name')
login = 'standard_user'
user_name.send_keys(login)


sleep(5)

