from selenium.webdriver.support import expected_conditions as ec
from fixtures.base import BaseTestCase
from fixtures.params import PRODUCT_NAME, PRICE, ORDER_NUMBER, GROUP_NAME, DATE

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
    def upload_image(self):
        self.driver.find_element_by_id("photo").send_keys(locators["image"])

    def set_product_name(self, product_name=PRODUCT_NAME):
        ec.element_to_be_clickable(locators["product_name"])
        self.driver.find_element_by_id(locators["product_name"]).send_keys(product_name)

    def set_price(self, product_price=PRICE):
        self.driver.find_element_by_id(locators["product_price"]).send_keys(product_price)

    def set_order_number(self, product_order_num=ORDER_NUMBER):
        self.driver.find_element_by_id(locators["order_number"]).send_keys(product_order_num)

    def select(self, product_order_date=DATE):
        ec.element_to_be_clickable(locators["order_date"])
        self.driver.find_element_by_id(locators["order_date"]).send_keys(product_order_date)

    def set_group_name(self, product_group_name=GROUP_NAME):
        ec.element_to_be_clickable(locators["group_name"])
        self.driver.find_element_by_id(locators["group_name"]).send_keys(product_group_name)

    def save(self):
        self.driver.find_element_by_tag_name(locators["save_btn"]).submit()
