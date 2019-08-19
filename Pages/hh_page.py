from Locators.locators import Locators


class Hh_page():

    def __init__(self, driver: object) -> object:
        self.driver = driver
        self.path_textbox_job = Locators.path_textbox_job
        self.path_button_find = Locators.path_button_find
        self.path_check_find = Locators.path_check_find

    def click_textbox(self, text_find):
        self.driver.find_element_by_xpath(self.path_textbox_job).send_keys(text_find)

    def click_find(self) -> object:
        self.driver.find_element_by_css_selector(self.path_button_find).click()

    def check_find(self):
        self.driver.find_elements_by_xpath(self.path_check_find)
