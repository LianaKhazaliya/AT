from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from element import BasePageElement
from locators import MainPageLocators


class Main_page:

    def __init__(self):
        self.URL = 'https://book.austrian.com/app/fb.fly?pos=BY&l=en'
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)
        self.driver.close()

    def __move_to_form(self):
        element = self.driver.find_element_by_id("aua-search-form")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _is_error_in_form(self):
        try:
            error_message = self.driver.find_element_by_xpath(
                "//span[@class = 'help-block small']"
                ).text
        except:
            error_message = ''
        return bool(error_message)

    def _submit_form(self):
        self.driver.find_element_by_id("aua-search-submit").click()

    def _fill_city_departure(self, city_from):
        city = city_from
        input = self.driver.find_element_by_xpath('//input[@id="flight_departure"]')
        input.send_keys(city)

    def _fill_city_arrive(self, city_to):
        city = city_to
        input = self.driver.find_element_by_xpath('//input[@id="flight_arrival"]')
        input.send_keys(city)


    def getPageName(self):
        return self.driver.find_element_by_xpath("//div[@class = 'top']//img/@alt").text

    def check_arrivall_city_empty(self):
        self._submit_form()
        return self._is_error_in_form()

    def check_arrivall_city_wrong(self):
        self._fill_city_arrive('qwte')
        self._submit_form()
        return self._is_error_in_form()
