from fixtures.base import BaseTestCase
from fixtures.params import USER_NAME, DEFAULT_PASSWORD, DEFAULT_EMAIL, DOMAIN


class SignUpPage(BaseTestCase):
    def signup(self):
        self.driver.delete_all_cookies()
        self.driver.get(DOMAIN + "/signup")
        self.set_username()
        self.set_email()
        self.set_password()
        self.set_confirm_password()
        self.sign_up()

    def set_username(self, username=USER_NAME):
        self.driver.find_element_by_id("name").send_keys(username)

    def set_email(self, email=DEFAULT_EMAIL):
        self.driver.find_element_by_id("email").send_keys(email)

    def set_password(self, password=DEFAULT_PASSWORD):
        self.driver.find_element_by_id("password").send_keys(password)

    def set_confirm_password(self, password=DEFAULT_PASSWORD):
        self.driver.find_element_by_id("passwordConfirm").send_keys(password)

    def sign_up(self):
        self.driver.find_element_by_tag_name("button").click()

