from automation.testbase.ActionDrivers import ActionDrivers
from automation.testbase.Base import Base
from time import sleep
import configparser
from selenium.webdriver.common.by import By
import sys
from automation.objectrepository.Home_Repo import Home_Repo


class HomePage(object):

    base = Base()
    ad = ActionDrivers()
    home_repo = Home_Repo()


    def read_config_file(self, section, option):
        """
        This method will parse the config file and gives the required parameter's value.
        :param section: Section Name
        :param option: option name
        :return: value
        """
        try:

            print("Parsing config file")
            config = configparser.ConfigParser()
            config.read('C:/Users/com/Desktop/Assembly/ConfigFile.ini')
            return config.get(section, option)
        except Exception as err:
            print("Unexpected error:", sys.exc_info())

    def launch_website(self):
        """
        This method will open the browser and then url.
        :return:
        """
        try:
            url = self.read_config_file('URL', 'assembly_url')
            self.ad.type_url(url)
        except Exception as err:
            print("Unexpected error:", sys.exc_info())


    def get_email_fields(self):
        """
        This method will get the occurrence of email fields.
        :return:
        """
        try:
            sleep(2)
            email_fields = self.ad.get_all_elements(By.NAME, self.home_repo.email_textbox_name)
            print("Total number of EMAIL feilds present in this page are %s", len(email_fields))
            return email_fields

        except Exception as err:
            print("Unexpected error:", sys.exc_info())
            return None

    def verify_email_field(self):
        """
        This method will verify the second email field.
        :return:
        """
        try:
            email_feilds = self.get_email_fields()
            placeholder = 'Please try a work email'
            for i in range(len(email_feilds)):
                if i == 2:
                    secnd_email = email_feilds[1]
                    sleep(5)
                    secnd_email.send_keys(self.read_config_file('EmailDetails', 'inactive_email'))
                    self.ad.click_element(By.CSS_SELECTOR, self.home_repo.second_email_try_button_css)
                    sleep(5)
                    place_holder = secnd_email.get_attribute('placeholder')
                    if place_holder == placeholder:
                        print('Email is not working, please provide a working email')

                    sleep(5)
                    secnd_email.clear()
                    secnd_email.send_keys(self.read_config_file('EmailDetails', 'active_email'))
                    self.ad.click_element(By.CSS_SELECTOR, self.home_repo.second_email_try_button_css)
                    sleep(10)
                    verification_window = self.ad.isElementPresent(By.CSS_SELECTOR, 'div.readmin-page-content')
                    if verification_window:
                        print("Email is working and active.")

        except Exception as err:
            print("Unexpected error:", sys.exc_info())

    def verify_features_tab(self):
        """
        This method will verify the feature tab's functionality.
        :return:
        """
        try:
            self.ad.click_element(By.LINK_TEXT, self.home_repo.features_link_text)
            sleep(5)

            active_tab = self.ad.get_element_attribute(By.CLASS_NAME, self.home_repo.default_li_active_tab_class, 'innerHTML')
            if 'Recognition' in active_tab:
                print("By default first tab is highlighted")

            sleep(5)
            anniversary_tab = self.ad.get_element(By.CSS_SELECTOR, self.home_repo.second_li_tab_css)
            anniversary_tab.click()
            sleep(3)
            tabs_list = ['Recognition', 'Anniversaries &amp; Birthdays', 'Culture Rewards', 'Badges']
            inactive_tabs = self.ad.get_all_elements(By.CSS_SELECTOR, self.home_repo.inactive_tabs_css)

            for tab in range(len(inactive_tabs)):
                sleep(3)
                if inactive_tabs[tab].get_attribute('class') == 'nav-link':
                    if tabs_list[tab] in inactive_tabs[tab].get_attribute('innerHTML'):
                        print(tabs_list[tab] + " tab is inactive")
            sleep(3)

        except Exception as err:
            print("Unexpected error:", sys.exc_info())

    def verify_contact_us(self):
        """
        This method will verify contact us section.
        """
        try:

            self.ad.click_element(By.LINK_TEXT, self.home_repo.contact_us_link_text)
            sleep(3)

        except Exception as err:
            print("Unexpected error:", sys.exc_info())
