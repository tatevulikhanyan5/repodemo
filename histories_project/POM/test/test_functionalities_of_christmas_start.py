import pytest

@pytest.mark.usefixtures('get_driver')
class TestChristmasStartFunctionality:
    def test_assert_header_on_christmas_start_page(self):
        self.homepage.navigate_to_christmas_started_page()
        self.christmasstartpage.assert_header_christmas_started_page()
