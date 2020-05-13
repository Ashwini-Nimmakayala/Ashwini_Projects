from automation.testbase.ActionDrivers import ActionDrivers
from automation.workflows.HomePage import HomePage
from automation.testbase.Base import Base




class Home(object):
    ad = ActionDrivers()
    home = HomePage()
    base = Base()


    def home_page(self):
        """cd ..
        This method is to validate the home page functionality.
        """

        self.home.launch_website()
        self.home.get_email_fields()
        self.home.verify_email_field()
        self.home.verify_features_tab()
        self.home.verify_contact_us()
        self.base.driver.close()


home = Home()
home.home_page()
