from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

webdriverwait=5

class ModifyUser():


    def __init__(self,driver):
        self.driver=driver

    def deactivateuser(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Manage Users')]")))
        ele_createUser = self.driver.find_element_by_xpath("//div[contains(text(),'Manage Users')]")
        ele_createUser.click()
        ele_edit = self.driver.find_element_by_css_selector("//i[contains(text(),'edit')]")
        value = randint(1, 10000)
        ele_uncheck = self.driver.find_element_by_css_selector("//i[contains(text(),'check_box_outline_blank')]")
        ele_uncheck.click()
        ele_Save=self.driver.find_element_by_css_selector("//div[contains(text(),' Save ')]")
        ele_Save.click()








