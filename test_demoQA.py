from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains



@pytest.fixture
# @pytest.fixture(scope="module") - to make test in one browser session
def browser():
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get("https://demoqa.com/")
    yield driver
    driver.quit()

def test_textbox_form(browser):
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    browser.find_element(By.XPATH,'//*[@id="item-0"]').click()
    form = browser.find_element(By.ID, 'userForm')
    form.find_element(By.ID, 'userName').send_keys('John Test')
    form.find_element(By.ID, 'userEmail').send_keys('test@test.com')
    form.find_element(By.ID, 'currentAddress').send_keys("my current address is in Bubu's heart")
    form.find_element(By.ID, 'permanentAddress').send_keys("my current address is in Bubu's heart")
    browser.execute_script("window.scrollTo(0, 1000);")
    form.find_element(By.ID, 'submit').click()
    form_output = form.find_element(By.ID,'output')
    name = form_output.find_element(By.ID,'name')
    name = name.text
    assert name == 'Name:John Test'

def test_checkbox_1(browser):
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    browser.find_element(By.XPATH,'//*[@id="item-1"]').click()
    browser.find_element(By.CLASS_NAME, 'rct-checkbox').click()

    result = browser.find_element(By.ID,'result')
    result = result.text
    assert isinstance(result, str)

def test_checkbox_2(browser):
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    browser.find_element(By.XPATH,'//*[@id="item-1"]').click()
    browser.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/button').click()
    browser.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[2]/span/button').click()
    browser.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()
    browser.execute_script("window.scrollTo(0, 1000);")
    browser.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[3]').click()
    result = browser.find_element(By.ID,'result')
    result = result.text
    assert isinstance(result, str)

def test_radioButton_yes(browser):
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    browser.find_element(By.XPATH,'//*[@id="item-2"]').click()
    browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label').click()
    result = browser.find_element(By.CLASS_NAME,'text-success').text
    assert result == 'Yes'

def test_radioButton_impressive(browser):
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    browser.find_element(By.XPATH,'//*[@id="item-2"]').click()
    browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]').click()
    result = browser.find_element(By.CLASS_NAME,'text-success').text
    assert result == 'Impressive'

def test_radioButton_changeRespond(browser):
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    browser.find_element(By.XPATH,'//*[@id="item-2"]').click()
    browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label').click()
    browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]').click()
    result = browser.find_element(By.CLASS_NAME,'text-success').text
    assert result == 'Impressive'

def test_buttonsClicks(browser):
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    browser.execute_script("window.scrollTo(0, 500);")
    browser.find_element(By.XPATH,'//*[@id="item-4"]').click()
    elementDoubleClick = browser.find_element(By.ID, 'doubleClickBtn')
    action_chains = ActionChains(browser)
    action_chains.double_click(elementDoubleClick).perform()

    elementRightClick = browser.find_element(By.ID, 'rightClickBtn')
    action_chains.context_click(elementRightClick).perform()
    browser.find_element(By.XPATH, '//button[text()="Click Me"]').click()

    def result():
        if browser.find_element(By.ID,'doubleClickMessage').text == 'You have done a double click' and browser.find_element(By.ID,'rightClickMessage').text == 'You have done a right click' and browser.find_element(By.ID,'dynamicClickMessage').text == 'You have done a dynamic click':
            return True

    assert result() == True

