import pytest
import allure
from  pageobjects.LoginPage import LoginPage
from  pageobjects.CreateUserpage import CreateUser
from utilities.CustomLogger import LogGen
from utilities.ReadProperties import  ReadConfig
from utilities.BrowserFactory import setup
import json

with open('C:/Users/karthik.survepalli/tqqa/TQQADemoProject/TestData/Data.json') as f:
  data = json.load(f)


@pytest.mark.usefixtures("setup")
class TestCreateUser():

    logger = LogGen.loggen()
    @allure.feature("CreateUser")
    @allure.severity('Critical')
    def test_createuser(self,setup):
        self.driver = setup
        self.driver.get(ReadConfig.getapplicationURL())
        self.lp = LoginPage(self.driver)
        self.lp.logIn(data["username"],data["password"],"test_createuser")
        self.cu = CreateUser(self.driver)
        email=self.cu.createuser("test_createuser")
        self.cu.validatecreateuser(email,"test_createuser")







