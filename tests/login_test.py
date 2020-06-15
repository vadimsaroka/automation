from selenium.webdriver.support import expected_conditions as ec
from fixtures.base import BaseTestCase
from fixtures.params import DOMAIN
from pages.delete_account_page import DeleteAccount
from pages.login_page import LoginPage
from pages.sing_up_page import SignUpPage


class LoginTest(SignUpPage, DeleteAccount, BaseTestCase):
    def setUp(self):
        self.page_url = DOMAIN + "/login"
        self.login = LoginPage(self.driver)
        self.go_to_page()

    def test_login_with_correct(self):
        # create a user in order to be able to login
        self.signup()
        self.wait.until(ec.url_to_be(DOMAIN + "/me"))
        # login with correct credentials
        self.go_to_page()
        self.login.login()
        self.wait.until(ec.url_to_be(DOMAIN + "/me"))
        # clean up after successfully login
        self.delete_account()

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
