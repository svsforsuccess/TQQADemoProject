import pytest
import allure
from  pageobjects.LoginPage import LoginPage
from  pageobjects.ChangePasswordPage import ChangePassword
from utilities.CustomLogger import LogGen
from utilities.ReadProperties import  ReadConfig


@pytest.mark.usefixtures("setup")
class TestCreateUser():

    logger = LogGen.loggen()
    @allure.feature("ChangePassword")
    @allure.severity('Critical')
    def test_changepassword(self,setup):
        self.driver=setup
        self.driver.get(ReadConfig.getapplicationURL())
        self.lp=LoginPage(self.driver)
        self.lp.logIn("admin6170@tqqaproject.com","password","test_changepassword")
        self.cu = ChangePassword(self.driver)
        self.cu.changepassword("admin6170@tqqaproject.com","test_changepassword")
        self.cu.validateChangePassword("admin6170@tqqaproject.com","test_changepassword")









