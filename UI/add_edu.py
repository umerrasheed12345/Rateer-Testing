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


def add_edu(driver, degree, institute, from_date, till_date):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+ "addeducation/" +'"]').click()
        driver.find_element(by=By.XPATH, value='//input[@id="'+ "id_Degree" +'"]').send_keys(degree)
        driver.find_element(by=By.XPATH, value='//input[@id="'+ "id_Institute" +'"]').send_keys(institute)
        driver.find_element(by=By.XPATH, value='//input[@id="'+ "id_From" +'"]').send_keys(from_date)
        driver.find_element(by=By.XPATH, value='//input[@id="'+ "id_Till" +'"]').send_keys(till_date)
        driver.find_element(by=By.XPATH, value='//button[@type="'+ "submit" +'"]').submit()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}'\
            .format(
            'https://rateer.pythonanywhere.com/dashboard/addeducation/',
            'Attempting to input Computer Sciences (Selenium)',
            'Clicking submit'))
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//h2[contains(text(), \'Certification Added!\')]').text
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
            'https://rateer.pythonanywhere.com/dashboard/addeducation/',
            'Attempting to input Computer Sciences (Selenium)',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))

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

    print("Starting test [Add Education]")
    signin(driver, test_users[0], test_users[0])
    add_edu(driver, "Computer Sciences (Selenium)", "ITU University LHR", "05-05-2020", "10-10-2022")
    print("Finished test [Add Education]")
    driver.quit()