from pages.delete_account_page import DeleteAccount
from pages.login_page import LoginPage


class DeleteAccountTest(DeleteAccount):
    def setUp(self):
        super(DeleteAccountTest, self).setUp()
        self.login = LoginPage(self.driver)
        # self.login.go_to_page()
        self.login.login()

    def test_delete(self):
        self.delete_account()

    def tearDown(self):
        self.driver.quit()
        print("TearDown")