import unittest
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from .params import EXPLICIT_TIMEOUT, BROWSER_TYPE
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import traceback
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options


def get_browser():
    if BROWSER_TYPE.lower().find("chrome") >= 0:
        options = Options()
        options.page_load_strategy = 'eager'
        browser = Chrome(options=options)
    elif BROWSER_TYPE.lower().find("firefox") >= 0:
        browser = Firefox()
    else:
        raise Exception(f"I'm sorry {BROWSER_TYPE} browser is not supported")
    return browser


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = get_browser()
            cls.driver.maximize_window()
            cls.wait = WebDriverWait(cls.driver, timeout=EXPLICIT_TIMEOUT, poll_frequency=1)
            cls.page_url = None
        except Exception as e:
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def alert_handling(self, text):
        """
        Helper method to accept the presence alert
        :params text: text value
        """
        sleep(2)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.assertEqual(alert_text, text)
        alert.accept()

    def go_to_page(self):
        """
        Helper method that allows going to the page URL
        defined on the page from which this method was called
        """
        try:
            sleep(2)
            self.driver.get(self.page_url)
            self.wait.until(ec.url_to_be(self.page_url))
        except TimeoutException:
            raise

    def save_screenshot(self):
        """
        Helper method that allows saving a screenshot
        """
        file_name = str(traceback.extract_stack(None, 2)[0]).split("/")[-1].split(",")[0]
        function_name = traceback.extract_stack(None, 2)[0][2]
        self.driver.save_screenshot(f"{file_name} => {function_name}_{datetime.datetime.now()}.png")


if __name__ == '__main__':
    unittest.main(verbosity=2)
