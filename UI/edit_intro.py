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

def edit_intro(driver, age, address, phonenum, profession, status):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+ "editintro/" +'"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Age" +'"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Age" +'"]').send_keys(age)
        
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Address" +'"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Address" +'"]').send_keys(address)
        
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Phone" +'"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Phone" +'"]').send_keys(phonenum)
        
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Profession" +'"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Profession" +'"]').send_keys(profession)

        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Status" +'"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "Status" +'"]').send_keys(status)

        driver.find_element(by=By.XPATH, value='//button[@type="'+ "submit" +'"]').submit()

        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n'\
            .format(
            'https://rateer.pythonanywhere.com/dashboard/editintro/',
            'Attempting to input Age, Address, Phone, Profession, Status.',
            'Clicking submit'))
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//h2[contains(text(), \'Intro Information Updated!\')]').text
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
            'https://rateer.pythonanywhere.com/dashboard/editintro/',
            'Attempting to input Age, Address, Phone, Profession, Status.',
            'Clicking submit',
            'Test Failed! --- ' + str(e)))

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

    print("Starting test [Edit Intro]")
    signin(driver, test_users[0], test_users[0])
    edit_intro(driver, "25", "110 London Street", "+1-777-777-888", "Senior Consulant", "Alive")
    print("Finished test [Edit Intro]")
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)  