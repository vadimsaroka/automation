from datetime import date
from random import randint
import os
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options

DOMAIN = "https://amzreviewer.now.sh"

USER_NAME = "Testuser"
DEFAULT_PASSWORD = "12345678"
DEFAULT_EMAIL = "test@gmail.com"

cwd = os.path.abspath(os.getcwd())

#The Chrome driver setup
options = Options()
options.page_load_strategy = 'eager'
CHROME_EXECUTABLE_PATH = Chrome(options=options)

#The FireFox driver setup
# FIREFOX_EXECUTABLE_PATH = os.path.join(cwd, "driver/geckodriver")\
FIREFOX_EXECUTABLE_PATH = Firefox()


BROWSER_TYPE = "Chrome"

EXPLICIT_TIMEOUT = 10

PRODUCT_NAME = "vs product name"
PRICE = f"{str(randint(1, 100))}"
ORDER_NUMBER = "111-222-333-444-555"
GROUP_NAME = 'testgroupname'
DATE = date.today().strftime("%m/%d/%y")




