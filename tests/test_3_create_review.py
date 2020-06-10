from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import datetime
from time import sleep
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.create_review_page import CreateReview
from fixtures.params import PRODUCT_NAME, DOMAIN, EXPLICIT_TIMEOUT


class CreateReviewTest(CreateReview):
    def setUp(self):
        self.login = LoginPage(self.driver)
        self.page_url = DOMAIN + "/newreview"
        self.login.login()

    def tearDown(self):
        self.login.logout()

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
            self.wait.until((ec.element_to_be_clickable((By.XPATH, f"//*[text()[contains(.,'{PRODUCT_NAME}')]]"))))
        except ValueError:
            self.driver.save_screenshot(f"{__name__}_{datetime.datetime.now()}.png")

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
        except ValueError:
            self.driver.save_screenshot(f"{__name__}_{datetime.datetime.now()}.png")

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
        except ValueError:
            self.driver.save_screenshot(f"{__name__}_{datetime.datetime.now()}.png")
