from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from automation.testbase.Base import Base
import sys

class ActionDrivers(object):

    base = Base()


    def isElementPresent(self, by, locator):
        """
        This method is used to check the element visibility.
        :param by:
        :param locator: locator of the element
        :return: boolean (True or False)
        """
        try:
            self.base.driver.find_element(by, locator).is_displayed()
            return True
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return None

    def click_element(self, by, locator):
        """
        This method is used to click on the element.
        :param by: By
        :param locator: locator of the element
        :return: boolean (True or False)
        """
        try:
            self.isElementPresent(by, locator)
            self.base.driver.find_element(by, locator).click()
            return True
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return False

    def type_in_textbox(self, by, locator, value):
        """
        This method is used to type the text in text box.
        :param by: By
        :param locator: locator of the element
        :return: Boolean (True or False)
        """
        try:
            self.isElementPresent(by, locator)
            self.base.driver.find_element(by, locator).clear()
            self.base.driver.find_element(by, locator).send_keys(value)
            return True
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return False

    def select_visibletext_from_dropdown_(self, by, locator, value):
        """
        This method is used to select value from the dropdown.
        :param by: By
        :param locator: locator of the element
        :param value: value to be selected
        :return: boolean (True or False)
        """
        try:
            self.isElementPresent(by, locator)
            select = Select(self.base.driver.find_element(by, locator))
            select.select_by_visible_text(value)
            return True
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return False

    def link_text(self, by, link_text):
        """
        This method is used to find element with link text.
        :param by: By
        :param link_text: link text value
        :return: Bolean (true or false)
        """
        try:
            self.isElementPresent(by, link_text)
            self.base.driver.find_element(by, link_text).click()
            return True
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return False

    def type_url(self, value):
        """
        This method is used to type the url.
        :param value: URL
        :return: Boolean (True or False)
        """
        try:
            self.base.driver.get(value)
            self.base.driver.maximize_window()
            return True
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return False

    def find_tagname(self, tag_name):
        """
        This method is used to find element by tag name.
        :param tag_name: Tag name
        :return: Boolean (True or False)
        """
        try:
            self.isElementPresent(By.TAG_NAME, tag_name)
            return True
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return False

    def get_element_attribute(self, by, locator, attribute):
        """
        This method is used to get the text basing on the attribute.
        :param attribute: attribute type
        :param by: By
        :param locator: Locator of the element
        :return: String (element text)
        """
        try:
            self.isElementPresent(by, locator)
            element_text = self.base.driver.find_element(by, locator).get_attribute(attribute)
            return element_text
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return None

    def get_all_elements(self, by, locator):
        """
        This method is used to get the elements with name.
        :param by: By
        :param locator: Locator of the element
        :return: elements
        """
        try:
            elements = self.base.driver.find_elements(by, locator)
            return elements
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return None


    def get_element(self, by, locator):
        """
        This method will get the element basing on the locator
        :param by: By type
        :param locator: locator of the element.
        :return: element
        """
        try:
            element = self.base.driver.find_element(by, locator)
            return element
        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return None



