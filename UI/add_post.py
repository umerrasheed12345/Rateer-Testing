from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from time import sleep
from faker import Faker
fake = Faker()
test_users = [
    "SELENIUM_TEST",
    "Lois_Lane",
    "Clark_Kent",
    "Jenny_Flex",
]
DELAY = 3


def signin(driver, username, password):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+ "/home/signin/" +'"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "username" +'"]').send_keys(username)
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "password" +'"]').send_keys(password)
        driver.find_element(by=By.XPATH, value='//button[@type="'+ "submit" +'"]').submit()
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}'\
            .format(
            'https://rateer.pythonanywhere.com/home/signin/',
            'Attempting to input',
            'Clicking submit',
            'Test Failed! Details:'+str(e)))


def add_post(driver, caption, file_path):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+ "/posts/" +'"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "caption" +'"]').send_keys(caption)
        driver.find_element(by=By.XPATH, value='//input[@id="'+ "files" +'"]').send_keys(os.getcwd() + "/" + file_path)
        driver.find_element(by=By.XPATH, value='//button[@type="'+ "submit" +'"]').submit()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}'\
            .format(
            'https://rateer.pythonanywhere.com/posts/',
            'Attempting to input caption and upload file',
            'Clicking submit'))
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//h4[contains(text(), \'' + caption + '!\')]').text
            print('\
            Then: Test Passed -- {}\n'\
            .format(
            ui_res))
        except Exception as e:
            print('\
            Then: Test Failed -- {}\n'\
            .format(
            str(e)))        
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}'\
            .format(
            'https://rateer.pythonanywhere.com/posts/',
            'Attempting to input caption and upload file',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://rateer.pythonanywhere.com/')
        driver.maximize_window()
    except Exception as e:
        print(str(e))
        exit(1)

    print("Starting test [Add Post]")
    signin(driver, test_users[0], test_users[0])
    add_post(driver, "Weather is best in spring", "sample.jpeg")
    print("Finished test [Add Post]")
    driver.quit()