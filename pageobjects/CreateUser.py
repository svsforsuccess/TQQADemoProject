from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

from pageobjects.LoginPage import LoginPage

webdriverwait=5

class CreateUser():


    def __init__(self,driver):
        self.driver=driver


    def createuser(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Create User')]")))
        ele_createUser = self.driver.find_element_by_xpath("//div[contains(text(),'Create User')]")
        ele_createUser.click()
        ele_fullName = self.driver.find_element_by_css_selector("input[aria-label='Full Name']")
        value = randint(1, 10000)
        ele_fullName.send_keys('admin' + str(value))
        ele_createuseremail = self.driver.find_element_by_css_selector("input[type='email']")
        ele_createuseremail.send_keys('admin' + str(value) + '@tqqaproject.com')
        ele_createuserpassword = self.driver.find_element_by_css_selector("input[aria-label='Set Password']")
        ele_createuserpassword.send_keys('password')
        ele_createuserconfirmpassword = self.driver.find_element_by_css_selector("input[aria-label='Confirm Password']")
        ele_createuserconfirmpassword.send_keys('password')
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Save')]")))
        ele_createusersave = self.driver.find_element_by_xpath("//div[contains(text(),'Save')]")
        ele_createusersave.click()
        # ele_rightdisabledarw=
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Next page']")))
            ele_rightenabledarw = self.driver.find_element_by_css_selector("button[aria-label='Next page']")
            while ele_rightenabledarw.is_displayed:
                ele_rightenabledarw.click()
                if len(self.driver.find_elements_by_css_selector(
                        "button[aria-label='Next page'][disabled='disabled']")) > 0:
                    break
        except TimeoutException as ex:
            print(ex.msg)
        ele_manageuser = self.driver.find_elements_by_xpath("//table[@class='v-datatable v-table theme--light']//tbody/tr")
        cnt = len(ele_manageuser)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//table[@class='v-datatable v-table theme--light']//tbody/tr[" + str(cnt) + "]/td[2]")))
        email = self.driver.find_element_by_xpath(
            "//table[@class='v-datatable v-table theme--light']//tbody/tr[" + str(cnt) + "]/td[2]")
        print(email.text)
        emailuser = 'admin' + str(value) + '@tqqaproject.com'
        print(str(email.text))
        print('*****'+emailuser+'*****'+str(email.text))
        assert emailuser.__eq__(str(email.text))

        fnameele = self.driver.find_element_by_xpath(
            "//table[@class='v-datatable v-table theme--light']//tbody/tr[" + str(cnt) + "]/td[3]")
        print(fnameele.text)
        fnameval = 'admin' + str(value)
        print(str(fnameval))
        print(emailuser)
        assert fnameval.__eq__(str(fnameele.text))
        logoutImg = self.driver.find_element_by_xpath("//i[contains(text(),'more_vert')]")
        logoutImg.click()
        logoutlink = self.driver.find_element_by_xpath("//div[contains(text(),'Logout')]")
        logoutlink.click()
        ele_user = self.driver.find_element_by_css_selector("input[name='login']")
        ele_user.click()
        ele_user.send_keys(emailuser)
        ele_password = self.driver.find_element_by_css_selector("#password")
        ele_password.click()
        ele_password.send_keys("password")
        ele_login = self.driver.find_element_by_css_selector("button.v-btn.theme--light")
        ele_login.click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'" + fnameval + "')]")))
        ele_dashboardloginuser = self.driver.find_element_by_xpath("//div[contains(text(),'" + fnameval + "')]")
        assert ele_dashboardloginuser.is_displayed()
        logoutImg = self.driver.find_element_by_xpath("//i[contains(text(),'more_vert')]")
        logoutImg.click()
        logoutlink = self.driver.find_element_by_xpath("//div[contains(text(),'Logout')]")
        logoutlink.click()
        ele_user = self.driver.find_element_by_css_selector("input[name='login']")
        ele_user.click()
        ele_user.send_keys(emailuser)
        ele_password = self.driver.find_element_by_css_selector("#password")
        ele_password.click()
        ele_password.send_keys("password")
        ele_login = self.driver.find_element_by_css_selector("button.v-btn.theme--light")
        ele_login.click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Change Password')]")))
        ele_createUser = self.driver.find_element_by_xpath("//div[contains(text(),'Change Password')]")
        ele_createUser.click()
        ele_changepwd = self.driver.find_element_by_css_selector("input[aria-label='Password']")
        ele_changepwd.click()
        ele_changepwd.send_keys("pwd")
        ele_confirmchangepwd = self.driver.find_element_by_css_selector("input[aria-label='Confirm Password']")
        ele_confirmchangepwd.click()
        ele_confirmchangepwd.send_keys("pwd")
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Save')]")))
        ele_createusersave = self.driver.find_element_by_xpath("//div[contains(text(),'Save')]")
        ele_createusersave.click()
        logoutImg = self.driver.find_element_by_xpath("//i[contains(text(),'more_vert')]")
        logoutImg.click()
        logoutlink = self.driver.find_element_by_xpath("//div[contains(text(),'Logout')]")
        logoutlink.click()
        ele_user = self.driver.find_element_by_css_selector("input[name='login']")
        ele_user.click()
        ele_user.send_keys(emailuser)
        ele_password = self.driver.find_element_by_css_selector("#password")
        ele_password.click()
        ele_password.send_keys("pwd")
        ele_login = self.driver.find_element_by_css_selector("button.v-btn.theme--light")
        ele_login.click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'" + fnameval + "')]")))
        ele_dashboardloginuser = self.driver.find_element_by_xpath("//div[contains(text(),'" + fnameval + "')]")
        assert ele_dashboardloginuser.is_displayed()





