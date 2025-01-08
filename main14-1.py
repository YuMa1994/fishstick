from selenium import webdriver
from time import sleep
import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

file = open('log.txt', 'w')
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/checkbox')
driver.maximize_window()

def expand_list_click():
    expand_list_button = driver.find_element(By.XPATH, '//*[@id="tree-node"]/div/button[1]')
    expand_list_button.click()

def home_check_box_click():
    home_check_box = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]')
    home_check_box.click()


# Tests

def test_context_after_expand_list():
    lowest_list_element_text = 'Excel File.doc'
    current_text = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]/span/label/span[3]')
    assert lowest_list_element_text == current_text.text, 'test_context_after_expand_list if FAILED'
    file.write('test_context_after_expand_list is OK \n')

def test_context_after_home_checkbox_click():
    correct_text = 'You have selected :'
    current_text = driver.find_element(By.XPATH, '//*[@id="result"]/span[1]')
    assert correct_text == current_text.text, 'test_context_after_home_checkbox_click is FAILED'
    file.write('test_context_after_home_checkbox_click is OK')

expand_list_click()
test_context_after_expand_list()
home_check_box_click()
test_context_after_home_checkbox_click()

file.close()
#driver.quit()

