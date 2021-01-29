from selenium.webdriver.common.by import By
from utilities.CustomLogger import LogGen


class LoginPage():

    username ="input[name='login']"
    password ="#password"
    loginButton="button.v-btn.theme--light"

    #Logger
    logger=LogGen.loggen()

    def __init__(self,driver):
        self.driver=driver

    def logIn(self,username,password,testcasename):
        ele_user = self.driver.find_element_by_css_selector(self.username)
        ele_user.click()
        self.logger.info("****--testcasename-"+testcasename+"---**** Clicked on login button")
        ele_user.send_keys(username)
        self.logger.info("****--testcasename-"+testcasename+"---****Entered username "+username)
        ele_password = self.driver.find_element_by_css_selector(self.password)
        ele_password.click()
        ele_password.send_keys(password)
        self.logger.info("****--testcasename-"+testcasename+"---****Entered password " + password)
        ele_login = self.driver.find_element_by_css_selector(self.loginButton)
        ele_login.click()

