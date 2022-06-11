from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
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


def del_post(driver, post_id):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+ "/posts/" +'"]').click()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}{}{}\n\
            When: {}'\
            .format(
            'https://rateer.pythonanywhere.com/posts/',
            'Attempting to delete a post. Xpath expression: //form[@class="DeleteForm"]/div/button[@value=',
            str(post_id),
            ']',
            'Clicking submit'))
        try:
            driver.find_element(by=By.XPATH, value='//form[@class="DeleteForm"]/div/button[@value=' + str(post_id) + ']').click()
            print('\
            Then: Test Passed -- Post Deleted\n')
        except Exception as e:
            print('\
            Then: Test Failed -- Post does not exist. Details:{}]\n'
            .format(str(e)))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}{}{}\n\
            When: {}\n\
            Then: {}'\
            .format(
            'https://rateer.pythonanywhere.com/posts/',
            'Attempting to delete a post. Xpath expression: //form[@class="DeleteForm"]/div/button[@value=',
            str(post_id),
            ']',
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

    print("Starting test [Del Post]")
    signin(driver, test_users[2], test_users[2])
    del_post(driver, 1)
    print("Finished test [Del Post]")
    driver.quit()
