# Implementation of Selenium WebDriver with Python using PyTest
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
DELAY = 2

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

def find_friend(driver, username):
    # Find friend
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+ "/friends/search/" +'"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "queryname" +'"]').send_keys(username)
        driver.find_element(by=By.XPATH, value='//button[@type="'+ "submit" +'"]').submit()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}'\
            .format(
            'https://rateer.pythonanywhere.com/friends/find/',
            'Attempting to Find Friends',
            'Clicking submit'))        
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//b[contains(text(), \'' + username + '\')]').text
            print('\
            Then: Test Passed -- User Found -- {}\n'\
            .format(
            ui_res))
        except Exception as e:
            print('\
            Then: Test Failed -- User Not Found-- {}\n'\
            .format(
            str(e)))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}'\
            .format(
            'https://rateer.pythonanywhere.com/friends/find/',
            'Attempting to input data',
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

    print("Starting test [Find Friends]")
    signin(driver, test_users[0], test_users[0])
    find_friend(driver, "Jenny_Flex")
    print("Finished test [Find Friends]")
    sleep(DELAY)
    sleep(DELAY)