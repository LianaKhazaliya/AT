import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pages
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary)

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.page = pages.Main_page()

    def test_name_of_the_page_is_ok(self):
        time.sleep(1)
        self.assertIn('Qantas Airways', self.page.getPageName())

    def test_epmty_arrivall_city(self):
        time.sleep(1)
        self.assertTrue(self.page.check_arrivall_city_empty())

    def test_wrong_arrivall_city(self):
        time.sleep(1)
        self.assertTrue(self.page.check_arrivall_city_wrong())

    def test_right_arrivall_city(self):
        time.sleep(1)
        self.assertFalse(self.page.check_arrivall_city_good_fill())

    # def check_arrivall_city_good_fill(self):

    def tearDown(self):
        self.page.driver.close()

if __name__ == "__main__":
    # page = pages.Main_page()
    # print(page.getPageName())
    # print(':', page.check_arrivall_city_empty())
    # print(page.check_arrivall_city_wrong_city())
    # page._fill_city()
    # page.check_infant_equals_adult()
    unittest.main()
