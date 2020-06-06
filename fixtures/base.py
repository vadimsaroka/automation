import unittest
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from .params import CHROME_EXECUTABLE_PATH, EXPLICIT_TIMEOUT, BROWSER_TYPE, FIREFOX_EXECUTABLE_PATH
from selenium.webdriver.support.ui import WebDriverWait


def get_browser():
    if BROWSER_TYPE.lower().find("chrome") >= 0:
        browser = CHROME_EXECUTABLE_PATH
    # elif BROWSER_TYPE.lower().find("firefox") >= 0:
    #     browser = FIREFOX_EXECUTABLE_PATH
    else:
        raise Exception(f"I'm sorry {BROWSER_TYPE} browser is not supported")
    return browser


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_browser()
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, timeout=EXPLICIT_TIMEOUT, poll_frequency=1)
        cls.page_url = None

    # @classmethod
    # def tearDownClass(cls):
    #     # yield
    #     # self.driver.close()
    #     cls.driver.quit()

    def go_to_page(self):
        sleep(2)
        self.driver.get(self.page_url)
        self.wait.until(ec.url_to_be(self.page_url))


if __name__ == '__main__':
    unittest.main(verbosity=2)
