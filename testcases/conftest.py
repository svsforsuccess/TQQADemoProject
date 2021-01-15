from selenium import webdriver
import pytest
from utilities.ReadProperties import  ReadConfig
from  pageobjects.LoginPage import LoginPage
from  pageobjects.CreateUser import CreateUser


@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = WebDriver.Firefox()
    elif browser=='remote':
        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        driver = webdriver.Remote('https://karthiksurvepall1:2u48dyFbmzRhsykyH8bX@hub-cloud.browserstack.com/wd/hub',desired_cap)
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    request.config.getoption("--browser")
















































#@pytest.fixture(scope="session")
# def setup(request):
#     print("initiating chrome driver")
#
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     session = request.node
#     for item in session.items:
#         cls = item.getparent(pytest.Class)
#         setattr(cls.obj, "driver", driver)
#     driver.get(ReadConfig.getapplicationURL())
#     driver.maximize_window()
#     cf = LoginPage(driver)
#     cu = CreateUser(driver)
#     yield driver,cf,cu
#
#
#     driver.close()

