from selenium.webdriver.common.by import By
from histories_project.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    how_did_christmas_start_link = (By.LINK_TEXT, 'How Did Christmas Start?')

    def navigate_to_christmas_started_page(self):
        self.find_and_click(self.how_did_christmas_start_link)

