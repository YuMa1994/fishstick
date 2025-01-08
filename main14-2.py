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

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()

def yes_radio_button_click():
    yes_radio = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/label')
    yes_radio.click()



# Tests

def test_yes_radio_button_is_selected():
    correct_text = 'Yes'
    current_text = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p/span')
    assert correct_text == current_text.text, 'test_yes_radio_button_is_selected if FAILED'
    file.write('test_yes_radio_button_is_selected is OK \n')


yes_radio_button_click()
test_yes_radio_button_is_selected()


file.close()
#driver.quit()

