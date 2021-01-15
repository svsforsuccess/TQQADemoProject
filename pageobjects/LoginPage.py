from utilities.CustomLogger import LogGen


class LoginPage():

    logger=LogGen.loggen()
    def __init__(self,driver):
        self.driver=driver

    def logIn(self):
        ele_user = self.driver.find_element_by_css_selector("input[name='login']")
        ele_user.click()
        self.logger.info("Clicked on login button")
        ele_user.send_keys("admin@tqqademoproject.com")
        ele_password = self.driver.find_element_by_css_selector("#password")
        ele_password.click()
        ele_password.send_keys("changethis")
        ele_login = self.driver.find_element_by_css_selector("button.v-btn.theme--light")
        ele_login.click()

