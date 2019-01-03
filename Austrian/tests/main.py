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

    def test_check_arrivall_city_wrong(self):
        self.assertTrue(self.page.check_arrivall_city_wrong())



    #def test_name_of_the_page_is_ok(self):
    #    self.assertIn('Austrian Airways', self.page.getPageName())
        
    def test_epmty_arrivall_city(self):
        self.assertTrue(self.page.check_arrivall_city_empty())

    def test_wrong_arrivall_city(self):
        self.assertTrue(self.page.check_arrivall_city_wrong())

    def test_right_arrivall_city(self):
        self.assertFalse(self.page.check_arrivall_city_good_fill())

    def tearDown(self):
        self.page.driver.close()



if __name__ == "__main__":
    
    unittest.main()
