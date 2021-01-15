import SeleniumLibrary
class simple:
  def __init__(self , driver):
      self.driver=driver;
  def clickJs(self,locator):
      javas = 'document.getElementsByClass('+locator+')[0].click();'
      self.driver.execute_script(javas)


s=simple()
