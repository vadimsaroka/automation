from selenium.webdriver.support.ui import Select
from pages.login_page import LoginPage
from pages.create_review_page import CreateReview
from fixtures.params import PRODUCT_NAME, DOMAIN, PRICE, ORDER_NUMBER, GROUP_NAME, DATE


class CreateReviewTest(CreateReview):
    def setUp(self):
        super(CreateReviewTest, self).setUp()
        self.login = LoginPage(self.driver)
        self.page_url = DOMAIN + "/newreview"
        self.login.login()

    def test_create_review(self):
        self.go_to_page()
        self.upload_image()
        self.set_product_name(PRODUCT_NAME)
        self.set_price(PRICE)
        self.set_order_number(ORDER_NUMBER)
        self.select(DATE)
        self.set_group_name(GROUP_NAME)
        self.save(PRODUCT_NAME)
        self.login.logout()



