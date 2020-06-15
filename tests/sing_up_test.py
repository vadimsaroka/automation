from selenium.webdriver.support import expected_conditions as ec
from fixtures.params import DOMAIN, DEFAULT_EMAIL
from pages.delete_account_page import DeleteAccount
from pages.login_page import LoginPage
from pages.sing_up_page import SignUpPage


class SignUpTest(SignUpPage, DeleteAccount):
    def setUp(self):
        self.page_url = DOMAIN + "/signup"
        self.driver.delete_all_cookies()
        self.go_to_page()

    def _assert_handler(self):
        self.assertEqual([], self.driver.get_cookies())
        self.assertEqual(self.page_url, self.driver.current_url)

    def _sing_up_with_duplicate_val(self):
        self.go_to_page()
        self.set_username()
        self.set_email()
        self.set_password()
        self.set_confirm_password()
        self.sign_up()
        self.alert_handling(f'Duplicate field value: "{DEFAULT_EMAIL}". Please use another value!')

    def test_sing_up(self):
        self.set_username()
        self.set_email()
        self.set_password()
        self.set_confirm_password()
        self.sign_up()
        self.wait.until(ec.url_to_be(DOMAIN + "/me"))
        self.assertEqual(DOMAIN + "/me", self.driver.current_url)
        # sign up with duplicate credentials
        self._sing_up_with_duplicate_val()
        # clean up after successfully signed up
        self.login = LoginPage(self.driver)
        self.login.login()
        self.delete_account()

    def test_sing_up_with_no_username(self):
        self.set_username(username="")
        self.set_email()
        self.set_password()
        self.set_confirm_password()
        self.sign_up()
        self._assert_handler()

    def test_sing_up_with_no_email(self):
        self.set_username()
        self.set_email(email="")
        self.set_password()
        self.set_confirm_password()
        self.sign_up()
        self.assertEqual([], self.driver.get_cookies())
        self.assertEqual(self.page_url, self.driver.current_url)

    def test_sing_up_with_no_password(self):
        self.set_username()
        self.set_email()
        self.set_password(password="")
        self.set_confirm_password()
        self.sign_up()
        self._assert_handler()

    def test_sing_up_with_no_conf_password(self):
        self.set_username()
        self.set_email()
        self.set_password()
        self.set_confirm_password(password="")
        self.sign_up()
        self._assert_handler()

    def test_sing_up_with_wrong_conf_password(self):
        self.set_username()
        self.set_email()
        self.set_password()
        self.set_confirm_password(password="somerandompassword")
        self.sign_up()
        self._assert_handler()
        self.alert_handling('Invalid input data. Passwords are not the same!')

    def test_sing_up_with_wrong_email(self):
        self.set_username()
        self.set_email(email="test@gmail")
        self.set_password()
        self.set_confirm_password()
        self.sign_up()
        self._assert_handler()
        self.alert_handling('Invalid input data. Please provide a valid email')

    def test_sing_up_with_empty_fields(self):
        self.set_username(username="")
        self.set_email(email="")
        self.set_password(password="")
        self.set_confirm_password(password="")
        self.sign_up()
        self._assert_handler()


