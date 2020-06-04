from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from fixtures.base import BaseTestCase

locators = {
    "image": "/home/vadim/PycharmProjects/selenium/files/image.JPG",
    "product_name": 'name',
    "product_price": 'price',
    "order_number": 'orderNumber',
    "order_date": 'orderDate',
    "group_name": 'groupName',
    "save_btn": "button"
}


class CreateReview(BaseTestCase):
    # def setUp(self):
    #     super(CreateReview, self).setUp()

    def upload_image(self):
        self.driver.find_element_by_id("photo").send_keys(locators["image"])

    def set_product_name(self, product_name):
        ec.element_to_be_clickable(locators["product_name"])
        self.driver.find_element_by_id(locators["product_name"]).send_keys(product_name)

    def set_price(self, product_price):
        self.driver.find_element_by_id(locators["product_price"]).send_keys(product_price)

    def set_order_number(self, product_order_num):
        self.driver.find_element_by_id(locators["order_number"]).send_keys(product_order_num)

    def select(self, product_order_date):
        ec.element_to_be_clickable(locators["order_date"])
        self.driver.find_element_by_id(locators["order_date"]).send_keys(product_order_date)

    def set_group_name(self, product_group_name):
        ec.element_to_be_clickable(locators["group_name"])
        self.driver.find_element_by_id(locators["group_name"]).send_keys(product_group_name)

    def save(self, product_name):
        self.driver.find_element_by_tag_name(locators["save_btn"]).submit()
        self.wait.until((ec.element_to_be_clickable((By.XPATH, f"//*[text()[contains(.,'{product_name}')]]"))))