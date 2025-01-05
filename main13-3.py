import fileinput

from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
#driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

# End of setup


# Sc functions ------------

def set_up():
    driver.get('http://saucedemo.com/')
    driver.maximize_window()

def login():
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('standard_user')
    file.write("Success login input \n")

    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('secret_sauce')
    file.write("Success password input \n")

    driver.find_element(By.XPATH, '//input[@id="login-button"]').click()
    file.write("Success login click \n")

def login_with_enter():
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('standard_user')
    file.write("Success login input \n")

    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('secret_sauce')
    file.write("Success password input \n")

    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(Keys.ENTER)
    file.write("Success Enter \n")

def fake_login():
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('standard_user')
    file.write("Success login input \n")

    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('secret_sauce1')
    file.write("Success fake password input \n")

    driver.find_element(By.XPATH, '//input[@id="login-button"]').click()
    file.write("Success login click \n")

def refresh_page():
    driver.refresh()

# End of Sc functions ------------



# Tests

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

def test_fake_login_label():
    correct_text = 'Epic sadface: Username and password do not match any user in this service'
    current_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert correct_text == current_text.text, 'test_fake_login_label is FAILED'
    file.write('test_fake_login_label is OK\n')

# End of tests


# Main block

def sc_fake_login():
    file.write('    FAKE login test results: \n')
    set_up()
    fake_login()

    test_fake_login_label()

    file.write('\n')

def sc_real_login():
    file.write('    REAL login test results: \n')
    set_up()
    login()

    test_login_redirect()
    test_context_after_login_is_correct()

    file.write('\n')

def sc_real_login_with_enter():
    file.write('    REAL login with ENTER test results: \n')
    set_up()
    login_with_enter()

    test_login_redirect()
    test_context_after_login_is_correct()

    file.write('\n')

# sc_fake_login()
# sc_real_login()
sc_real_login_with_enter()

file.close()
driver.quit()

