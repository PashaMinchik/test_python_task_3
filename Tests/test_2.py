from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.tut_by_page import Tut_by_page
from Pages.hh_page import Hh_page


class TestLogin(unittest.TestCase):

    driver: WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1(self):

        tut_by = Tut_by_page(self.driver)
        tut_by.get_home_page()
        assert "Белорусский портал" in self.driver.title

    def test_2(self):

        tut_by = Tut_by_page(self.driver)
        tut_by.click_job()
        assert True, tut_by.logo_availability()

    def test_3(self):

        head_hunter: Hh_page = Hh_page(self.driver)
        head_hunter.click_textbox("специалист по тестированию")
        head_hunter.click_find()
        assert True, head_hunter.check_find()

        time.sleep(4)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
