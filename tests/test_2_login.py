from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base import BaseTestCase
from fixtures.params import DOMAIN, EXPLICIT_TIMEOUT
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


class LoginTest(BaseTestCase):
    def setUp(self):
        super(LoginTest, self).__init__()
        self.login = LoginPage(self.driver)

    def _alert_handling(self, text):
        sleep(2)
        alert = self.driver.switch_to.alert
        alert_test = alert.text
        self.assertEqual(alert_test, text)
        alert.accept()

    # Log In with the correct credentials
    def test_login_with_correct(self):
        self.login.get_page()
        self.login.set_user_name()
        self.login.set_password()
        self.login.click_submit()
        # Expected condition
        WebDriverWait(self.driver, timeout=EXPLICIT_TIMEOUT).until(ec.url_to_be(DOMAIN + "/me"))

    # Log In with nonexistent user
    def test_login_nonexistent_user(self):
        self.login.get_page()
        self.login.set_user_name(username="nonexistentvalue")
        self.login.set_password()
        self.login.click_submit()
        # Expected condition
        self._alert_handling("Incorrect email or password")

    # Log In with wrong password
    def test_login_wrong_password(self):
        self.login.get_page()
        self.login.set_user_name()
        self.login.set_password(password=87654321)
        self.login.click_submit()
        # Expected condition
        self._alert_handling("Incorrect email or password")

    # Log In with empty fields
    def test_login_with_empty_fields(self):
        self.login.get_page()
        self.login.set_user_name(username="")
        self.login.set_password(password="")
        self.login.click_submit()
        # Expected condition
        self._alert_handling("Please provide email and password!")

    # Log In with one empty field
    def test_login_with_one_empty_field(self):
        self.login.get_page()
        self.login.set_user_name()
        self.login.set_password(password="")
        self.login.click_submit()
        # Expected condition
        self._alert_handling("Please provide email and password!")
