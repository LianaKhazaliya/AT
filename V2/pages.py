from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class Main_page:
    def __init__(self):
        self.URL = 'https://www.qantas.com'
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)

        self.__hide_start_window()
        self._show_form()
        time.sleep(.4)

    def __hide_start_window(self):
        x = self.driver.find_element_by_class_name('disclaimer__wrap--toggler--close-btn')
        x.click()

    def __move_to_form(self):
        element = self.driver.find_element_by_class_name("multi-search-form")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def _show_form(self):
        form = self.driver.find_element_by_class_name('widget-form__group')
        self.__move_to_form()
        time.sleep(.5)
        form.click()

    def _is_error_in_form(self):
        time.sleep(.3)
        try:
            error_message = self.driver.find_element_by_xpath("//div[@class = 'form-validation-message']//div[@class='form-validation-message__text']").text
        except:
            error_message = ''
        return bool(error_message)

    def _submit_form(self):
        self.driver.find_element_by_xpath("//div[@class='qfa1-submit-button__container-right widget-form__group-container size-big']//div[@class='widget-form__group']").click()

    def _fill_city(self):
        city = 'Auckland'
        input = self.driver.find_element_by_id('typeahead-input-to')
        input.send_keys(city)


    def getPageName(self):
        return self.driver.find_element_by_xpath("//a[@class = 'logo-qantas']").text

    def check_arrivall_city_empty(self):
        self._submit_form()
        return self._is_error_in_form()

    def check_arrivall_city_wrong(self):
        input = self.driver.find_element_by_id('typeahead-input-to')
        input.send_keys('Minsk')
        self._submit_form()
        return self._is_error_in_form()

    def check_arrivall_city_good_fill(self):
        self._fill_city()
        self._show_form()
        return self._is_error_in_form()
