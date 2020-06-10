from fixtures.params import DOMAIN
from pages.delete_review_page import DeleteReview
from pages.login_page import LoginPage


class DeleteReviewTest(DeleteReview):
    def setUp(self):
        super(DeleteReviewTest, self).setUp()
        self.page_url = DOMAIN + "/reviews"
        self.login = LoginPage(self.driver)
        self.login.login()

    def test_delete_review(self):
        self.go_to_page()
        self.search_product()
        self.click_product()
        self.delete_review()
        self.login.logout()

