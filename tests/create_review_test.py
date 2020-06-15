from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.delete_account_page import DeleteAccount
from pages.create_review_page import CreateReview
from fixtures.params import PRODUCT_NAME, DOMAIN, EXPLICIT_TIMEOUT
from pages.sing_up_page import SignUpPage


class CreateReviewTest(SignUpPage, DeleteAccount, CreateReview):
    def setUp(self):
        # create an account in order to be able to login
        self.signup()
        self.wait.until(ec.url_to_be(DOMAIN + "/me"))
        self.page_url = DOMAIN + "/newreview"

    def tearDown(self):
        # clean up after test
        self.delete_account()

    def test_create_review(self):
        try:
            self.go_to_page()
            self.upload_image()
            self.set_product_name()
            self.set_price()
            self.set_order_number()
            self.select()
            self.set_group_name()
            self.save()
            self.wait.until(ec.url_to_be(DOMAIN + "/reviews"))
            self.search_product()
            self.wait.until((ec.element_to_be_clickable((By.XPATH, f"//*[text()[contains(.,'{PRODUCT_NAME}')]]"))))
        except TimeoutException:
            self.save_screenshot()
            raise

    def test_create_review_with_no_product_name(self):
        try:
            self.go_to_page()
            self.upload_image()
            self.set_product_name(product_name="")
            self.set_price()
            self.set_order_number()
            self.select()
            self.set_group_name()
            self.save()
            sleep(3)
            self.alert_handling("Invalid input data. A review must have a name")
            self.wait.until(ec.url_to_be(self.page_url))
        except NoAlertPresentException:
            self.save_screenshot()
            raise
        except TimeoutException:
            self.save_screenshot()
            raise

    def test_create_review_with_no_price(self):
        try:
            self.go_to_page()
            self.upload_image()
            self.set_product_name()
            self.set_price(product_price="")
            self.set_order_number()
            self.select()
            self.set_group_name()
            self.save()
            sleep(3)
            self.alert_handling("Invalid price: null.")
            WebDriverWait(self.driver, timeout=EXPLICIT_TIMEOUT).until(ec.url_to_be(self.page_url))
        except NoAlertPresentException:
            self.save_screenshot()
            raise
        except TimeoutException:
            self.save_screenshot()
            raise

