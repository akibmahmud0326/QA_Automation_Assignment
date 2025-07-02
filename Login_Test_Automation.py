from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver


def login_with_id():
    driver = setup_driver()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)
    driver.quit()

def login_with_xpath():
    driver = setup_driver()

    username_xpath = "//input[@data-test='username' and @name='user-name']"
    password_xpath = "//input[@data-test='password' and @name='password']"
    login_button_xpath = "//input[@data-test='login-button' and @type='submit']"

    driver.find_element(By.XPATH, username_xpath).send_keys("standard_user")
    driver.find_element(By.XPATH, password_xpath).send_keys("secret_sauce")
    driver.find_element(By.XPATH, login_button_xpath).click()

    time.sleep(3)
    driver.quit()


def main():
    login_with_id()


main()