from curses.ascii import DEL
from unittest import FunctionTestCase
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from faker import Faker     #   for random data input
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

def del_hobby(driver, hobby):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+ "delhobby/" +'"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Hobby" +'"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Hobby" +'"]').send_keys(hobby)
        driver.find_element(by=By.XPATH, value='//button[@type="'+ "submit" +'"]').submit()
        # check if hobby was del successfully
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}'\
            .format(
            'rateer.pythonanywhere.com/dashboard/delhobby/',
            'Attempting to input hobby: ' + hobby,
            'Clicking submit'))
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//h2[contains(text(), \'Hobby Deleted!\')]').text
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
            'rateer.pythonanywhere.com/dashboard/delhobby/',
            'Attempting to input hobby: ' + hobby,
            'Clicking submit',
            'Test Failed! Details:'+str(e)))

    sleep(DELAY)
    driver.find_element(by=By.XPATH, value='//a[@href="'+ "/dashboard/" +'"]').click()

if __name__ == '__main__':
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://rateer.pythonanywhere.com/')
        driver.maximize_window()
    except Exception as e:
        print(str(e))
        exit(1)

    print("Starting test [Remove Hobby]")
    signin(driver, test_users[0], test_users[0])
    del_hobby(driver, "Table Tennis")
    print("Finished test [Remove Hobby]")
    sleep(DELAY)
    sleep(DELAY)  