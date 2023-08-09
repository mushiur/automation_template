import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver, locator):
        self.driver = driver
        self.user_name = locator["LOCATORS"]["user_email"]
        self.user_password = locator["LOCATORS"]["user_password"]
        self.sign_button = locator["LOCATORS"]["sign_in_button"]

    def user_login(self, user_data):
        """
            Enter Username
        """
        userID = self.driver.find_element("xpath", self.user_name)
        userID.click()
        userID.send_keys(user_data['userName'])
        time.sleep(1)
        # self.driver.find_element("xpath", self.user_name).send_keys(invex1['userName'])

        """
             Enter Password
        """
        passWord = self.driver.find_element("xpath", self.user_password)
        passWord.click()
        passWord.send_keys(user_data['userPassword'])
        time.sleep(1)
        self.driver.find_element("xpath", self.sign_button).click()
        time.sleep(10)
