from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from utilities.CustomLogger import LogGen

webdriverwait=5

class ChangePassword():


    def __init__(self,driver):
        self.driver=driver


    logger = LogGen.loggen()
    def changepassword(self,emailuser,testcasename):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Change Password')]")))
        ele_createUser = self.driver.find_element_by_xpath("//div[contains(text(),'Change Password')]")
        ele_createUser.click()
        self.logger.info("****--testcasename-" + testcasename + "---**** Clicked on changepassword link");
        ele_changepwd = self.driver.find_element_by_css_selector("input[aria-label='Password']")
        ele_changepwd.click()
        ele_changepwd.send_keys("pwd123456")
        self.logger.info("****--testcasename-" + testcasename + "---**** Entered password as pwd123456");
        ele_confirmchangepwd = self.driver.find_element_by_css_selector("input[aria-label='Confirm Password']")
        ele_confirmchangepwd.click()
        ele_confirmchangepwd.send_keys("pwd123456")
        self.logger.info("****--testcasename-" + testcasename + "---**** Entered confirmpassword as pwd123456");
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Save')]")))
        ele_createusersave = self.driver.find_element_by_xpath("//div[contains(text(),'Save')]")
        ele_createusersave.click()
        self.logger.info("****--testcasename-" + testcasename + "---**** successfully changed password");
        logoutImg = self.driver.find_element_by_xpath("//i[contains(text(),'more_vert')]")
        logoutImg.click()
        logoutlink = self.driver.find_element_by_xpath("//div[contains(text(),'Logout')]")
        logoutlink.click()
    def validateChangePassword(self,emailuser,testcasename):
        ele_user = self.driver.find_element_by_css_selector("input[name='login']")
        self.logger.info("****--testcasename-" + testcasename + "---**** validated changpassword functionality successfully");
        ele_user.click()
        username = emailuser.split('@')
        ele_user.send_keys(emailuser)
        ele_password = self.driver.find_element_by_css_selector("#password")
        ele_password.click()
        ele_password.send_keys("pwd123456")
        ele_login = self.driver.find_element_by_css_selector("button.v-btn.theme--light")
        ele_login.click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'" + username[0] + "')]")))
        ele_dashboardloginuser = self.driver.find_element_by_xpath("//div[contains(text(),'" + username[0] + "')]")
        assert ele_dashboardloginuser.is_displayed()
        self.logger.info("****--testcasename-" + testcasename + "---**** validated changpassword functionality successfully");



