from fixtures.base import BaseTestCase
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from fixtures.params import DOMAIN
from pages.sing_up_page import SignUpPage


class DeleteAccount(BaseTestCase):

    def delete_account(self):
        self.driver.get(DOMAIN + "/me")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        self.wait.until((ec.element_to_be_clickable((By.CLASS_NAME, "btn--red")))).click()
        self.driver.switch_to.alert.accept()
        self.wait.until(ec.url_to_be(DOMAIN + "/signup"))

