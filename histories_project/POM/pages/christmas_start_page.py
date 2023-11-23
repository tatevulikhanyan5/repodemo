from selenium.webdriver.common.by import By
from histories_project.POM.lib.helpers import Helpers


class ChristmasStartedPage(Helpers):
    how_did_christmas_start_header = (By.ID, 'how-did-christmas-start')

    def assert_header_christmas_started_page(self):
        self.find(self.how_did_christmas_start_header, get_text=True)

