from selenium import webdriver
from pages.home.login_page import loginPage
import unittest


class LoginTest(unittest.TestCase):

    def test_Login_valid(self):
        self.baseurl = "https://www.surveymonkey.com"
        self.driver = webdriver.Chrome()

        # maximise window
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # open Url
        self.driver.get(self.baseurl)

        self.lp = loginPage(self.driver)

        self.lp.login("arsalan.khan01", "arsalan.123")
        self.driver.implicitly_wait(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
