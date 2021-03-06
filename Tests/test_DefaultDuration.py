import unittest
from PageObjects.Common import *
from PageObjects.Pages.LoginPage import LoginPage
from TestData.SettingsData import *
from CalendarAPI import *
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

@pytest.mark.usefixtures("driver")
class DefaultDurationTest(unittest.TestCase):

    def test_default_duration(self):
        loginpage = LoginPage(self.driver)
        loginpage.go_to_page(base_url())
        calendar_page = loginpage.login(username(), password())
        settings_page = calendar_page.go_to_settings_page(base_url() + settings_uri)
        settings_page.change_default_duration(self.event_length)
        settings_page.save_changes()
        changed_event_length = str(get_setting('defaultEventLength'))
        start_time, end_time = quick_add_event()
        settings_page.validate_default_length(start_time, end_time, changed_event_length)


if __name__ == "__main__":
    unittest.main()
