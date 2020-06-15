from time import sleep
from fixtures.params import DOMAIN
from pages.create_review_page import CreateReview
from pages.delete_account_page import DeleteAccount
from pages.delete_review_page import DeleteReview
from pages.sing_up_page import SignUpPage
from selenium.webdriver.support import expected_conditions as ec


class DeleteReviewTest(SignUpPage, CreateReview, DeleteAccount, DeleteReview):
    def setUp(self):
        # create an account in order to be able to login
        self.signup()
        self.wait.until(ec.url_to_be(DOMAIN + "/me"))
        self.page_url = DOMAIN + "/reviews"
        # create a review
        self.create_review()

    def tearDown(self):
        # clean up after test
        self.delete_account()

    def test_delete_review(self):
        self.go_to_page()
        self.search_product()
        sleep(2)
        self.click_product()
        self.delete_review()

