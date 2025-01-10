from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

file = open('log.txt', 'w')
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/buttons')
driver.maximize_window()


action = ActionChains(driver)

def double_click_button():
    action.double_click(driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')).perform()

def right_click_button():
    action.context_click(driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')).perform()

def standard_click_button():
    action.click(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')).perform()


# Tests

def test_double_click_button():
    assert driver.find_element(By.XPATH, '//*[@id="doubleClickMessage"]').text == "You have done a double click",\
        "test_double_click_button is FAILED"
    file.write("test_double_click_button is OK \n")

def test_right_click_button():
    assert driver.find_element(By.XPATH, '//*[@id="rightClickMessage"]').text == "You have done a right click",\
        "test_right_click_button is FAILED"
    file.write("test_right_click_button is OK \n")

def test_standard_click_button():
    assert driver.find_element(By.XPATH, '//*[@id="dynamicClickMessage"]').text == "You have done a dynamic click",\
        "test_standard_click_button is FAILED"
    file.write("test_standard_click_button is OK \n")


double_click_button()
test_double_click_button()
right_click_button()
test_right_click_button()
standard_click_button()
test_standard_click_button()

file.close()
#driver.quit()

