from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from fixtures.base import BaseTestCase
from fixtures.params import PRODUCT_NAME


class DeleteReview(BaseTestCase):
    # def setUp(self):
    #     super(DeleteReview, self).setUp()

    def search_product(self, name=PRODUCT_NAME):
        self.driver.find_element_by_id("search").send_keys(name)
        self.driver.find_element_by_xpath("//button[@class='btn btn--search']").click()
        sleep(2)

    def click_product(self, name=PRODUCT_NAME):
        self.wait.until((ec.element_to_be_clickable((By.XPATH, f"//*[text()[contains(.,'{name}')]]")))).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)

    def delete_review(self):
        self.wait.until((ec.element_to_be_clickable((By.XPATH, "//button[2]")))).click()
        self.driver.switch_to.alert.accept()
