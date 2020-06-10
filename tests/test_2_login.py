from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from fixtures.base import BaseTestCase
from fixtures.params import DOMAIN, EXPLICIT_TIMEOUT
from pages.login_page import LoginPage


class LoginTest(BaseTestCase):
    def setUp(self):
        self.page_url = DOMAIN + "/login"
        self.login = LoginPage(self.driver)
        self.go_to_page()

    def test_login_with_correct(self):
        self.login.set_user_name()
        self.login.set_password()
        self.login.click_submit()
        WebDriverWait(self.driver, timeout=EXPLICIT_TIMEOUT).until(ec.url_to_be(DOMAIN + "/me"))

    def test_login_nonexistent_user(self):
        self.login.set_user_name(username="nonexistentvalue")
        self.login.set_password()
        self.login.click_submit()
        self.alert_handling("Incorrect email or password")

    def test_login_wrong_password(self):
        self.login.set_user_name()
        self.login.set_password(password=87654321)
        self.login.click_submit()
        self.alert_handling("Incorrect email or password")

    def test_login_with_empty_fields(self):
        self.login.set_user_name(username="")
        self.login.set_password(password="")
        self.login.click_submit()
        self.alert_handling("Please provide email and password!")

    def test_login_with_one_empty_field(self):
        self.login.set_user_name()
        self.login.set_password(password="")
        self.login.click_submit()
        self.alert_handling("Please provide email and password!")
