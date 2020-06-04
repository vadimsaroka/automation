# from datetime import date
# from time import sleep
# from selenium.webdriver.support import expected_conditions as EC
#
# review_name = "Testproductname"
# review_price = "99.99"
# review_order_num = "111-222-333-444-555"
# review_order_date = date.today().strftime("%m/%d/%y")
# review_group_name = "testgroupname"
#
#
# def login(self, username="vsaroka87@gmail.com", password="YPXwgdCa"):
#     driver = self.driver
#     driver.implicitly_wait(2)
#     driver.find_element_by_css_selector("[href='/login']").click()
#     driver.find_element_by_id("email").send_keys(username)
#     driver.find_element_by_id("password").send_keys(password)
#     driver.find_element_by_tag_name("button").click()
#     self.assertEqual(username,
#                      driver.find_element_by_xpath("//input[@id='email']").get_attribute('value'))
#
#
# def logout(driver):
#     sleep(3)
#     driver.execute_script("window.scrollTo(0, 0);")
#     driver.find_element_by_xpath("//*[text()[contains(.,'Log out')]]").click()
#
#
# def create_review(driver):
#     driver.find_element_by_xpath('//*[@href="/newreview"]').click()
#     driver.find_element_by_id('name').send_keys(review_name)
#     driver.find_element_by_id('price').send_keys(review_price)
#     driver.find_element_by_id('orderNumber').send_keys(review_order_num)
#     driver.find_element_by_id('orderDate').send_keys(review_order_date)
#     driver.find_element_by_id('groupName').send_keys(review_group_name)
#     driver.find_element_by_tag_name("button").submit()
#
#
# def delete_review(driver):
#     EC.element_to_be_clickable('//*[@href="/reviews"]')
#     driver.find_element_by_xpath('//*[@href="/reviews"]').click()
#     sleep(3)
#     driver.find_element_by_id("search").send_keys(review_name)
#     driver.find_element_by_xpath("//button[@class='btn btn--search']").click()
#     sleep(2)
#     driver.find_element_by_class_name("review__image").click()
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     sleep(2)
#     driver.find_element_by_xpath("//button[2]").click()
#     EC.alert_is_present()
#     driver.switch_to.alert.accept()
