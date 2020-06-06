from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from fixtures.params import DOMAIN, DEFAULT_PASSWORD, DEFAULT_EMAIL, EXPLICIT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username=DEFAULT_EMAIL, password=DEFAULT_PASSWORD):
        self.driver.get(DOMAIN + "/login")
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_tag_name("button").click()
        WebDriverWait(self.driver, timeout=EXPLICIT_TIMEOUT).until(ec.url_to_be(DOMAIN + "/me"))

    def logout(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        sleep(2)
        WebDriverWait(self.driver, timeout=EXPLICIT_TIMEOUT).until((ec.element_to_be_clickable(
            (By.XPATH, "//*[text()[contains(.,'Log out')]]")))).click()
        WebDriverWait(self.driver, timeout=EXPLICIT_TIMEOUT).until(ec.url_to_be(DOMAIN + "/"))

    def get_page(self):
        self.driver.get(DOMAIN + "/login")
        WebDriverWait(self.driver, timeout=EXPLICIT_TIMEOUT).until(ec.url_to_be(DOMAIN + "/login"))

    def set_user_name(self, username=DEFAULT_EMAIL):
        self.driver.find_element_by_id("email").send_keys(username)

    def set_password(self, password=DEFAULT_PASSWORD):
        self.driver.find_element_by_id("password").send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_tag_name("button").click()
