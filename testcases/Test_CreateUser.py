import pytest
import allure
from  pageobjects.LoginPage import LoginPage
from  pageobjects.CreateUser import CreateUser
from utilities.CustomLogger import LogGen
from utilities.ReadProperties import  ReadConfig


@pytest.mark.usefixtures("setup")
class TestCreateUser():

    logger = LogGen.loggen()
    @allure.feature("Feature name")
    @allure.severity('Critical')
    def test_createuser3(self,setup):
        self.driver=setup
        self.driver.get(ReadConfig.getapplicationURL())
        self.lp=LoginPage(self.driver)
        self.lp.logIn()
        self.cu = CreateUser(self.driver)
        self.cu.createuser()







