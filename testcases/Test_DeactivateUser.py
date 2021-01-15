import pytest
import allure
from  pageobjects.LoginPage import LoginPage
from  pageobjects.ModifyUser import ModifyUser
from  pageobjects.CreateUser import CreateUser

from utilities.CustomLogger import LogGen
from utilities.ReadProperties import  ReadConfig

@pytest.mark.usefixtures("setup")
class TestDeactivateUser():
    logger = LogGen.loggen()


    @allure.feature("Feature name")
    @allure.severity('Critical')
    def test_deactivateuser(self, setup):
        self.driver = setup
        self.driver.get(ReadConfig.getapplicationURL())
        self.lp = LoginPage(self.driver)
        self.lp.logIn()
        self.cu =ModifyUser(self.driver)
        self.cu.deactivateuser()












