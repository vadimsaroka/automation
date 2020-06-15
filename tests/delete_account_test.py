from fixtures.params import DOMAIN
from pages.delete_account_page import DeleteAccount
from pages.sing_up_page import SignUpPage
from selenium.webdriver.support import expected_conditions as ec


class DeleteAccountTest(SignUpPage, DeleteAccount):
    def setUp(self):
        self.signup()
        self.wait.until(ec.url_to_be(DOMAIN + "/me"))

    def test_delete(self):
        self.delete_account()
