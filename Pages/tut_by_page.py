from Locators.locators import Locators


class Tut_by_page ():

    def __init__(self, driver):
        self.driver = driver
        self.home_site = "https://www.tut.by/"
        self.button_job = Locators.button_job

    def get_home_page(self):
        self.driver.get(self.home_site)

    def click_job(self):
        self.driver.find_element_by_xpath(self.button_job).click()

    def logo_availability(self):
        self.driver.find_element_by_xpath(self.logo_availability())
