from fixtures.params import PRODUCT_NAME, DOMAIN, PRICE, ORDER_NUMBER, GROUP_NAME, DATE
from pages.sing_up_page import SignUpPage


class SignUpTest(SignUpPage):
    def setUp(self):
        super(SignUpTest, self).setUp()
        self.page_url = DOMAIN + "/signup"

    def test_sing_up(self):
        self.go_to_page()
        self.set_username()
        self.set_email()
        self.set_password()
        self.set_confirm_password()
        self.sign_up()
