import fileinput

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
driver = webdriver.Chrome()

def set_up():
    driver.get('http://saucedemo.com/')
    driver.maximize_window()

def login():
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('standard_user')
    file.write("Success login input \n")

    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('secret_sauce')
    file.write("Success password input \n")

    sleep(3)

    driver.find_element(By.XPATH, '//input[@id="login-button"]').click()
    file.write("Success login click \n")

def test_login_redirect():
    correct_url = 'https://www.saucedemo.com/inventory.html'
    get_url = driver.current_url
    assert correct_url == get_url, 'test_login_redirect is FAILED'
    file.write('test_login_redirect is OK \n')

def test_context_after_login_is_correct():
    correct_text = 'Products'
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text == current_text.text, 'test_context_after_login_is_correct is FAILED'
    file.write('test_context_after_login_is_correct is OK\n')


#main block
set_up()
login()

test_login_redirect()
test_context_after_login_is_correct()

sleep(5)

file.close()
driver.quit()

